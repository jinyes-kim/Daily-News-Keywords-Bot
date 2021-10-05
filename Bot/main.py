from library import slack
from library.es_query import *
from collections import defaultdict
from datetime import datetime
import json

today = datetime.now().strftime("%Y%m%d")


def naver():
    slack.post_message("#news", "\n---{} 네이버 뉴스---".format(datetime.now().strftime("%Y년 %m월 %d일")))

    with open("/home/jinyes/Daily-News-Keywords-Bot/Crawler/Naver/info/category.json", 'r') as catregory:
        file = json.load(catregory)

    for subject in file["keywords"]:
        for specific_subject in file["specific_keywords"][subject]:
            # Read Data
            records = request_data(today, "NAVER", keyword, specific_subject)

            # Count Nouns
            noun_dict = defaultdict(int)
            for record in records["hits"]["hits"]:
                noun_list = record["_source"]["title_noun"]
                for noun in noun_list:
                    noun_dict[noun] += 1

            rank_list = []
            for noun, cnt in noun_dict.items():
                rank_list.append([noun, cnt])

            # Sort
            rank_list.sort(key=lambda x: x[1], reverse=True)
            limit = rank_list[2][1]

            # Result
            msg = "[{}]\n".format(specific_subject)
            for keyword, cnt in rank_list:
                if cnt >= limit:
                    msg += "{}: {}회 등장\n".format(keyword, cnt)
                else:
                    break

            # Send Message
            slack.post_message("#news", msg+"\n")


def daum():
    slack.post_message("#news", "\n---{} 다음 뉴스---".format(datetime.now().strftime("%Y년 %m월 %d일")))
    with open("/home/jinyes/Daily-News-Keywords-Bot/Crawler/DAUM/info/category.json", 'r') as catregory:
        file = json.load(catregory)

    for keyword in file["keywords"]:
        if keyword == "보도자료" or keyword == "자동생성기사":
            specific_keyword_list = [None]
        else:
            specific_keyword_list = file["specific_keywords"][keyword]

        for specific_keyword in specific_keyword_list:
            # Read Data
            records = request_data(today, "DAUM", keyword, specific_keyword)

            # Count Nouns
            noun_dict = defaultdict(int)
            for record in records["hits"]["hits"]:
                noun_list = record["_source"]["title_noun"]
                for noun in noun_list:
                    noun_dict[noun] += 1

            rank_list = []
            for noun, cnt in noun_dict.items():
                rank_list.append([noun, cnt])

            # Sort
            rank_list.sort(key=lambda x: x[1], reverse=True)
            limit = rank_list[2][1]

            # Result
            msg = "[{}]\n".format(specific_keyword)
            for keyword, cnt in rank_list:
                if cnt >= limit:
                    msg += "{}: {}회 등장\n".format(keyword, cnt)
                else:
                    break

            # Send Message
            slack.post_message("#news", msg+"\n")


def main():
    naver()
    daum()


if __name__ == "__main__":
    main()
