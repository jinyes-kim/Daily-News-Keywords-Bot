from kafka import KafkaConsumer

broker = ['jinyes-server:9092']
topic = "news_test"
consumer = KafkaConsumer(topic,
                         group_id="group_1",
                         bootstrap_servers=broker,
                         auto_offset_reset="earliest")

try:
    for msg in consumer:
        print("Topic: {}\nPartition: {}\nOffset: {}\nKey: {}\nValue: {}\n".format(
            msg.topic, msg.partition, msg.offset, msg.key, msg.value.decode("utf-8")))

except KeyboardInterrupt:
    exit(0)