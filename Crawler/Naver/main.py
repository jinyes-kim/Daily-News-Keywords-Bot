from library.preprocessing import *
from library.crawler import *
from datetime import datetime
import json
import time


# Static Variable
today = str(int(datetime.now().strftime("%Y%m%d"))-1)
file = json.load(open("/home/jinyes/Daily-News-Keywords-Bot/Crawler/Naver/info/category.json", 'r'))


def main():
    records = []
    subject_list = file["keywords"]
    for subject in subject_list:
        specific_subject_list = file["specific_keywords"][subject]
        for specific_subject in specific_subject_list:
            category1 = file["keyword_code"][subject]
            category2 = file["specific_keyword_code"][specific_subject]
            try:
                raw = extract_news(date=today, category1=category1, category2=category2)
                news_list = extract_news_title(raw)
            except Exception as Error:
                continue

            for record in news_list:
                title = remove_quot(record[0])
                url = record[1].replace("amp;", '')
                records.append([today, "NAVER", subject, specific_subject, title, url])
            time.sleep(1)

    with open("/home/jinyes/Daily-News-Keywords-Bot/Data/NAVER{}.txt".format(today), "w") as out:
        for record in records:
            raw = ','.join(record)
            out.write(raw+'\n')


if __name__ == "__main__":
    print("[{}] Start - NAVER news Crawler".format(datetime.now()))
    main()
    print("[{}] Success - NAVER news Crawler".format(datetime.now()))
