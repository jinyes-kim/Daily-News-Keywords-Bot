from library import slack
from library.es_query import *
from collections import defaultdict
from datetime import datetime
import json
from pprint import pprint


def main():
    slack.post_message("#news", "---{}---".format(datetime.now().strftime("%Y년 %m월 %d일")))
    today = str(int(datetime.now().strftime("%Y%m%d"))-1)
    with open("/Users/jinyes/git/Daily-News-Keywords-Bot/Crawler/Naver/info/category.json") as catregory:
        file = json.load(catregory)

    for subject in file["keywords"]:
        for specific_subject in file["specific_keywords"][subject]:
            # Read Data
            records = request_data(today, specific_subject)

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
            slack.post_message("#news", msg)
            slack.post_message("#news", "\n")


if __name__ == "__main__":
    main()
