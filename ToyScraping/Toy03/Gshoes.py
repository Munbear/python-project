from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from urllib.request import urlopen 
import urllib.request 
import time



path = '/Users/dowon/Downloads/chromedriver' #크롬 위치 경로 
driver = webdriver.Chrome(path)# 크롬 위치 경로 
url = ("https://shop.adidas.co.kr/PF020201.action?S_CTGR_CD=01002001&NFN_ST=Y") #url 주소
driver.get(url) # 창 열기 
driver.maximize_window() #창 최대화


elem = driver.find_element_by_class_name("link").click() #세부 목록창 클릭 

try:
    #로딩시간 기달린후 동작 수행 
    name = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH,"//*[@id='p_prod_bas']")))
    # 가격 값 가져오기 
    price = driver.find_element_by_xpath("//*[@id='ss_price']")
    # 제품 코드 가져오기 
    product_code = driver.find_element_by_xpath("//*[@id='contents_r']/div[3]/div[5]/div/table/tbody/tr[1]/td[1]")
    # 제품 이미지 가져오기 

    print(name.text, price.text, product_code.text) #값 텍스트 출력 
finally:
    driver.quit()




# name = driver.find_element_by_xpath("//*[@id='p_prod_bas']")
# print(name.text)