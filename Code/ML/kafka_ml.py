from kafka import KafkaConsumer, KafkaProducer
import json
import joblib

consumer = KafkaConsumer(
    'air',
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda v: json.loads(v.decode('utf-8')),
    auto_offset_reset='earliest',  # Start reading at the earliest message
    enable_auto_commit=True,  # Automatically commit the offsets
    group_id='1'  # Consumer group ID
)

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)


model = joblib.load('random_forest_model.pkl')

# Process messages from Kafka
try:
    for message in consumer:
        data = message.value
        print(f"Received message: {data}")

        features = [data['MQ2'], data['MQ9'], data['MQ135'], data['MQ137'], data['MQ138'], data['MG811']]  
        prediction = model.predict([features])


        result = {'prediction': prediction[0]}
       # producer.send('output_topic', value=result) # for the moment
        print(f"Sent prediction: {result}")
except KeyboardInterrupt:
    print("Stopping consumer.")
finally:
    # Ensure proper shutdown of the consumer and producer
    consumer.close()
    producer.flush()
    producer.close()
