import requests 
from bs4 import BeautifulSoup as bs 



def Astory():  #함수 병 

    result = [], [], [], [], [], []  # [] 안에다가 넣어줄 결과값 

    for n in range(1,21):  #포문 n은 range() 함수를 써 첫번째 부터 21 개의 페이즈를 파싱함
        url = "https://finance.naver.com/item/sise_day.nhn?code=241840&page="+str(n) # 파싱알 URL 
        re = requests.get(url) # 가져온 주소에서 HTML 파일을 가져옴 
        soup = bs(re.text, "html.parser") # BeautifulSoup4 이용해 html 파싱 
        pages = soup.select("table > tr") # 내가 원하는 값이 있는 테그를 css select 이용해 가져오기 

        for i in range(1, len(pages)-1):
            if pages[i].select('td')[0].text.strip():
                result[0].append(pages[i].select('td')[0].text.strip())
                result[1].append(pages[i].select('td')[1].text.strip())
                result[2].append(pages[i].select('td')[2].text.strip())
                result[3].append(pages[i].select('td')[3].text.strip())
                result[4].append(pages[i].select('td')[4].text.strip())
                result[5].append(pages[i].select('td')[5].text.strip())

    for i in range(len(result[0])):
        print(
            result[0][i],
            result[1][i],
            result[2][i],
            result[3][i],
            result[4][i],
            result[5][i],
        )



print(Astory())




