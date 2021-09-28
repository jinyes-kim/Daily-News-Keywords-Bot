from pymongo import MongoClient

pw = open("/Users/jinyes/git/Daily-News-Keywords-Bot/pw.txt", 'r').read()
client = MongoClient(host="jinyes-server",
                     port=27017,
                     username="root",
                     password=pw)


def consume(db, collection, date):
    db = client[db]
    collection = db[collection]
    records = collection.find({"date": str(date)})
    return records

