from confluent_kafka import Consumer
import json

# Kafka Configuration
KAFKA_BROKER = 'localhost:9092'
KAFKA_TOPIC = 'AIR_QS'
CONSUMER_GROUP = 'AIR_GRP'

# Initialize Consumer
consumer = Consumer({
    'bootstrap.servers': KAFKA_BROKER,
    'group.id': CONSUMER_GROUP,
    'auto.offset.reset': 'earliest'  # Start reading from the beginning
})

# Subscribe to the topic
consumer.subscribe([KAFKA_TOPIC])

# Consume data continuously (live streaming)
try:
    print("Kafka Consumer is live streaming data... Press Ctrl+C to stop.")
    while True:
        msg = consumer.poll(1.0)  # Wait up to 1 second for a message
        if msg is None:  # No message available yet
            continue
        if msg.error():  # Check for any error in message
            print(f"Error: {msg.error()}")
            continue
        # Deserialize and process the message
        data = json.loads(msg.value().decode('utf-8'))
        print(f"Consumed: {data}")
except KeyboardInterrupt:
    print("Consumer stopped.")
finally:
    consumer.close()
