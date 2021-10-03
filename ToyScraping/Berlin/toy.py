import requests
from bs4 import BeautifulSoup as bs

a=[]
for i in range(1,92):
    url = f'http://berlinreport.com/bbs/board.php?bo_table=flohmarkt&sca=%EB%B0%A9%EC%9E%88%EC%9D%8C&page='+str(i)
    re = requests.get(url)
    # html 뽑아오
    soup = bs(re.text, "html.parser")
    # 게시판의 모든 페이지 가져오
    pagination = soup.find("div",{"class": "mw_basic_page"}).find_all("a")
    # 모든 페이지에 있는 모든 제목 가져오기
    post = soup.find_all("td", {"class": "mw_basic_list_subject"})
    a = [_.text for _ in post]
    for p in a:
        list = p
        print(list.replace("삭제되었습니다.", ""))