import pika

connection_parameters = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

channel.queue_declare(queue='letterbox')

channel.basic_consume(queue='letterbox', auto_ack=True, on_message_callback=lambda ch, method, properties, body: print(f" [x] Received :{body}"))

print('Starting consuming...')

channel.start_consuming()