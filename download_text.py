
import requests

class Text:
    prefixe_url = "https://gateway.dict.naver.com/krdict/kr/koen/today/"
    sufixe_url = "/conversation.dict"

    def __init__(self, demande):
        self.demande = demande

    def _recherche_audio(self, date):
        date_url = date.replace("-", "")
        url = f"{self.prefixe_url}{date_url}{self.sufixe_url}"
        print(url)
        content = requests.get(url).json()
        return content["data"]

    def download_text(self, nombre_dialogue, dates):
        for num, item in enumerate(self.demande):
            content = self._recherche_audio(dates[num])
            item = item.upper()
            # Téléchargement de l'ensemble des dialogues et des exemples
            if "TOUT" in item:
                for i in range(0, int(nombre_dialogue[num])):
                    with open(f"dialogue_{i+1}_{dates[num]}.txt", "w", encoding="utf-8") as fich_sortie :
                        fich_sortie.write(str(content['sentences'][num]['sentence']))

                for i in range(0, 3):
                    with open(f"exemple_{i + 1}_{dates[num]}.txt", "w", encoding="utf-8") as fich_sortie:
                        fich_sortie.write(content['studys'][0]['translation'])
                        fich_sortie.write("\n")
                        fich_sortie.write(content['studys'][0]['examples'][num]['example'])

            elif "DIAL" in item:
                # Téléchargement des dialogues (tous les dialogues ou certaines phrases)
                for i in range(0, int(nombre_dialogue[num])):
                    with open(f"dialogue_{i+1}_{dates[num]}.txt", "w", encoding="utf-8") as fich_sortie :
                        fich_sortie.write(content['sentences'][num]['sentence'])


            elif "EXEM" in item:
                # Téléchargement des exemples (tous les exemples ou certaines phrases)
                for i in range(0, 3):
                    with open(f"exemple_{i + 1}_{dates[num]}.txt", "w", encoding="utf-8") as fich_sortie:
                        fich_sortie.write(content['studys'][0]['translation'])
                        fich_sortie.write("\n")
                        fich_sortie.write(content['studys'][0]['examples'][num]['example'])


            else:
                print("Erreur, merci d'indiquer \"TOUT\", \"DIALogue\" ou \"EXEMple\"")
                pass
        return

if __name__=="__main__":
    text = Text(["TOUT"])
    text.download_text("2",["2021-11-15"])
