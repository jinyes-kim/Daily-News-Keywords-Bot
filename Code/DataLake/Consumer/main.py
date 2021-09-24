from lib.mongo_consumer import consume
from lib.noun_extractor import extract_noun
from lib.es_format import *
from datetime import datetime

# Consume Data from MongoDB
today = datetime.now().strftime("%Y%m%d")
bson_documents = consume("news", "news_test", today)


# Extract Noun using Okt
bson_noun_documents = extract_noun(bson_documents)


# Insert DataSet to ES
documents = []
for bson in bson_noun_documents:
    es_json = to_document(bson, date=today)
    documents.append(es_json)

insert_bulk(documents)

