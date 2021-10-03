import requests
from bs4 import BeautifulSoup as bs 


def extract_data():

    result = [[], [], []]

    for n in range(1,26):
        url = "https://finance.naver.com/item/sise_day.nhn?code=005930&page="+str(n)
        re = requests.get(url)
        soup = bs(re.text, "html.parser")
        tr = soup.select('table > tr')

        for i in range(1, len(tr)-1):
            if tr[i].select('td')[0].text.strip():
                result[0].append(tr[i].select('td')[0].text.strip())
                result[1].append(tr[i].select('td')[1].text.strip())
                result[2].append(tr[i].select('td')[6].text.strip())

    for i in range(len(result[0])):
        print(result[0][i], result[1][i], result[2][i])


print(extract_data())
        
        

