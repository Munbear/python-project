import requests
from bs4 import BeautifulSoup as bs

url = "https://finance.daum.net/api/search/ranks?limit=10"

headers = {
    "Referer": "https://finance.daum.net/",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
}

response = requests.get(url, headers=headers)
datas = response.json()
DataList = datas['data']
print(DataList)

for data in DataList:
    print(data['rank'],
          data['name'],
          data['tradePrice'])


