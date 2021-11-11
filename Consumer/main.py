from library.mongo_consumer import consume
from library.noun_extractor import extract_noun
from library.elasticsearch import *
from dependency import default_time

today = default_time.today

# Consume Data from MongoDB
bson_documents = consume("news", str(today), today)


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


if insert_bulk(documents):
    print("[{}] ElasticSearch - Insert Success".format(datetime.now()))
else:
    print("[{}] ElasticSearch - Insert Fail".format(datetime.now()))
