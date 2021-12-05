from get_audio import Audio
from get_content import Text


class Download:
    def __init__(self, demande):
        self.demande = demande

    def download(self, dates):
        for num, item in enumerate(self.demande):
            print(f"Fichiers du {dates[num]} en cours de récupération")
            item = item.upper()
            text = Text(dates[num])
            content = text.recherche_text()
            folder_path = "files_created"

            # Téléchargement de l'ensemble des dialogues et des exemples
            if "TOUT" in item.upper():
                print(f"Téléchargement des dialogues et des exemples")
                nb_dialogue = len(content['sentences'])
                for i in range(1, nb_dialogue+1):
                    audio = Audio(content['sentences'][i-1]['sentence_pron_file'])
                    audio.recherche_audio(f"{folder_path}/dialogue_{dates[num]}_{str(i)}")
                    with open(f"{folder_path}/dialogue_{dates[num]}_{str(i)}.txt", "w", encoding="utf-8") as fich_sortie :
                        fich_sortie.write(str(content['sentences'][i-1]['sentence']))

                for i in range(1, 4):
                    audio = Audio(content['studys'][0]['examples'][i-1]['pron_file_url'])
                    audio.recherche_audio(f"{folder_path}/exemple_{dates[num]}_{str(i)}")
                    with open(f"{folder_path}/exemple_{dates[num]}_{str(i)}.txt", "w", encoding="utf-8") as fich_sortie:
                        fich_sortie.write(content['studys'][0]['title'])
                        fich_sortie.write("\n")
                        fich_sortie.write(content['studys'][0]['translation'])
                        fich_sortie.write("\n")
                        fich_sortie.write(content['studys'][0]['examples'][i-1]['example'])

            elif "DIAL" in item.upper():
                print(f"Téléchargement des dialogues uniquement")
                # Téléchargement des dialogues (tous les dialogues ou certaines phrases)
                nb_dialogue = len(content['sentences'])
                for i in range(1, nb_dialogue+1):
                    audio = Audio(content['sentences'][i-1]['sentence_pron_file'])
                    audio.recherche_audio(f"{folder_path}/dialogue_{dates[num]}_{str(i)}")
                    with open(f"{folder_path}/dialogue_{dates[num]}_{str(i)}.txt", "w", encoding="utf-8") as fich_sortie :
                        fich_sortie.write(content['sentences'][i-1]['sentence'])

            elif "EXEM" in item.upper():
                print(f"Téléchargement des exemples uniquement")
                # Téléchargement des exemples (tous les exemples ou certaines phrases)
                for i in range(1, 4):
                    audio = Audio(content['studys'][0]['examples'][i-1]['pron_file_url'])
                    audio.recherche_audio(f"{folder_path}/exemple_{dates[num]}_{str(i)}")
                    with open(f"{folder_path}/exemple_{dates[num]}_{str(i)}.txt", "w", encoding="utf-8") as fich_sortie:
                        fich_sortie.write(content['studys'][0]['title'])
                        fich_sortie.write("\n")
                        fich_sortie.write(content['studys'][0]['translation'])
                        fich_sortie.write("\n")
                        fich_sortie.write(content['studys'][0]['examples'][i-1]['example'])

            else:
                print("Erreur, merci d'indiquer \"TOUT\", \"DIALogue\" ou \"EXEMple\"")