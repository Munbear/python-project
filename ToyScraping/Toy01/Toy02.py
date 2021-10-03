import requests
from bs4 import BeautifulSoup as bs 

url = "https://search.daum.net/search?nil_suggest=btn&w=tot&DA=SBC&q=%EC%86%A1%ED%8C%8C+%ED%97%AC%EB%A6%AC%EC%98%A4%EC%8B%9C%ED%8B%B0"
res = requests.get(url)
res.raise_for_status() # 200 OK 코드가 아닌 경우 에러 발동
soup = bs(res.text, "html.parser")

# with open("quiz.html", "w", encoding="utf8") as f: #출력값 html 파일로 만들기 
    # f.write(soup.prettify())

data_rows = soup.find("table", attrs={"class":"tbl"}).find("tbody").find_all("tr")
for index, row in enumerate(data_rows):
    columns = row.find_all("td")

    print("========== 매물 {} ==========".format(index+1))
    print("거래 :", columns[0].get_text().strip())
    print("면적 :", columns[1].get_text().strip())
    print("가격 :", columns[2].get_text().strip())
    print("동 :", columns[3].get_text().strip())
    print("층 :", columns[4].get_text().strip())

#next_sibling 은 다음 엘리먼트 값으 가져온다 )