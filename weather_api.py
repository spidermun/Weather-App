import json
import requests
import config


class Weather:
    def __init__(self):
        self.api_key = config.API_KEY
        self.base_url = config.BASE_URL

    def _build_params(self,city):
        params = {
            "q": city,
            "appid": self.api_key,
            "units": "metric",
            "lang": "pl"
        }
        return params

    def get_weather(self,city):
        params = self._build_params(city)
        response = requests.get(self.base_url,params=params)

        try:
            if response.status_code == 200:
                return response.json()

        except Exception:
            print(f"Blad, kod:{response.status_code}")
