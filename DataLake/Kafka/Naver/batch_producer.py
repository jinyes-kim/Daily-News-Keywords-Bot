from kafka import KafkaProducer
from fastavro import reader


# Kafka info
broker = ["192.168.0.9:9092"]
topic = "news_test"
producer = KafkaProducer(bootstrap_servers=broker)


with open('/Users/jinyes/git/Daily-News-Keywords-Bot/Data/20210917.avro', 'rb') as fo:
    avro_reader = reader(fo)
    for record in avro_reader:
        producer.send(topic, record)
        producer.flush()

"""
avro 파일 읽어서
그 파일을 고대로 카프카에 전송하고
컨슈머는 다시 읽어서 Hbase로 저장하고
Hbase -> HDFS, ES 저장 

"""


