from library.mongo_consumer import consume
from library.noun_extractor import extract_noun
from library.elasticsearch import *
from datetime import datetime


# Consume Data from MongoDB
today = datetime.now().strftime("%Y%m%d")
bson_documents = consume("news", "news", today)


# Extract Noun using Okt
bson_noun_documents = extract_noun(bson_documents)


# Remove One Letter
for bson in bson_noun_documents:
    noun_list = bson["title_noun_list"]
    processed_noun_list = []
    for noun in noun_list:
        if len(noun) == 1:
            continue
        processed_noun_list.append(noun)

    bson["title_noun_list"] = processed_noun_list


# Insert DataSet to ES
documents = []
for bson in bson_noun_documents:
    es_json = to_document(bson, date=today)
    documents.append(es_json)

insert_bulk(documents)

