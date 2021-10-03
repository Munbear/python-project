import requests
from bs4 import BeautifulSoup as bs 
import re 

url ="https://www.coupang.com/np/search?q=%EC%97%90%EC%96%B4%ED%8C%9F&channel=recent"
headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36"
}
res = requests.get(url, headers=headers)
soup = bs(res.text, "lxml")


items = soup.find_all("li", attrs={"class":re.compile("^search-product")})
# print(items[0].find("div", attrs={"class":"name"}).get_text())

for item in items:
    name = item.find("div", attrs={"class":"name"}).get_text()
    price = item.find("strong", attrs={"class":"price-value"}).get_text()
    rating = item.find("em", attrs={"class":"rating"}).get.text()

    print(name,price,rating)

