from pymongo import MongoClient

pw = open("../../pw.txt", 'r').read()
open("../../pw.txt", 'r')
client = MongoClient(host="jinyes-server",
                     port=27017,
                     username="root",
                     password=pw)


def consume(db, collection, date):
    db = client[db]
    collection = db[collection]
    records = collection.find({"date": str(date)})
    return records

