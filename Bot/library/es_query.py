from elasticsearch import Elasticsearch


def request_data(date, portal, subject, specific_subject):
    client = Elasticsearch(host="jinyes-server", port=9200)
    result = client.search(
        index="news-test",
        size=10000,
        query={
            "bool": {
                "must": [
                    {"match": {"@timestamp": date}},
                    {"match": {"portal": portal}},
                    {"match": {"subject": subject}},
                    {"match": {"specific_subject": specific_subject}},
                ]
            },
        }
    )
    return result


