from urllib.request import urlopen # 요청한 url를 열기 위한 라이브러리 
import urllib.request # url 요청하는 라이브러리 
from urllib.parse import quote_plus # 요청한 라이브러리의 한글화 가능하게 위해서 
from bs4 import BeautifulSoup as bs # 데이터 파싱 
from selenium import webdriver # 셀레니움 
import time 




def get_insta_img():
    Baseurl = 'https://www.instagram.com/explore/tags/'
    Plusurl = input('검색할 태그를 입력하세요 : ')
    url = Baseurl + quote_plus(Plusurl)


    path = '/Users/dowon/Downloads/chromedriver'
    driver = webdriver.Chrome(path)
    driver.get(url)

    time.sleep(3)


    html = driver.page_source
    soup = bs(html, "html.parser")

    insta = soup.select('.v1Nh3.kIKUG._bz0w')

    n = 1 
    for i in insta:
        print('https://www.instagram.com' + i.a['href'])
        imgUrl = i.select_one('.KL4Bh').img['src']
        with urlopen(imgUrl) as f: 
            with open('./instaimg/' + Plusurl + str(n) + '.jpg', 'wb') as h:
                img = f.read()
                h.write(img)
        n += 1
        print(imgUrl)



print(get_insta_img())
