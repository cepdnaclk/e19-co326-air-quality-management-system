import paho.mqtt.client as mqtt
import time
import json
import os
import random

def generate_message():
    return {
        'MQ2': random.randint(260, 1300),
        'MQ9': random.randint(340, 1400),
        'MQ135': random.randint(750, 1800),
        'MQ137': random.randint(1300, 2000),
        'MQ138': random.randint(700, 2000),
        'MG811': random.randint(1700, 2700)
    }

broker = os.getenv('BROKER')
port = 8883

MY_DEVICE = os.getenv('MY_DEVICE')
MY_TENANT = os.getenv('MY_TENANT')
password = os.getenv('MY_PWD')

if not MY_DEVICE or not MY_TENANT or not password:
    raise ValueError("Environment variables MY_DEVICE, MY_TENANT, or MY_PWD are not set.")

# Create the username in the format "device_id@tenant_id"
username = f'{MY_DEVICE}@{MY_TENANT}'
topic = 'telemetry'  

# Path to the CA certificate bundle on Ubuntu
ca_cert_path = "/etc/ssl/certs/ca-certificates.crt"  

# Create an MQTT client instance
client = mqtt.Client(protocol=mqtt.MQTTv5)  
client.username_pw_set(username, password)

# Enable SSL/TLS
client.tls_set(ca_cert_path)  
client.tls_insecure_set(False) 


def on_connect(client, userdata, flags, reasonCode, properties=None):
    if reasonCode == 0:
        print("Connected successfully")
    else:
        print(f"Connection failed with reason code {reasonCode}")


def on_publish(client, userdata, mid, properties=None, reasonCode=None):
    if reasonCode is None or reasonCode == 0:
        print(f"Message {mid} published successfully")
    else:
        print(f"Message {mid} failed to publish with reason code {reasonCode}")
    print("")

# Assign the callback functions to the client
client.on_connect = on_connect
client.on_publish = on_publish

# Connect to the MQTT broker
client.connect(broker, port, keepalive=60)  
# Maintain the connection
client.loop_start() 


try:
    while True:
        if client.is_connected():
            message = generate_message()  # Generate sensor data message
            result = client.publish(topic, json.dumps(message))
            status = result.rc
            if status == mqtt.MQTT_ERR_SUCCESS:
                print(f"Published message: {json.dumps(message)} to topic {topic}")
            else:
                print(f"Failed to send message to topic {topic} with status code {status}")
        else:
            print("Client is not connected, attempting to reconnect...")
            client.reconnect()
        time.sleep(3)  # Wait for 3 seconds before publishing the next message

except KeyboardInterrupt:
    print("Interrupted by user. Disconnecting...")
    client.disconnect()
    client.loop_stop()

