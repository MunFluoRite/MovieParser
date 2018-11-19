import requests
from bs4 import BeautifulSoup

def movie():
    url = "https://movie.naver.com/movie/sdb/rank/rmovie.nhn"
    html = requests.get(url).text
    soup = BeautifulSoup(html, "html.parser")
    tags = soup.find_all("div", {"class": "tit3"})

    for index, tag in enumerate(tags):
        tag.a.get_text()
        print(index + 1, tag.a.get_text())
movie()
