import requests
from bs4 import BeautifulSoup as bs
from datetime import datetime
import time


def get_code(company_code):
    url = "https://finance.naver.com/item/main.nhn?code=" + company_code
    re = requests.get(url)
    soup = bs(re.content, "html.parser")
    return soup

def get_price(company_code):
    soup = get_code(company_code)
    re_soup = soup.find("p", {"class":"no_today"})
    price = re_soup.find("span", {"class":"blind"})
    clean_text = price.text
    return clean_text


company_codes = ["005930","005935","066570"]

for i in company_codes:
    clean_text = get_price(i)
    print(clean_text)






