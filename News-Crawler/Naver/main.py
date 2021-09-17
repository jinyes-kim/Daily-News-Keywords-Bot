from naver_news.news_crawler import *
from datetime import datetime
from kafka import KafkaProducer
import json
import time


def main():
    today = datetime.now().strftime("%Y%m%d")
    file = json.load(open("./data/category.json", 'r'))
    subject_list = file["keywords"]

    for subject in subject_list:
        specific_subject_list = file["specific_keywords"][subject]
        for specific_subject in specific_subject_list:
            category1 = file["keyword_code"][subject]
            category2 = file["specific_keyword_code"][specific_subject]
            try:
                raw = extract_article(date=today, category1=category1, category2=category2)
                news_list = preprocess_article(raw)
            except Exception as Error:
                # slack으로 에러 발생한 지점 전송
                print(Error)
                continue

            for news in news_list:
                data = ','.join([today, subject, specific_subject, news[0], news[1]])
                print(data)
                # data로 카프카에 전송하기

            time.sleep(2)


if __name__ == "__main__":
    main()
