from pymongo import MongoClient
from datetime import datetime

pw = open("../pw.txt", 'r').read()
client = MongoClient(host="jinyes-server",
                     port=27017,
                     username="jinyes",
                     password=pw)
db = client.news


def to_bson(data):
    raw = data.split(",")
    doc = {
        "date": raw[0],
        "subject": raw[1].strip(),
        "specific_subject": raw[2].strip(),
        "title": raw[3].strip(),
        "url": raw[4].strip(),
    }

    return doc


def main():
    dataset = []
    today = str(int(datetime.now().strftime("%Y%m%d"))-1)
    portal_list = ["NAVER", "DAUM"]
    for portal in portal_list:
        with open("../Data/{}{}.txt".format(portal, today), 'r') as records:
            for record in records:
                doc = to_bson(record)
                dataset.append(doc)

        db.news_test.insert_many(dataset)   # collection 네임 수정


if __name__ == "__main__":
    main()
