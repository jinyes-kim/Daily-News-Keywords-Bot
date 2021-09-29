from library import slack
from library.es_query import *
from collections import defaultdict


def main():
    for specific_subject in ["청와대", "사회일반"]:
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

        # Send Message
        slack.post_message("#news", msg)


if __name__ == "__main__":
    main()
