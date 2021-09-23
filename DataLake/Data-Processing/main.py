from konlpy.tag import Okt
from pymongo import MongoClient
from datetime import datetime

today = datetime.now().strftime("%Y%m%d")
pw = open("/Users/jinyes/git/Daily-News-Keywords-Bot/pw.txt", 'r').read()
client = MongoClient(host="jinyes-server",
                     port=27017,
                     username="root",
                     password=pw)
db = client["news"]
collection = db["news_test"]

# query
records = collection.find({"date": str(today)})

jvm_path = "/Library/Java/JavaVirtualMachines/zulu-15.jdk/Contents/Home/bin/java"
okt = Okt(jvmpath=jvm_path)

for idx, record in enumerate(records):
    subject = record["subject"]
    specific_subject = record["specific_subject"]
    title = record["title"]
    noun = okt.nouns(title)
    print(subject, specific_subject, title, noun)
    if idx == 100:
        break
