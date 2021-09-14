import requests

url = "https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=100"
req = requests.get(url, headers={'User-Agent':'Mozilla/5.0'})

print(req.status_code)

