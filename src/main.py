import codecs

from scraping.parsers import *
from scraping.models import Vacancy, City, ProgrammingLanguage

parsers = (
    (work, "https://www.work.ua/ru/jobs/"),
    (dou, 'https://jobs.dou.ua/'),
    (djinni, 'https://djinni.co/jobs/'),
)
jobs, errors = [], []

for func, url in parsers:
    j, e = func(url)
    jobs += j
    errors += e

if __name__ == '__main__':
    with codecs.open("work.json", "w", "utf-8") as handler:
        handler.write(str(jobs))
