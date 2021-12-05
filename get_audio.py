import requests

class Audio:
    """
    Download and save the audio of a specific date
    """
    prefixe = "https://learn.dict.naver.com/dictPronunciation.dict?filePaths="
    def __init__(self, url_audio):
        self.url_audio = url_audio

    def recherche_audio(self, nom_sortie):
        url_source = self.prefixe+self.url_audio
        content_source = requests.get(url_source).json()
        url_mp3 = content_source['url'][0]
        mp3 = requests.get(url_mp3)
        with open(nom_sortie + ".mp3", 'wb') as Entree:
            Entree.write(mp3.content)
