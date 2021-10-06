from bs4 import BeautifulSoup
import requests


def extract_news(date, category1, category2):
    cache1, cache2 = None, None
    records = []

    for i in range(1, 100):
        url = "https://news.naver.com/main/list.naver?mode=LS2D&sid2={1}&sid1={0}&mid=shm&date={2}&page={3}". \
            format(category1, category2, date, i)
        request = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        soup = BeautifulSoup(request.content.decode("euc-kr", "replace"), "html.parser")

        target1 = "#main_content > div.list_body.newsflash_body > ul.type06_headline > li > dl > dt > a"
        target2 = "#main_content > div.list_body.newsflash_body > ul.type06 > li > dl > dt > a"

        merged_list = []
        news1_list = soup.select(target1)
        news2_list = soup.select(target2)
        merged_list.extend(news1_list)
        merged_list.extend(news2_list)

        # Stop condition1
        try:
            if cache1 == news1_list[-1].text.strip():
                break
            cache1 = news1_list[-1].text.strip()
        except:
            pass

        # Stop condition2
        try:
            if cache2 == news2_list[-1].text.strip():
                break
            cache2 = news2_list[-1].text.strip()
        except:
            pass

        for raw in merged_list:
            if raw.select("img"):
                continue
            title = raw.text.strip()
            url = raw.get("href")
            records.append([title, url])

    return records


