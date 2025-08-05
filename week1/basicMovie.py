#themoviedb.org => film dizi arşivi
#Anahtar kelimeye göre arma
#En popüler film listesi
#Vizyondaki film listesi

import requests
import json

class theMovieDB:
    def __init__(self):
        self.api_url = "https://api.themoviedb.org/3/"
        self.api_key = "f395d2d10ddb21194fc8f88c6c052fe0"

    #functionCode = ""

    def getPopulars(self):
        url = f"{self.api_url}movie/popular?api_key={self.api_key}&language=en-US&page=1"
        response = requests.get(url)

        if response.status_code == 200:
            return response.json()  # JSON veriyi döndür
        else:
            print("Hata:", response.status_code)
            return None
        
    def getNowPlaying(self):
        url = f"{self.api_url}movie/now_playing?api_key={self.api_key}&language=en-US&page=1"
        response = requests.get(url)

        if response.status_code == 200:
            return response.json()  # JSON veriyi döndür
        else:
            print("Hata:", response.status_code)
            return None

movieApi = theMovieDB()

while True:
    s = input("1-Popular movies\n2-Quit\n3-NowPlaying\n: ")
    if s == "2":
        break
    else:
        if s == "1":
            pageResults = movieApi.getPopulars()["results"]
            for m in pageResults:
                print(m["original_title"])
        elif s == "3":
            pageResults = movieApi.getNowPlaying()["results"]
            for m in pageResults:
                print(m["original_title"])
