from bs4 import BeautifulSoup
import time
import requests

"""
코드 리팩토링 필요함
뷰티풀 솝 적극 활용하기
"""


def extract_news(date, category1, category2):
    # 마지막 페이지 탐색
    url = "https://news.naver.com/main/list.naver?mode=LS2D&mid=shm&sid1={}&sid2={}".\
        format(category1, category2)
    request = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(request.text, "html.parser")
    last_page = soup.select(".paging > a")
    target = (".type06_headline > li > dl > dt:nth-of-type(1) > a",
              ".type06 > li > dl > dt:nth-of-type(1) > a")

    # 섹션별 뉴스 데이터 수집
    result = []
    for i in range(1, len(last_page)+2):
        url = "https://news.naver.com/main/list.naver?mode=LS2D&sid2={1}&sid1={0}&mid=shm&date={2}&page={3}".\
            format(category1, category2, date, i)
        request = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        soup = BeautifulSoup(request.content.decode("euc-kr", "replace"), "html.parser")

        for section in target:
            result.extend(soup.select(section))
        time.sleep(2)

    return result


def extract_news_title(raw_data):
    result = []
    for line in raw_data:
        line = str(line).replace("\n", '')
        if "<img" in line:
            dummy = line.split('">')
            news_url = dummy[0].replace('<a href="', '')
            news_title = dummy[1].split(" height")[0].replace("<img alt=", '')
        else:
            dummy = line.split("</a>")[0].split('">')
            news_url = dummy[0].replace('<a href="', '')
            news_title = dummy[1]

        if news_title != '':
            result.append([news_title.strip(), news_url.strip()])
    return result


