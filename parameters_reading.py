from datetime import date


class LectureFichier:
    """
    Object reads the file semaine.txt to get the date,
    choice of download and number of lines of dialogue
    """
    def __init__(self, day_mining):
        self.day_mining = day_mining

    def lecture(self):
        choix = []
        dates_demande = []

        with open(self.day_mining, "r") as Entree:
            for ligne in Entree:
                if "#" not in ligne :
                    ligne = ligne.strip()
                    ligne = ligne.split()
                    dates_demande.append(ligne[0].strip())
                    choix.append(ligne[-1].strip())
        return dates_demande, choix