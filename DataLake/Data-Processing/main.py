from pymongo import MongoClient
from datetime import datetime

pw = open("/Users/jinyes/git/Daily-News-Keywords-Bot/pw.txt", 'r').read()
today = datetime.now().strftime("%Y%m%d")
client = MongoClient(host="jinyes-server",
                     port=27017,
                     username="root",
                     password=pw)

db = client["news"]
collection = db["news_test"]
records = collection.find({"date": str(today)})


for record in records:
    print(record)
    break