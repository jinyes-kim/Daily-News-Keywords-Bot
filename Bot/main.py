from library import slack
from library.es_query import *
from collections import defaultdict
from dependency import default_time
import json

today = default_time.today


def naver():
    slack.post_message("#news", "\n---{} 네이버 뉴스---".format(default_time.datetime.now().strftime("%Y년 %m월 %d일")))

    with open("/home/jinyes/Daily-News-Keywords-Bot/Crawler/Naver/info/category.json", 'r') as catregory:
        file = json.load(catregory)

    for subject in file["keywords"]:
        for specific_subject in file["specific_keywords"][subject]:
            # Read Data
            records = request_data(today, "NAVER", subject, specific_subject)

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
    slack.post_message("#news", "\n---{} 다음 뉴스---".format(default_time.datetime.now().strftime("%Y년 %m월 %d일")))
    with open("/home/jinyes/Daily-News-Keywords-Bot/Crawler/DAUM/info/category.json", 'r') as catregory:
        file = json.load(catregory)

    for subject in file["keywords"]:
        if subject == "보도자료" or subject == "자동생성기사":
            specific_subject_list = ["null"]
        else:
            specific_subject_list = file["specific_keywords"][subject]

        for specific_subject in specific_subject_list:
            # Read Data
            records = request_data(today, "DAUM", subject, specific_subject)

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


def main():
    cnt_time = default_time.datetime.strptime(today, "%Y년 %m월 %d일")
    try:
        naver()
    except Exception as error:
        slack.post_message("#alert", "[{}]\n네이버 뉴스 슬랙 봇 이슈 발생\n\n{}".format(cnt_time, error))
    try:
        daum()
    except Exception as error:
        slack.post_message("#alert", "[{}]\n다음 뉴스 슬랙 봇 이슈 발생\n\n{}".format(cnt_time, error))


if __name__ == "__main__":
    main()
