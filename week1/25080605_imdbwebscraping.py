import requests
from bs4 import BeautifulSoup
#pip list
#beautifulsoup html,xml,json gibi verileri parse etmekte kullanılır
url = "https://www.imdb.com/chart/top/?ref_=chtmvm_nv_menu"

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"}

html = requests.get(url, headers=headers).content #ya da text
#print(html)
soup = BeautifulSoup(html, "html.parser")

liste = soup.find('ul', {'class':"ipc-metadata-list"}).find_all('li', limit=10)
for li in liste:
    moviename = li.find("h3", {"class": "ipc-title__text"}).text
    print(moviename, end=' -*- ')
    puan = li.find("span", {"class":"ipc-rating-star"}).text
    print(puan)