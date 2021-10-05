from elasticsearch import Elasticsearch, helpers
from datetime import datetime

client = Elasticsearch(host="jinyes-server", port=9200)


def insert_bulk(documents):
    try:
        helpers.bulk(client, documents)
        print("[{}]Insert Success".format(datetime.now()))
    except Exception as Error:
        print("[{}]Insert Fail\n{}".format(datetime.now(), Error))


def to_document(bson, date):
    doc = {
        "_index": "news-test",
        "_source": {
            "subject": bson["subject"],
            "portal": bson["portal"],
            "specific_subject": bson["specific_subject"],
            "title_noun": bson["title_noun_list"],
            "@timestamp": date
        }
    }
    return doc





