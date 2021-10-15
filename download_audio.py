from datetime import date

import requests

prefixe_dialogue = "https://learn.dict.naver.com/dictPronunciation.dict?filePaths=/wordbook/mew/koreanconv/sentence/"
prefixe_exemple = "https://learn.dict.naver.com/dictPronunciation.dict?filePaths=/wordbook/mew/koreanconv/study/"
suffixe_exemple = "_study01_"


class LectureFichier:
    """
    Object reads the file semaine.txt to get the date, choice of download and number of lines of dialogue
    """
    def __init__(self, day_mining):
        self.day_mining = day_mining

    def lecture(self):
        nb_dialogue = []
        choix = []
        dates_demande = []
        with open(self.day_mining, "r") as Entree:
            for ligne in Entree:
                if "#" in ligne :
                    pass
                else :
                    ligne = ligne.strip()
                    ligne = ligne.split()
                    dates_demande.append(ligne[0].strip())
                    choix.append(ligne[-1].strip())
                    nb_dialogue.append(ligne[1].strip())
        return dates_demande, choix, nb_dialogue

    def dates_to_consider(self,dates):
        correspondance = []
        ref_correspondance = "0574"
        ref_date = "2021-09-30"
        date_ref = ref_date.split("-")
        for item in dates:
            item = item.split("-")
            date1 = date(int(item[0]), int(item[1]), int(item[2]))
            date2 = date(int(date_ref[0]), int(date_ref[1]), int(date_ref[2]))
            diff = (date1 - date2).days
            num_date = int(ref_correspondance) + diff -1
            correspondance.append("0" + str(num_date))
        return correspondance


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
        return


class ChoixAction:
    """
    Téléchargement de l'ensemble des dialogues et exemples, des certains dialogues ou certains exemples selon le choix
    de l'utilisateur
    """
    def __init__(self, demande):
        self.demande = demande

    def download(self,nombre_dialogue, correspondance, dates):
        for num, item in enumerate(self.demande):
            item = item.upper()
            if "TOUT" in item:                         # téléchargement de l'ensemble des dialogues et des exemples
                for i in range(1, int(nombre_dialogue[num])+1):
                    audio = Audio(f"{prefixe_dialogue}{correspondance[num]}_0{str(i)}.mp3")
                    audio.recherche_audio(f"dialogue_{dates[num]}_{str(i)}")
                for i in range(1, 4):
                    audio = Audio(f"{prefixe_exemple}{correspondance[num]}_study01_0{str(i)}.mp3")
                    audio.recherche_audio(f"exemple_{dates[num]}_{str(i)}")

            elif "DIAL" in item:            # téléchargement des dialogues (tous les dialogues ou certaines phrases)
                for i in range(1, int(nombre_dialogue[num])+1):
                    audio = Audio(f"{prefixe_dialogue}{correspondance[num]}_0{str(i)}.mp3")
                    audio.recherche_audio(f"dialogue_{dates[num]}_{str(i)}")

            elif "EXEM" in item:              # téléchargement des exemples (tous les exemples ou certaines phrases)
                for i in range(1, 4):
                    audio = Audio(f"{prefixe_exemple}{correspondance[num]}_study01_0{str(i)}.mp3")
                    audio.recherche_audio(f"exemple_{dates[num]}_{str(i)}")

            else:
                print("Erreur, merci d'indiquer \"TOUT\", \"DIALogue\" ou \"EXEMple\"")
                pass
        return