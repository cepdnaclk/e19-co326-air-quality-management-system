from kafka import KafkaProducer
import json
import time
import random

# Initialize Kafka producer
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def generate_message():
    return {
        'MQ2': random.uniform(260, 1300),
        'MQ9': random.uniform(340, 1400),
        'MQ135': random.uniform(750, 1800),
        'MQ137': random.uniform(1300, 2000),
        'MQ138': random.uniform(700, 2000),
        'MG811': random.uniform(1700, 2700)
    }

# Continuously send messages
try:
    while True:
        message = generate_message()
        producer.send('air', value=message)
        print(f"Sent message: {message}")
        time.sleep(1)  # Send data every second
except KeyboardInterrupt:
    print("Stopping producer.")
finally:
    producer.flush()
    producer.close()
