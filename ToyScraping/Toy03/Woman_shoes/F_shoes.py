import requests
from bs4 import BeautifulSoup as bs 
import re 
from urllib.request import urlopen



for pages in range(1,6):
    url = "https://shop.adidas.co.kr/PF020201.action?command=LIST&ALL=ALL&S_CTGR_CD=01002001&CONR_CD=10&S_ORDER_BY=1&S_PAGECNT=100&PAGE_CUR={}&S_SIZE=&S_TECH=&S_COLOR=&S_COLOR2=&CATG_CHK=&CATG_CLK=&STEP_YN=N&S_QUICK_DLIVY_YN=&S_PRICE=&S_STATE1=&S_STATE2=&S_STATE3=&NFN_ST=Y".format(pages)
    headers ={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36"}
    res = requests.get(url, headers=headers)
    soup = bs(res.text, "lxml")


    items = soup.find_all("div", attrs={"class":"inner"})  # dic 테그 안에 inner 클래인 것을 추출하기
    for idx, item in enumerate(items): # items을 반복해서 inner 클래스를 가진 모든 div 테그 추출 
        name = item.find("div", attrs={"class":"info_title"}).get_text() # 추출한 데이터에서 title만 가져오기 
        price = item.find("div", attrs={"class":"sale"}) #세일한 가격만 가져오기 
        if price: #세일한 가격이 있으면 텍스트를 뽑아라 
            price = price.get_text()
        else: # 세일한 가격 데이터가 없으면 info_price 클래스를 가진 div 에서 가격을 추출하라 
            price = item.find("div", attrs={"class":"info_price"}).get_text()

        re_price = " ".join(price.split())  #추출한 가격에 쓸대 없이 빈공간이 많아서 replace  정규식을 써서 빈공간 제거 
        code = item.find("a") # 신발 제품 코드가 들어가 있는 테그 a 테그를 추출 
        codes = code['href'] # href 줄만 다시 추출 
        re_code = codes[20:26] # 거기서 코드만 있는 부문만 자르기 

        images = item.find("img")["src"] # 이미지 테그에 src이 있는 부분 추출 
        if images.startswith("//"): # 추출한 이미지 데이터 앞부분에 // 가있으면 
            images = "https:" + images # 앞에 https:// 를 붙여줘라 (붙여 주는 코드는 startswith)

            img_res = requests.get(images)
            with open('shoes_{}_{}.jpg'.format(pages, idx+1),"wb",) as f:
                f.write(img_res.content)


        print(name,re_price,re_code)

