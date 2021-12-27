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


