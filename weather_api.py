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

        try:
            response = requests.get(self.base_url, params=params)

            if response.status_code == 200:
                return response.json()
            else:
                print(f"Nie udało się pobrać danych. Kod błędu: {response.status_code}")
                return None
        except requests.exceptions.RequestException:
            print("Blad polaczenia")
            return None