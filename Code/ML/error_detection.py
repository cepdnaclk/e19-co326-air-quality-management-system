from confluent_kafka import Consumer, Producer, KafkaException
import json
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import logging
import numpy as np

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Initialize Kafka consumer
consumer_conf = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'error-detection-group',
    'auto.offset.reset': 'earliest'
}
consumer = Consumer(consumer_conf)
consumer.subscribe(['air'])

# Initialize Kafka producer
producer = Producer({'bootstrap.servers': 'localhost:9092'})

# Manually provided mean and standard deviation values
sensor_stats = {
    'MQ2': {'mean': 587, 'std_dev': 190},
    'MQ9': {'mean': 653, 'std_dev': 173},
    'MQ135': {'mean': 1166, 'std_dev': 208},
    'MQ137': {'mean': 1609, 'std_dev': 118},
    'MQ138': {'mean': 1300, 'std_dev': 279},
    'MG811': {'mean': 2000, 'std_dev': 500}
}

def validate_sensor_data(data):
    required_fields = ['sensor_id', 'timestamp', 'MQ2', 'MQ9', 'MQ135', 'MQ137', 'MQ138', 'MG811']
    for field in required_fields:
        if field not in data or data[field] is None:
            return False
    return True

def handle_missing_data(data):
    sensor_id = data.get('sensor_id', 'unknown')
    timestamp = data.get('timestamp', time.time())
    
    missing_data_alert = {
        'sensor_id': sensor_id,
        'timestamp': timestamp,
        'status': 'missing_data'
    }
    logging.warning(f"Missing data detected: {missing_data_alert}")
    
    # Send the alert to Kafka-ML topic
    # send_to_kafka_ml(missing_data_alert)
    
    # Notify stakeholders (e.g., via email, SMS, etc. - this is a placeholder)
    # notify_stakeholders(missing_data_alert)
    
    # Attempt data correction
    corrected_data = correct_data(data)
    if corrected_data:
        send_to_kafka_ml(corrected_data)

def handle_anomalies(data):
    anomalies = detect_anomalies(data)
    if anomalies:
        for sensor, value in anomalies.items():
            anomaly_alert = {
                'sensor_id': data['sensor_id'],
                'timestamp': data['timestamp'],
                'sensor': sensor,
                'value': value,
                'status': 'anomaly_detected'
            }
            logging.warning(f"Anomaly detected: {anomaly_alert}")
            
            # Send the alert to Kafka-ML topic
            # send_to_kafka_ml(anomaly_alert)
            
            # Notify stakeholders (e.g., via email, SMS, etc. - this is a placeholder)
            # notify_stakeholders(anomaly_alert)

def send_to_kafka_ml(data):
    producer.produce('kafka-ml', value=json.dumps(data).encode('utf-8'))
    producer.flush()

def correct_data(data):
    default_values = {
        'MQ2': 587.458537,   
        'MQ9': 653.465583,
        'MQ135': 1166.036856,
        'MQ137': 1609.279675,
        'MQ138': 1302.121951,
        'MG811': 1467.879232
    }

    for key in default_values:
        if key not in data or data[key] is None:
            data[key] = default_values[key]
            logging.info(f"Imputed missing value for {key} with default value: {default_values[key]}")

def detect_anomalies(data, threshold=3):
    anomalies = {}
    for key in sensor_stats:
        if key in data:
            mean = sensor_stats[key]['mean']
            std_dev = sensor_stats[key]['std_dev']
            if std_dev > 0:  # Avoid division by zero
                z_score = (data[key] - mean) / std_dev
                if abs(z_score) > threshold:
                    anomalies[key] = data[key]
    return anomalies

def consume_and_process():
    while True:
        msg = consumer.poll(timeout=1.0)
        if msg is None:
            continue
        if msg.error():
            if msg.error().code() == KafkaException._PARTITION_EOF:
                print('End of partition reached {0}/{1}'.format(msg.topic(), msg.partition()))
            elif msg.error():
                raise KafkaException(msg.error())
        else:
            data = json.loads(msg.value().decode('utf-8'))
            if not validate_sensor_data(data):
                handle_missing_data(data)
            else:
                # Detect anomalies
                handle_anomalies(data)
                
                # Send valid data to Kafka-ML for prediction
                send_to_kafka_ml(data)

try:
    consume_and_process()
except KeyboardInterrupt:
    pass
finally:
    consumer.close()
