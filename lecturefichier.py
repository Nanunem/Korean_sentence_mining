from datetime import date


class LectureFichier:
    """
    Object reads the file semaine.txt to get the date,
    choice of download and number of lines of dialogue
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
        ref_correspondance = "0577"
        ref_date = "2021-10-04"
        date_ref = ref_date.split("-")

        for item in dates:
            item = item.split("-")

            date1 = date(int(item[0]), int(item[1]), int(item[2]))
            date2 = date(int(date_ref[0]), int(date_ref[1]), int(date_ref[2]))
            diff = (date1 - date2).days

            # Pour enlever les dimanches sans dialogues
            diff_semaine = int(diff / 7)

            num_date = int(ref_correspondance) + diff - diff_semaine
            correspondance.append("0" + str(num_date))
        return correspondance