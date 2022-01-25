import requests as req
from bs4 import BeautifulSoup as bs

url="https://www.nytimes.com/live/2022/01/24/world/omicron-covid-vaccine-tests#us-officials-limit-approval-of-treatments-that-dont-work-on-omicron"

response = req.get(url, verify=False)
soup = bs(response.content, "html.parser")
title = soup.find("h1")
summary = soup.find("p")

print("The headline is " + title.text)
print("A quick summary is" + summary.text)
