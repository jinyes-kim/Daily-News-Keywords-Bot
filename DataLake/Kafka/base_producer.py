from kafka import KafkaProducer

broker = ["localhost:9092"]
topic = "news"
producer = KafkaProducer(bootstrap_servers=broker)

# Send test message
msg = "Hello Kafka"
producer.send(topic, msg.encode("utf-8"))
producer.flush()
