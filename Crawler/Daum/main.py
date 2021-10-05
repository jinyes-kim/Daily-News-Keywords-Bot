from library.crawler import *
from library.preprocessing import *
from datetime import datetime
import json
import time
import logging

# Static variable
file = json.load(open("/home/jinyes/Daily-News-Keywords-Bot/Crawler/Naver/info/category.json", 'r'))
today = datetime.now().strftime("%Y%m%d")


def main():
    records = []

    for keyword in file["keywords"]:
        category1 = file["keyword_code"][keyword]

        if keyword == "보도자료" or keyword == "자동생성기사":
            specific_keyword_list = [None]
        else:
            specific_keyword_list = file["specific_keywords"][keyword]

        for specific_keyword in specific_keyword_list:
            category2 = file["specific_keyword_code"][specific_keyword]
            news_list = extract_news(today, category1, category2)

            for record in news_list:
                title = record[0]
                url = record[1]
                print([keyword, specific_keyword, remove_quot(title), url])
                records.append([today, "DAUM", keyword, specific_keyword, remove_quot(title), url])

            time.sleep(1)

    with open("/home/jinyes/Daily-News-Keywords-Bot/Data/DAUM{}.txt".format(today), "w") as out:
        for record in records:
            raw = ','.join(record)
            out.write(raw+'\n')


if __name__ == "__main__":
    logging.info("[{}] Start - DAUM news Crawler".format(datetime.now()))
    main()
    logging.info("[{}] Success - DAUM news Crawler".format(datetime.now()))
