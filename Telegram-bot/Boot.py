import requests 
from bs4 import BeautifulSoup as bs 
import telegram
from apscheduler.schedulers.blocking import BlockingScheduler

token = "나의 텔레그램 토큰" # 내 텔레그램 토큰 
bot = telegram.Bot(token=token) # 변수명  bot 안에다가 내 토근 입력
sched = BlockingScheduler()

old_links = [] # 이미 보낸 링크를 집어 넣을 변수 
def extrct_links(old_links=[]):

    url = "https://m.search.naver.com/search.naver?where=m_news&sm=mtb_jum&query=%EC%BD%94%EB%A1%9C%EB%82%98"
    re = requests.get(url)
    html = re.text 
    soup = bs(html, "html.parser")
    search_result = soup.select_one("#news_result_list")
    news_list = search_result.select(".bx > .news_wrap > a")


    links = []
    for news in news_list[:5]:
        link = news['href']
        links.append(link)


    new_links = []
    for link in links:
        if link not in old_links:
            new_links.append(link)
    return new_links        


def send_links():
    global old_links
    new_links = extrct_links(old_links)
    if new_links:
        for link in new_links:
            bot.sendMessage(chat_id= "아이디 넘버", text=link)
    else:
        bot.sendMessage(chat_id= "아이디 넘버", text="No new news")
    old_links += new_links.copy()
    old_links = list(set(old_links))


send_links()
sched.add_job(send_links, 'interval', hours=1)
sched.start()



