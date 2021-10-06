from pymongo import MongoClient
from datetime import datetime
import logging

pw = open("/home/jinyes/Daily-News-Keywords-Bot/pw.txt", 'r').read()
client = MongoClient(host="jinyes-server",
                     port=27017,
                     username="jinyes",
                     password=pw)
db = client.news


def to_bson(data):
    raw = data.split(",")
    doc = {
        "date": raw[0],
        "portal": raw[1],
        "subject": raw[2].strip(),
        "specific_subject": raw[3].strip(),
        "title": raw[4].strip(),
        "url": raw[5].strip(),
    }

    return doc


def main():
    dataset = []
    today = datetime.now().strftime("%Y%m%d")
    portal_list = ["NAVER", "DAUM"]
    for portal in portal_list:
        with open("/home/jinyes/Daily-News-Keywords-Bot/Data/{}{}.txt".format(portal, today), 'r') as records:
            for record in records:
                doc = to_bson(record)
                dataset.append(doc)

        try:
            db.news.insert_many(dataset, ordered=False)
        except Exception as error:
            logging.info("[{}] - {}".format(datetime.now(), error))


if __name__ == "__main__":
    logging.info("[{}] - Start Producer")
    main()
    logging.info("[{}] - Success Produce")
