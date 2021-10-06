from library.crawler import *
from library.preprocessing import *
from datetime import datetime
import json
import time
import logging

# Static variable
file = json.load(open("/home/jinyes/Daily-News-Keywords-Bot/Crawler/Daum/info/category.json", 'r'))
today = datetime.now().strftime("%Y%m%d")


def main():
    data_set = []
    subject_list = file["subjects"]

    for subject in subject_list:
        category1 = file["subject_code"][subject]
        if subject == "보도자료" or subject == "자동생성기사":
            specific_subject_list = [None]
        else:
            specific_subject_list = file["specific_subjects"][subject]

        for specific_subject in specific_subject_list:
            if specific_subject is not None:
                category2 = file["specific_subject_code"][specific_subject]
            else:
                category2 = None

            records = extract_news(today, category1, category2)

            for record in records:
                title = record[0]
                url = record[1]
                data_set.append([today, "DAUM", subject, specific_subject, remove_quot(title), url])

            time.sleep(1)

    with open("/home/jinyes/Daily-News-Keywords-Bot/Data/DAUM{}.txt".format(today), "w") as out:
        for data in data_set:
            raw = ','.join(data)
            out.write(raw+'\n')


if __name__ == "__main__":
    logging.getLogger("[{}] Start - DAUM news Crawler".format(datetime.now()))
    main()
    logging.getLogger("[{}] Success - DAUM news Crawler".format(datetime.now()))
