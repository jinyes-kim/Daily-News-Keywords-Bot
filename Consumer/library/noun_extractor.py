from konlpy.tag import Okt

#jvm_path = "/Library/Java/JavaVirtualMachines/zulu-15.jdk/Contents/Home/bin/java"
#okt = Okt(jvmpath=jvm_path)
okt = Okt()


def extract_noun(records):
    documents = []
    for record in records:
        title = record["title"]
        noun_list = okt.nouns(title)
        record["title_noun_list"] = noun_list
        documents.append(record)

    return documents


