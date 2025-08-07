import requests
import json

class theMovieDB:
    def __init__(self):
        self.api_url = "https://api.themoviedb.org/3/"
        self.api_key = "f395d2d10ddb21194fc8f88c6c052fe0"

    def _get_json_response(self, endpoint):
        url = f"{self.api_url}{endpoint}?api_key={self.api_key}&language=en-US&page=1"
        response = requests.get(url)

        if response.status_code == 200:
            return response.json()
        else:
            print("Hata:", response.status_code)
            return None

    def getPopulars(self):
        return self._get_json_response("movie/popular")

    def getNowPlaying(self):
        return self._get_json_response("movie/now_playing")

    def search(self, keyword):
        # search endpointi farklı bir URL yapısında, ona özel
        url = f"{self.api_url}search/movie?api_key={self.api_key}&query={keyword}&language=en-US&page=1"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            print("Hata:", response.status_code)
            return None