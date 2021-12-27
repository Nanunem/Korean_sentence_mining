import os
import datetime
from create_file import Download
from parameters_reading import ReadingParamFile
from card_creation import Card, Deck

# Reading the file week.txt containing the days to consider
date_file = ReadingParamFile("week.txt")
dates, choice = date_file.reading()

# Listing the days requested by the user
print("The days considered are :")
for item in dates:
    print(f"{item}")
print("\nPlease update the \"week.txt\" file if needed\n")


# Choice of downloading both conversation and examples, only the dialogues or only the examples
action = Download(user_request=choice)
action.download(dates)

print("\nDownload done")

semaine_demandee = datetime.datetime.strptime(dates[0], '%Y-%m-%d')
year, week_num, day_of_week = semaine_demandee.isocalendar()
chemin = "files_created"
chemin_deck = "decks_created"

print("\nCreation of the deck")
for fichier in os.listdir(chemin):
    if fichier.endswith(".txt"):
        nom = fichier.removesuffix(".txt")
        card = Card(nom + ".mp3", nom + ".txt")
        card_created = card.card_creation()
        deck = Deck(f"{chemin_deck}/deck_year_{year}_week_{week_num}.txt")
        deck.create_deck(card_created)
print(f"\nDeck deck_year_{year}_week_{week_num}.txt created")