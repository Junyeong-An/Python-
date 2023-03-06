from bs4 import BeautifulSoup
from requests import get
import requests


def extract_jobs(term):
    url = f"https://remoteok.com/remote-{term}-jobs"
    request = requests.get(url, headers={"User-Agent": "Kimchi"})
    results = []
    if request.status_code == 200:
    
      print("good")

      soup = BeautifulSoup(request.text, "html.parser")
      
      jobs=soup.find_all('tr',class_="job")
      
      for job in jobs:
        
        company = job.find('h3',itemprop="name")
        position=job.find('h2',itemprop="title")
        location=job.find('div',class_="location")
        print(company,position,location)    
    # write your ✨magical✨ code here
    else:
         print("Can't get jobs. try again!")
    return results


extract_jobs("python")