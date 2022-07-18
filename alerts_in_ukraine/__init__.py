__version__ = "1.0"
import requests


class AlertsAPI:
    def __init__(self, key, id_):
        self.key: str = key
        self.url: str = f"https://alerts.com.ua/api/states/{id_}"

    def get_alert(self):
        """Request to API for get info about alerts."""
        r = requests.get(self.url, headers={"X-API-Key": self.key})
        return r.json()
