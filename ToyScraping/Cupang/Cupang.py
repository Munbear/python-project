import requests
from bs4 import BeautifulSoup as bs 

url = ("https://finance.yahoo.com/quote/AMZN?p=AMZN&.tsrc=fin-srch")
res = requests.get(url)
res.raise_for_status()
soup = bs(res.text, "lxml")

price = soup.find("div", attrts={"class":"D(ib) Mend(20px)"})
print(price)