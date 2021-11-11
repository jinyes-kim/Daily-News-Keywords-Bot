import sys
sys.path.append("/home/jinyes/Daily-News-Keywords-Bot/")

from library.preprocessing import *
from library.crawler import *
from dependency import default_time
import json
import time


# Static Variable
today = default_time.today
file = json.load(open("/home/jinyes/Daily-News-Keywords-Bot/Crawler/Naver/info/category.json", 'r'))


def main():
    data_set = []
    subject_list = file["subjects"]

    for subject in subject_list:
        specific_subject_list = file["specific_subjects"][subject]
        for specific_subject in specific_subject_list:
            category1 = file["subject_code"][subject]
            category2 = file["specific_subject_code"][specific_subject]
            records = extract_news(date=today, category1=category1, category2=category2)

            for record in records:
                title = remove_quot(record[0])
                url = record[1].replace("amp;", '')
                data_set.append([today, "NAVER", subject, specific_subject, title, url])
            time.sleep(1)

    with open("/home/jinyes/Daily-News-Keywords-Bot/Data/NAVER{}.txt".format(today), "w") as out:
        for data in data_set:
            raw = ','.join(data)
            out.write(raw+'\n')

    print("[{}] Insert {}".format(default_time.datetime.now(), len(data_set)))


if __name__ == "__main__":
    print("[{}] Start - NAVER news Crawler".format(default_time.datetime.now()))
    main()
    print("[{}] Success - NAVER news Crawler".format(default_time.datetime.now()))
