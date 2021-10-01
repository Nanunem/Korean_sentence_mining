from datetime import date
import requests

prefixe_dialogue = "https://learn.dict.naver.com/dictPronunciation.dict?filePaths=/wordbook/mew/koreanconv/sentence/"

prefixe_exemple = "https://learn.dict.naver.com/dictPronunciation.dict?filePaths=/wordbook/mew/koreanconv/study/"
suffixe_exemple = "_study01_"

class Date_mining :

    def __init__(self, day_mining):
        self.day_mining = day_mining

    def dates_a_traiter(self) :
        correspondance = []
        ref_correspondance = "0574"
        ref_date = "2021-09-30"
        date_ref = ref_date.split("-")
        with open(self.day_mining,"r") as Entree:
            for ligne in Entree :
                ligne = ligne.strip()
                ligne = ligne.split("-")
                date1 = date(int(ligne[0]),int(ligne[1]),int(ligne[2]))
                date2 = date(int(date_ref[0]), int(date_ref[1]), int(date_ref[2]))
                diff = (date1 - date2).days
                num_date = int(ref_correspondance) + diff
                correspondance.append("0" + str(num_date))
        return correspondance

class Audio :

    def __init__(self, url_audio):
        self.url_audio = url_audio

    def recherche_audio(self, nom_sortie) :
        lignes = requests.get(self.url_audio)
        lignes = lignes.text
        lignes = lignes.split("\"")
        url_mp3 = lignes[-2]
        mp3 = requests.get(url_mp3)
        with open(nom_sortie + ".mp3", 'wb') as Entree:
            Entree.write(mp3.content)
        return

fichier_dates = Date_mining("semaine.txt")
correspondance = fichier_dates.dates_a_traiter()

audio = Audio("https://learn.dict.naver.com/dictPronunciation.dict?filePaths=/wordbook/mew/koreanconv/sentence/0574_05.mp3")
audio.recherche_audio("test")