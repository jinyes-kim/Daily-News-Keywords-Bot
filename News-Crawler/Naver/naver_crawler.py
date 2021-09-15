import time
import requests
from bs4 import BeautifulSoup


def extract_article(date, category1, category2):
    result = []
    # 최대 페이지 체크
    url = "https://news.naver.com/main/list.naver?mode=LS2D&mid=shm&sid1={}&sid2={}".format(category1, category2)
    request = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(request.text, "html.parser")
    limit = soup.select(".paging > a")
    target = (".type06_headline > li > dl > dt:nth-child(1) > a",
              ".type06 > li > dl > dt:nth-child(1) > a")

    # 섹션 별 데이터 수집
    for i in range(1, len(limit)+2):
        url = "https://news.naver.com/main/list.naver?mode=LS2D&sid2={1}&sid1={0}&mid=shm&date={2}&page={3}".\
            format(category1, category2, date, i)
        request = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        soup = BeautifulSoup(request.content.decode("euc-kr", "replace"), "html.parser")
        for section in target:
            result.extend(soup.select(section))
        time.sleep(2) # delay

    return result


def preprocess_article(raw_data):
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
            result.append([remove_quot(news_title).strip(), news_url.strip()])
    return result


def remove_quot(letter):
    quot_list = ['"', "'", "&quot", ";", ",", "...", "..", "…", '‘', '’', '“', '”']
    for tmp in quot_list:
        letter = letter.replace(tmp, '')
    return letter

