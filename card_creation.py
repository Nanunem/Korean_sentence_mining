import os
import datetime

class Card:
    """
    Create the card using the txt file and audio file extracted
    """
    def __init__(self, audio_file_name, text_file_name):
        self.audio_file_name = audio_file_name
        self.text_file_name = text_file_name

    def card_creation(self):
        audio_field = "[sound:" + self.audio_file_name + "]"
        word_definition_field = ""
        grammar_point_title_field = ""
        grammar_point_field = ""
        image_field = ""

        folder_path = "files_created/"

        with open(folder_path + self.text_file_name, "r", encoding="utf8") as Input:
            content = Input.readlines()
            if "dialogue" in self.text_file_name:
                transcript_field = content[0].strip()
            else :
                transcript_field = content[2].strip()
                grammar_point_title_field = content[0].strip()
                grammar_point_field = content[1].strip()

        card = audio_field+"\t"+transcript_field+"\t"+audio_field+"\t"+word_definition_field+"\t"\
                +grammar_point_title_field+"\t"+grammar_point_field+"\t"+image_field
        return card

class Deck:
    """
    Create of the anki deck using the cards
    """
    def __init__(self, deck_name):
        self.deck_name = deck_name

    def create_deck(self, card):
        with open(self.deck_name, "a", encoding="utf8") as DeckFile :
            DeckFile.write(card + "\n")

def check_deck_folder():
    deck_folder_path = "decks_created"
    if os.path.isdir(deck_folder_path):
        pass
    else:
        os.mkdir(deck_folder_path)

def creation(user_answer, first_date_listed):
    user_answer = user_answer.upper()

    if "NO" in user_answer:
        print("Anki deck not created")
    elif "YES" in user_answer:
        check_deck_folder()
        week_of_first_date_request = datetime.datetime.strptime(first_date_listed, '%Y-%m-%d')
        year, week_num, day_of_week = week_of_first_date_request.isocalendar()
        files_downloaded_folder_path = "files_created"
        deck_folder_path = "decks_created"

        print("\nCreation of the deck")
        for fichier in os.listdir(files_downloaded_folder_path):
            if fichier.endswith(".txt"):
                nom = fichier.removesuffix(".txt")
                card = Card(nom + ".mp3", nom + ".txt")
                card_created = card.card_creation()
                deck = Deck(f"{deck_folder_path}/deck_year_{year}_week_{week_num}.txt")
                deck.create_deck(card_created)
        print(f"\nDeck deck_year_{year}_week_{week_num}.txt created")
    else :
        print("Anki deck not created, please put YES in the parameters file if you want to create the deck")