from elasticsearch import Elasticsearch


def request_data(date, specific_subject):
    client = Elasticsearch(host="jinyes-server", port=9200)
    result = client.search(
        index="news-test",
        query={
            "bool": {
                "must": [
                    {"match": {"@timestamp": date}},
                    {"match": {"specific_subject": specific_subject}},
                ]
            }
        }
    )
    return result
