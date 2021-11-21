import requests

class Audio:
    """
    Download and save the audio of a specific date
    """
    def __init__(self, url_audio):
        self.url_audio = url_audio

    def recherche_audio(self, nom_sortie):
        lignes = requests.get(self.url_audio)
        lignes = lignes.text
        lignes = lignes.split("\"")
        url_mp3 = lignes[-2]

        mp3 = requests.get(url_mp3)
        with open(nom_sortie + ".mp3", 'wb') as Entree:
            Entree.write(mp3.content)
