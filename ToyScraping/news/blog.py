import requests
from bs4 import BeautifulSoup as bs 



for page in range(10): # url의 첫 페이지가 1 부터 시작해서 다음 페이지는 11 그다음 페이지는 21 씩 이렇게 10씩 증가 
    # 크롤링 하려고 한 페이지의 url 정보 + str(page * 10 + 1) url의 마지막 부분을 보면 페이지 이동에 따라 숫자가 변경하는걸 확일 할 수가 있음 
    url = "https://search.naver.com/search.naver?date_from=&date_option=0&date_to=&dup_remove=1&nso=&post_blogurl=&post_blogurl_without=&query=%EC%8B%A0%EC%B4%8C%EB%A7%9B%EC%A7%91&sm=tab_pge&srchby=all&st=sim&where=post&start=" + str(page * 10 + 1)
    # res 란 변수 명을 지정해서 크롤링 하고자한 url 값을 요청하기
    res = requests.get(url)
    # 요청을 했을때 잘 요청이 됬는지 안됬는지 확이하려고 raise_for_status()를 쓴다 만약 요청이 되지 않았을때 에러를 보내는 역활을 한다 
    res.raise_for_status()
    #Beautifulsoup 를 써서 웹 페이지의 html를 뽑아 온다 
    soup = bs(res.text, "lxml")

    # 위에서 뽑아온 soup(html) 에서 내가 필요한 정보가 담긴 테그와 클래스를 확인 후 추줄 
    links = soup.find_all("li", attrs={"class":"sh_blog_top"}) 
    # 이제 내가 뽑고 싶은 데이터를 반복해서 원하는 만큼 추줄 하게 반복문을 돌려준다 
    for blog in links:
        # 블로그 제목을 가져온다 이 코드는 위에서 뽑은 li의 정보 안에 있는 테그와 제목 테그와 클라스이다 a 안에 텍스트 값이 없고
        # 타이틀 속성 안에 원하는 제목이 있어 ["title"] 을 사용해서 타이틀 안에 있는 값을 가져왔다 
        title = blog.find("a", attrs={"class":"sh_blog_title _sp_each_url _sp_each_title"})["title"]
        #위 와 같은 방법으로 추출한 블로그의 url 주소이다 뒤에 ["href"] 가 없으면 그 url로 이동 할 수 없기 때문에 붙여줬다
        link = blog.find("a", attrs={"class":"sh_blog_title _sp_each_url _sp_each_title"})["href"]
        
        #내가 만든 코드가 잘 동작하는 지 확인 하기위해 프린트를 해주었다 
        print(title)