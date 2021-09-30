from library import slack
from library.es_query import *
from collections import defaultdict
import json


def main():
    with open("/Users/jinyes/git/Daily-News-Keywords-Bot/Crawler/Naver/info/category.json") as catregory:
        file = json.load(catregory)

    for subject in file["keywords"]:
        for specific_subject in file["specific_keywords"][subject]:
            # Read Data
            records = request_data("20210924", specific_subject)

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


if __name__ == "__main__":
    main()
