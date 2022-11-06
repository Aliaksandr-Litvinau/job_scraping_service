import codecs

import requests
from bs4 import BeautifulSoup as BS

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/102.0.5005.61/63 Safari/537.36"
}

domain = "https://www.work.ua/"
url = "https://www.work.ua/jobs-python/"
response = requests.get(url, headers=headers)

jobs = []
errors = []

if response.status_code == 200:
    soup = BS(response.content, "html.parser")
    main_div = soup.find('div', id='pjax-job-list')
    if main_div:
        div_lst = main_div.find_all('div', attrs={'class': 'job-link'})
        for div in div_lst:
            title = div.find('h2')
            href = title.a['href']
            content = div.p.text
            company = 'No name'
            logo = div.find('img')
            if logo:
                company = logo['alt']
            jobs.append(
                {
                    'url': domain + href,
                    'title': title.text,
                    'company': company,
                    'description': content,
                }
            )
    else:
        errors.append({"url": url, "title": "Div doesn't exists'"})
else:
    errors.append({"url": url, "title": "This page don't response'"})

with codecs.open("work.json", "w", "utf-8") as handler:
    handler.write(str(jobs))
