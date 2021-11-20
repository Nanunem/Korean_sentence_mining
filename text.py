
import requests

class Text:
    prefixe_url = "https://gateway.dict.naver.com/krdict/kr/koen/today/"
    sufixe_url = "/conversation.dict"

    def __init__(self, date):
        self.date = date

    def recherche_text(self):
        date_url = self.date.replace("-", "")
        url = f"{self.prefixe_url}{date_url}{self.sufixe_url}"
        content = requests.get(url).json()
        return content["data"]



