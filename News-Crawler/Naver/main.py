from naver_crawler import *
from datetime import datetime
from pprint import pprint
import json
import time


def main():
    today = datetime.now().strftime("%Y%m%d")
    file = json.load(open("category.json", 'r'))
    subject_list = file["keywords"]

    idx = 0
    for subject in subject_list:
        specific_subject_list = file["specific_keywords"][subject]

        for specific_subject in specific_subject_list:
            category1 = file["keyword_code"][subject]
            category2 = file["specific_keyword_code"][specific_subject]
            try:
                raw = extract_article(date=today, category1=category1, category2=category2)
                result = preprocess_article(raw)
            except Exception as Error:
                # slack으로 에러 발생한 지점 전송
                continue
            idx += len(result)
            pprint(result)

            time.sleep(5)

    print(idx)


if __name__ == "__main__":
    main()
