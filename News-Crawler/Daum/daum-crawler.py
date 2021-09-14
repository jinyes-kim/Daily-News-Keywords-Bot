import requests

url = "https://news.daum.net/politics#1"
req = requests.get(url, headers={'User-Agent':'Mozilla/5.0'})

print(req.status_code)