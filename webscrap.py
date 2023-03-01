from bs4 import BeautifulSoup
from requests import get


def extract_jobs(term):
  url = f"https://remoteok.com/remote-{term}-jobs"
  request = get(url)
  if request.status_code == 200:
    print("Can't get jobs.")

    # write your ✨magical✨ code here
  else:
    print("good")
    results = []
    soup = BeautifulSoup(request.text, "html.parser")
    job_body = soup.find("tbody")
    jobs_list = job_body.find_all("tr", class_="job")
    for job in jobs_list:
      div = job.find("td", class_="company position company_and_position")
      title = job.find("h2", itemprop="title")
      company = job.find("h3", itemprop="name")
      type = div.find_all("div", class_="location")
      location, money = type[0], type[1]
      job_data = {
        'position': title.string.replace('\n', ""),
        'company': company.string.replace('\n', ""),
        'money': money.string,
        'location': location.string
      }
      results.append(job_data)
      print(results)


extract_jobs("python")