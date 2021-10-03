from selenium import webdriver
from time import sleep

url = 'https://www.gopax.co.kr/'

path = '/Users/dowon/Downloads/chromedriver'
driver = webdriver.Chrome(path)
driver.get(url)

f_tbody = driver.find_element_by_xpath('//*[@id="react"]/div/div[1]/div[2]/div[2]/div[2]/table/tbody')
f_table = f_tbody.find_elements_by_tag_name("tr")

for td in f_table:
    coin_row = td.text
    coin_row_list =  coin_row.split('/n')
    print(coin_row_list)
          

          





