from datetime import date
import requests

prefixe_dialogue = "https://learn.dict.naver.com/dictPronunciation.dict?filePaths=/wordbook/mew/koreanconv/sentence/"

prefixe_exemple = "https://learn.dict.naver.com/dictPronunciation.dict?filePaths=/wordbook/mew/koreanconv/study/"
suffixe_exemple = "_study01_"


class DateMining:
    """
    Object the defines the date containing the audio and text of the Naver lesson
    """
    def __init__(self, day_mining):
        self.day_mining = day_mining

    def dates_to_consider(self):
        correspondance = []
        dates_demande = []
        ref_correspondance = "0574"
        ref_date = "2021-09-30"
        date_ref = ref_date.split("-")
        with open(self.day_mining, "r") as Entree:
            for ligne in Entree:
                ligne = ligne.strip()
                dates_demande.append(ligne)
                ligne = ligne.split("-")
                date1 = date(int(ligne[0]), int(ligne[1]), int(ligne[2]))
                date2 = date(int(date_ref[0]), int(date_ref[1]), int(date_ref[2]))
                diff = (date1 - date2).days
                num_date = int(ref_correspondance) + diff
                correspondance.append("0" + str(num_date))
        return correspondance, dates_demande


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

    def download(self):
        self.demande = self.demande.upper()

        if "TOUT" in self.demande:                         # téléchargement de l'ensemble des dialogues et des exemples
            for num, item in enumerate(correspondance):
                for i in range(1, 7):
                    audio = Audio(f"{prefixe_dialogue}{item}_0{str(i)}.mp3")
                    audio.recherche_audio(f"dialogue_{dates_demande[num]}_{str(i)}")
                for i in range(1, 4):
                    audio = Audio(f"{prefixe_exemple}{item}_study01_0{str(i)}.mp3")
                    audio.recherche_audio(f"exemple__{dates_demande[num]}_{str(i)}")

        elif "DIAL" in self.demande:            # téléchargement des dialogues (tous les dialogues ou certaines phrases)
            demande_precision = input("tout les dialogue ou quelques lignes (1 à 6) ? Indiquer \"TOUT\" ou une liste de chiffres")
            if demande_precision == "TOUT":
                for num, item in enumerate(correspondance):
                    for i in range(1, 7):
                        audio = Audio(f"{prefixe_dialogue}{item}_0{str(i)}.mp3")
                        audio.recherche_audio(f"dialogue_{dates_demande[num]}_{str(i)}")
            elif "1" in demande_precision or "2" in demande_precision or "3" in demande_precision or "4" in demande_precision or "5" in demande_precision or "6" in demande_precision:
                pass
            else:
                print("Erreur, merci d'indiquer \"TOUT\" ou une liste de chiffres")

        elif "EXEM" in self.demande:              # téléchargement des exemples (tous les exemples ou certaines phrases)
            pass

        else:
            print("Erreur, merci d'indiquer \"TOUT\", \"DIALogue\" ou \"EXEMple\"")
            pass
        return


# Lecture du fichier semaine.txt définissant les dates à traiter
fichier_dates = DateMining("semaine.txt")
correspondance, dates_demande = fichier_dates.dates_to_consider()

# Indication à l'utilisateur des dates traitées
print("Les dates traitées sont :\n")
for item in dates_demande:
    print(f"{item}\n")
print("Modifiez le fichier \"semaine.txt\" si d'autres dates sont à traitées")

# Choix des téléchargements à effectuer
choix = ChoixAction(demande=input("Que télécharger ? \"TOUT\", \"DIALogue\" ou \"EXEMple\" "))
choix.download()