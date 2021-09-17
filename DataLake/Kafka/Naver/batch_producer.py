from kafka import KafkaProducer
from datetime import datetime

broker = ["jinyes-server:9092"]
topic = "news_test"
producer = KafkaProducer(bootstrap_servers=broker)
today = datetime.now().strftime("%Y%m%d")

with open("/Users/jinyes/git/Daily-News-Keywords-Bot/Data/{}.txt".format(today)) as file:
    for record in file:
        producer.send(topic=topic, value=record.encode("utf-8"))
        producer.flush()