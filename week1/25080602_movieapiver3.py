import requests
import json

def handle_api_response(func):
    def wrapper(*args, **kwargs):
        response = func(*args, **kwargs)
        if response.status_code == 200:
            return response.json()
        else:
            print("Hata:", response.status_code)
            return None
    return wrapper

class theMovieDB:
    def __init__(self):
        self.api_url = "https://api.themoviedb.org/3/"
        self.api_key = "f395d2d10ddb21194fc8f88c6c052fe0"

    @handle_api_response
    def getPopulars(self):
        url = f"{self.api_url}movie/popular?api_key={self.api_key}&language=en-US&page=1"
        return requests.get(url)

    @handle_api_response
    def getNowPlaying(self):
        url = f"{self.api_url}movie/now_playing?api_key={self.api_key}&language=en-US&page=1"
        return requests.get(url)

    @handle_api_response
    def search(self, keyword):
        url = f"{self.api_url}search/movie?api_key={self.api_key}&query={keyword}&language=en-US&page=1"
        return requests.get(url)
