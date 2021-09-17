from fastavro import reader

with open('./data/20210917.avro', 'rb') as fo:
    avro_reader = reader(fo)
    for record in avro_reader:
        print(record)