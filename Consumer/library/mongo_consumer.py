from pymongo import MongoClient

pw = open("/home/jinyes/Daily-News-Keywords-Bot/dependency/pw.txt", 'r').read()
client = MongoClient(host="jinyes-server",
                     port=27017,
                     username="root",
                     password=pw)


def consume(db, collection, date):
    db = client[db]
    collection = db[collection]
    records = collection.find({"date": str(date)})
    return records

