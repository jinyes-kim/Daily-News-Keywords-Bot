from fastavro import parse_schema, writer, reader

schema = {
    'doc': 'Daily News Keywords',
    'name': 'news',
    'namespace': 'NAVER',
    'type': 'record',
    'fields': [
        {'name': 'date', 'type': 'string'},
        {'name': 'subject', 'type': 'string'},
        {'name': 'specific_subject', 'type': 'string'},
        {'name': 'title', 'type': 'string'},
        {'name': 'url', 'type': 'string'},
    ],
}


def to_json(date, subject, specific_subject, title, url):
    record = {
        "date": date,
        "subject": subject,
        "specific_subject": specific_subject,
        "title": title,
        "url": url
    }
    return record


def to_avro(save_as, records):
    parsed_schema = parse_schema(schema)
    with open("./data/{}.avro".format(save_as), 'wb') as out:
        writer(out, parsed_schema, records)


