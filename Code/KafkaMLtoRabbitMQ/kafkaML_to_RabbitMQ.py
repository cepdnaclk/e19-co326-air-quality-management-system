from kafka import KafkaConsumer
import json
import joblib
import pika

# Kafka Consumer setup
consumer = KafkaConsumer(
    'air',
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda v: json.loads(v.decode('utf-8')),
    auto_offset_reset='earliest',  # Start reading at the earliest message
    enable_auto_commit=True,  # Automatically commit the offsets
    group_id='1'  # Consumer group ID
)

# Load the pre-trained ML model
model = joblib.load('random_forest_model.pkl')

# RabbitMQ setup
rabbit_connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
rabbit_channel = rabbit_connection.channel()

# Declare a topic queue
rabbit_channel.queue_declare(queue='air_predictions')

# Process messages from Kafka
try:
    for message in consumer:
        data = message.value
        print(f"Received message: {data}")

        # Prepare data for prediction
        features = [data['MQ2'], data['MQ9'], data['MQ135'], data['MQ137'], data['MQ138'], data['MG811']]
        prediction = model.predict([features])

        # Convert the prediction to a Python native int
        prediction_value = int(prediction[0])  # Ensure it is a native Python int

        # Create a result object
        result = {'prediction': prediction_value}
        print(f"Prediction: {result}")

        # Publish to RabbitMQ
        rabbit_channel.basic_publish(
            exchange='',
            routing_key='air_predictions',
            body=json.dumps(result)  # Ensure the result is serializable
        )
        print(f"Sent prediction to RabbitMQ: {result}")
except KeyboardInterrupt:
    print("Stopping consumer.")
except Exception as e:
    print(f"Error occurred: {e}")
finally:
    # Ensure proper shutdown of resources
    consumer.close()
    rabbit_connection.close()

