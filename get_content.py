import requests

class Text:
    """
    Creation of the text files with the dialogue, sample sentences and grammar points
    """
    url_prefix = "https://gateway.dict.naver.com/krdict/kr/koen/today/"
    url_suffix = "/conversation.dict"

    def __init__(self, date):
        self.date = date

    def text_search(self):
        date_url = self.date.replace("-", "")
        url = f"{self.url_prefix}{date_url}{self.url_suffix}"
        content = requests.get(url).json()
        return content["data"]



