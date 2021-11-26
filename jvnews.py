import requests
from bs4 import BeautifulSoup
import jarvis


toi_r = requests.get("https://timesofindia.indiatimes.com/briefs")
toi_soup = BeautifulSoup(toi_r.content, 'html.parser')

toi_headings = toi_soup.find_all('h2')

toi_headings = toi_headings[2:4]

toi_news = []

for th in toi_headings:
    toi_news.append(th.text)
for news in toi_news:
    # print(news)
    jarvis.speak(news)
