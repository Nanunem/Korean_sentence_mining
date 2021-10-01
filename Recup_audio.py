from datetime import date
import requests

prefixe_dialogue = "https://learn.dict.naver.com/dictPronunciation.dict?filePaths=/wordbook/mew/koreanconv/sentence/"

prefixe_exemple = "https://learn.dict.naver.com/dictPronunciation.dict?filePaths=/wordbook/mew/koreanconv/study/"
suffixe_exemple = "_study01_"

ref_correspondance = "0574"
ref_date= "2021-09-30"

def dates_a_traiter(fichier) :
    correspondance = []
    date_ref = ref_date.split("-")
    with open(fichier,"r") as Entree:
        for ligne in Entree :
            ligne = ligne.strip()
            ligne = ligne.split("-")
            date1 = date(int(ligne[0]),int(ligne[1]),int(ligne[2]))
            date2 = date(int(date_ref[0]), int(date_ref[1]), int(date_ref[2]))
            diff = (date1 - date2).days
            num_date = int(ref_correspondance) + diff
            correspondance.append("0" + str(num_date))
    return correspondance


def recherche_audio(nom,url_ko) :
    lignes = requests.get(url_ko)
    lignes = lignes.text
    lignes = lignes.split("\"")
    url_audio = lignes[-2]

    audio = requests.get(url_audio)
    with open(nom + ".mp3", 'wb') as Entree:
        Entree.write(audio.content)

correspondance = dates_a_traiter("semaine.txt")
#recherche_audio("test","https://learn.dict.naver.com/dictPronunciation.dict?filePaths=/wordbook/mew/koreanconv/sentence/0574_05.mp3")
#with open(aujourd+".txt","w") :