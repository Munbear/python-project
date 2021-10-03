import requests
from bs4 import BeautifulSoup

LIMIT = 1
URL = f"http://www.jobkorea.co.kr/recruit/joblist?menucode=search#anchorGICnt_{LIMIT}"


def get_max_page():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")
    pagination = soup.find("div", {"class": "tplPagination newVer"})
    links = pagination.find_all("a")
    pages = []
    for link in links[:-1]:
        pages.append(int(link.string))
    max_page = pages[-1]
    return max_page


def extract_job(html):
    title = html.find("div", {"class": "titBx"}).find("a").string
    company = html.find("td", {'class': 'tplCo'})
    if company:
      company_anchor = company.find("a")
      if company_anchor is not None:
        company = (company_anchor.string)
      else: 
        company = (company.string)
    else:
      company = None        
    job_id = html['data-info']
    return {'title': title, 'company': company,
    'link': f"http://www.jobkorea.co.kr/Recruit/GI_Read/{job_id}"}


def extract_jk_jobs(last_page):
    jobs = []
    for page in range(last_page):
      print(f"Scrapping page {page}")
      result = requests.get(f"{URL}anchorGICnt_{page+LIMIT}")
      soup = BeautifulSoup(result.text, "html.parser")
      results = soup.find_all("tr", {"class": "devloopArea"})
      for result in results:
          job = extract_job(result)
          jobs.append(job)
    return jobs


def jk_jobs_information():
  last_page = get_max_page()
  jk_jobs = extract_jk_jobs(last_page)
  return jk_jobs