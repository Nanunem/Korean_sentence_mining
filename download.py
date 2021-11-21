from audio import Audio
from text import Text


class Download:
    def __init__(self, demande):
        self.demande = demande

    def download(self,nombre_dialogue, correspondance, dates):
        prefixe_dialogue = "https://learn.dict.naver.com/dictPronunciation.dict?filePaths=/wordbook/mew/koreanconv/sentence/"
        prefixe_exemple = "https://learn.dict.naver.com/dictPronunciation.dict?filePaths=/wordbook/mew/koreanconv/study/"
        suffixe_exemple = "_study01_0"
        for num, item in enumerate(self.demande):
            item = item.upper()
            text = Text(dates[num])
            content = text.recherche_text()

            # Téléchargement de l'ensemble des dialogues et des exemples
            if "TOUT" in item:
                for i in range(1, int(nombre_dialogue[num])+1):
                    audio = Audio(f"{prefixe_dialogue}{correspondance[num]}_0{str(i)}.mp3")
                    audio.recherche_audio(f"dialogue_{dates[num]}_{str(i)}")
                    with open(f"dialogue_{i}_{dates[num]}.txt", "w", encoding="utf-8") as fich_sortie :
                        fich_sortie.write(str(content['sentences'][num]['sentence']))

                for i in range(1, 4):
                    audio = Audio(f"{prefixe_exemple}{correspondance[num]}{suffixe_exemple}{str(i)}.mp3")
                    audio.recherche_audio(f"exemple_{dates[num]}_{str(i)}")
                    with open(f"exemple_{i}_{dates[num]}.txt", "w", encoding="utf-8") as fich_sortie:
                        fich_sortie.write(content['studys'][0]['translation'])
                        fich_sortie.write("\n")
                        fich_sortie.write(content['studys'][0]['examples'][num]['example'])

            elif "DIAL" in item:
                # Téléchargement des dialogues (tous les dialogues ou certaines phrases)
                for i in range(1, int(nombre_dialogue[num])+1):
                    audio = Audio(f"{prefixe_dialogue}{correspondance[num]}_0{str(i)}.mp3")
                    audio.recherche_audio(f"dialogue_{dates[num]}_{str(i)}")
                    with open(f"dialogue_{i}_{dates[num]}.txt", "w", encoding="utf-8") as fich_sortie :
                        fich_sortie.write(content['sentences'][num]['sentence'])

            elif "EXEM" in item:
                # Téléchargement des exemples (tous les exemples ou certaines phrases)
                for i in range(1, 4):
                    audio = Audio(f"{prefixe_exemple}{correspondance[num]}{suffixe_exemple}{str(i)}.mp3")
                    audio.recherche_audio(f"exemple_{dates[num]}_{str(i)}")
                    with open(f"exemple_{i}_{dates[num]}.txt", "w", encoding="utf-8") as fich_sortie:
                        fich_sortie.write(content['studys'][0]['translation'])
                        fich_sortie.write("\n")
                        fich_sortie.write(content['studys'][0]['examples'][num]['example'])

            else:
                print("Erreur, merci d'indiquer \"TOUT\", \"DIALogue\" ou \"EXEMple\"")