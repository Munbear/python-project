import requests
from bs4 import BeautifulSoup as bs 


def ListOfdate():

    result = [[], [], [], [], [], [], []]

    for n in range(1,42):
        url = "https://finance.naver.com/item/sise_time.nhn?code=005930&thistime=20200327161050&page="+str(n)
        re = requests.get(url)
        soup = bs(re.text, "html.parser")
        pagination = soup.select('table > tr')

        for i in range(1, len(pagination)-1):
            if pagination[i].select('td')[0].text.strip():
                result[0].append(pagination[i].select('td')[0].text.strip())
                result[1].append(pagination[i].select('td')[1].text.strip())
                result[3].append(pagination[i].select('td')[3].text.strip())
                result[4].append(pagination[i].select('td')[4].text.strip())
                result[5].append(pagination[i].select('td')[5].text.strip())
                result[6].append(pagination[i].select('td')[6].text.strip())


    for i in range(len(result[0])):
        print(
            result[0][i],
            result[1][i],
            result[3][i],
            result[4][i],
            result[5][i],
            result[6][i]
            ) 


print(ListOfdate())     
