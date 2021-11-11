from bs4 import BeautifulSoup
import requests


def extract_news(date, category1, category2):
    records = []
    for page in range(1, 100):
        if category2 is not None:
            url = "https://news.daum.net/breakingnews/{}/{}?page={}&regDate={}".format(category1, category2, page, date)
        else:
            url = "https://news.daum.net/breakingnews/{}?page={}&regDate={}".format(category1, page, date)

        request = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        soup = BeautifulSoup(request.text, "html.parser")
        target = "#mArticle > div.box_etc > ul > li"
        news_list = soup.select(target)

        # Stop condition -> Last Page
        if not news_list:
            break

        for news in news_list:
            record = news.select(".cont_thumb > .tit_thumb > .link_txt")[0]
            link = record.get("href")
            title = record.text.strip()
            records.append([title, link])

    return records



