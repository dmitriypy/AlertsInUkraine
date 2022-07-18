import requests


class AlertsAPI:
    def __init__(self, key, id_=None):
        self.key: str = key
        self.id: int = id_
        self.url: str = "https://alerts.com.ua/api/"

    def get_alert(self):
        """Request to API for get info about alerts."""
        if self.id is None:
            r = requests.get(self.url + "states", headers={"X-API-Key": self.key})
        else:
            r = requests.get(f"{self.url + 'states/' + str(self.id)}", headers={"X-API-Key": self.key})
        return r.json()
    
    def alerts_history(self):
        r = requests.get(self.url + "history", headers={"X-API-Key": self.key})
        return r.json()
