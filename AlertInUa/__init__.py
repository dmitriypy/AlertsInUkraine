__version__ = "1.0"
import requests
from enum import Enum


class AlertsAPI:
    def __init__(self, key, id_):
        self.key: str = key
        self.url: str = f"https://alerts.com.ua/api/states/{id_}"

    def get_alert(self):
        """Request to API for get info about alerts."""
        r = requests.get(self.url, headers={"X-API-Key": self.key})
        return r.json()

    def states(self):
        r = requests.get(
            "https://alerts.com.ua/api/states", headers={"X-API-Key": self.key}
        )
        return r.json()


class States(Enum):
    Vinnytsia = 1
    Volyn = 2
    Dnipropetrovsk = 3
    Donetsk = 4
    Zhytomyr = 5
    Zakarpattia = 6
    Zaporizhzhia = 7
    Ivano_Frankivsk = 8
    Kyiv = 9
    Kirovohrad = 10
    Luhansk = 11
    Lviv = 12
    Mykolaiv = 13
    Odesa = 14
    Poltava = 15
    Rivne = 16
    Sumy = 17
    Ternopil = 18
    Kharkiv = 19
    Kherson = 20
    Khmelnytskyi = 21
    Cherkasy = 22
    Chernivts = 23
    Chernihiv = 24
    Kyiv_city = 25
