from naver_news.preprocessing import *
from naver_news.crawler import *
from naver_news.avro_schema import *
from datetime import datetime
import json
import time

# Static Variable
today = datetime.now().strftime("%Y%m%d")
file = json.load(open("info/category.json", 'r'))


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
                print(Error)    # slack 에러 발생한 지점 전송
                continue

            for record in news_list:
                title = remove_quot(record[0])
                url = record[1]
                records.append(to_json(today, subject, specific_subject, title, url))

            time.sleep(1)
    to_avro(today, records)


if __name__ == "__main__":
    main()
