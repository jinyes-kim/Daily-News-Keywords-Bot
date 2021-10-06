from elasticsearch import Elasticsearch, helpers
from datetime import datetime
import logging
client = Elasticsearch(host="jinyes-server", port=9200)


def insert_bulk(documents):
    try:
        helpers.bulk(client, documents)
        return True
    except Exception as error:
        logging.getLogger("[{}] Error Log\n\n {}".format(datetime.now(), error))
        return False


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





