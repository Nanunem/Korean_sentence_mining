import requests

prefixe_dialogue = "https://learn.dict.naver.com/dictPronunciation.dict?filePaths=/wordbook/mew/koreanconv/sentence/"
prefixe_exemple = "https://learn.dict.naver.com/dictPronunciation.dict?filePaths=/wordbook/mew/koreanconv/study/"
suffixe_exemple = "_study01_"


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
    Téléchargement de l'ensemble des dialogues et exemples,
    des certains dialogues ou certains exemples selon le choix
    de l'utilisateur
    """
    def __init__(self, demande):
        self.demande = demande

    def download(self,nombre_dialogue, correspondance, dates):
        for num, item in enumerate(self.demande):
            item = item.upper()
            # Téléchargement de l'ensemble des dialogues et des exemples
            if "TOUT" in item:
                for i in range(1, int(nombre_dialogue[num])+1):
                    audio = Audio(f"{prefixe_dialogue}{correspondance[num]}_0{str(i)}.mp3")
                    audio.recherche_audio(f"dialogue_{dates[num]}_{str(i)}")

                for i in range(1, 4):
                    audio = Audio(f"{prefixe_exemple}{correspondance[num]}_study01_0{str(i)}.mp3")
                    audio.recherche_audio(f"exemple_{dates[num]}_{str(i)}")

            elif "DIAL" in item:
                # Téléchargement des dialogues (tous les dialogues ou certaines phrases)
                for i in range(1, int(nombre_dialogue[num])+1):
                    audio = Audio(f"{prefixe_dialogue}{correspondance[num]}_0{str(i)}.mp3")
                    audio.recherche_audio(f"dialogue_{dates[num]}_{str(i)}")

            elif "EXEM" in item:
                # Téléchargement des exemples (tous les exemples ou certaines phrases)
                for i in range(1, 4):
                    audio = Audio(f"{prefixe_exemple}{correspondance[num]}_study01_0{str(i)}.mp3")
                    audio.recherche_audio(f"exemple_{dates[num]}_{str(i)}")

            else:
                print("Erreur, merci d'indiquer \"TOUT\", \"DIALogue\" ou \"EXEMple\"")
                pass
        return