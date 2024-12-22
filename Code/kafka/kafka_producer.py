import json
import time
import random
from confluent_kafka import Producer

# Kafka Configuration
KAFKA_BROKER = 'localhost:9092'
KAFKA_TOPIC = 'AIR_QS'

# Initialize Producer
producer = Producer({'bootstrap.servers': KAFKA_BROKER})

# Function to generate simulated sensor data
def generate_sensor_data():
    return {
        "dust": round(random.uniform(10.0, 50.0), 2),
        "vocs": round(random.uniform(0.1, 5.0), 2),
        "co": round(random.uniform(0.01, 0.5), 2),
        "co2": round(random.uniform(300.0, 800.0), 2),
        "temperature": round(random.uniform(20.0, 35.0), 2),
        "humidity": round(random.uniform(30.0, 70.0), 2)
    }

# Function to deliver messages to Kafka
def delivery_report(err, msg):
    if err:
        print(f"Message delivery failed: {err}")
    else:
        print(f"Message delivered to {msg.topic()} partition {msg.partition()} at offset {msg.offset()}")

# Produce sensor data continuously (live stream)
try:
    print("Kafka Producer is live streaming data... Press Ctrl+C to stop.")
    while True:
        sensor_data = generate_sensor_data()
        producer.produce(KAFKA_TOPIC, value=json.dumps(sensor_data), callback=delivery_report)
        producer.flush()  # Ensure the message is sent immediately
        time.sleep(1)  # Wait for 1 second before sending the next message
except KeyboardInterrupt:
    print("Producer stopped.")
finally:
    producer.flush()
