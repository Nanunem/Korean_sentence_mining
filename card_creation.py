class Card:

    def __init__(self, nom_fichier_audio, nom_fichier_text):
        self.nom_fichier_audio = nom_fichier_audio
        self.nom_fichier_text = nom_fichier_text

    def crea_carte(self):
        champ_audio = "[sound:"+self.nom_fichier_audio+"]"
        champ_definition_mots = ""
        champ_titre_grammaire = ""
        champ_grammaire = ""
        champ_image = ""

        chemin = "files_created/"

        with open(chemin + self.nom_fichier_text,"r", encoding="utf8") as Entree:
            content = Entree.readlines()
            if "dialogue" in self.nom_fichier_text:
                champ_transcript = content[0].strip()
            else :
                champ_transcript = content[2].strip()
                champ_titre_grammaire = content[0].strip()
                champ_grammaire = content[1].strip()

        carte = champ_audio+"\t"+champ_transcript+"\t"+champ_audio+"\t"+champ_definition_mots+"\t"\
                +champ_titre_grammaire+"\t"+champ_grammaire+"\t"+champ_image
        return carte

class Deck:

    def __init__(self,nom_deck):
        self.nom_deck = nom_deck

    def create_deck(self,carte):
        with open(self.nom_deck, "a", encoding="utf8") as Sortie :
            Sortie.write(carte+"\n")

if __name__ == '__main__':
    import os
    chemin = "files_created"
    for fichier in os.listdir(chemin):
        if fichier.endswith(".txt"):
            nom = fichier.removesuffix(".txt")
            card = Card(nom+".mp3", nom+".txt")
            card_created = card.crea_carte()
            deck = Deck("test.txt")
            deck.create_deck(card_created)

