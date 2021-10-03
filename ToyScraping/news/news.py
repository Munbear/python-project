import requests
from bs4 import BeautifulSoup as bs 



for page in range(10): # 페이즈
    url = "https://search.naver.com/search.naver?date_from=&date_option=0&date_to=&dup_remove=1&nso=&post_blogurl=&post_blogurl_without=&query=%EC%8B%A0%EC%B4%8C%EB%A7%9B%EC%A7%91&sm=tab_pge&srchby=all&st=sim&where=post&start=" + str(page * 10 + 1)
    res = requests.get(url)
    res.raise_for_status()
    soup = bs(res.text, "lxml")

    links = soup.find_all("li", attrs={"class":"sh_blog_top"})
    for blog in links:
        title = blog.find("a", attrs={"class":"sh_blog_title _sp_each_url _sp_each_title"})["title"]
        link = blog.find("a", attrs={"class":"sh_blog_title _sp_each_url _sp_each_title"})["href"]
        

        print(title)
