import os
import datetime
from create_file import Download
from parameters_reading import LectureFichier
from card_creation import Card, Deck

# Lecture du fichier semaine.txt définissant les dates à traiter
fichier_dates = LectureFichier("semaine.txt")
dates, choix = fichier_dates.lecture()

# Indication à l'utilisateur des dates traitées
print("Les dates traitées sont :")
for item in dates:
    print(f"{item}")
print("\nModifiez le fichier \"semaine.txt\" si d'autres dates sont à traitées\n")


# Choix des téléchargements à effectuer
action = Download(demande=choix)
action.download(dates)

print(f"Téléchargement terminé")


aujour = datetime.date.today()
year, week_num, day_of_week = aujour.isocalendar()
chemin = "files_created"
chemin_deck = "decks_created"
for fichier in os.listdir(chemin):
    if fichier.endswith(".txt"):
        nom = fichier.removesuffix(".txt")
        card = Card(nom + ".mp3", nom + ".txt")
        card_created = card.crea_carte()
        deck = Deck(f"{chemin_deck}/deck_semaine_{week_num}.txt")
        deck.create_deck(card_created)