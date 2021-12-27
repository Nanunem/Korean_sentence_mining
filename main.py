import card_creation
from create_file import Download
from parameters_reading import ReadingParamFile

# Reading the file week.txt containing the days to consider
date_file = ReadingParamFile("week.txt")
dates, choice, create_deck_answer = date_file.reading()

# Listing the days requested by the user
print("The days considered are :")
for item in dates:
    print(f"{item}")
print("\nPlease update the \"week.txt\" file if needed\n")


# Choice of downloading both conversation and examples, only the dialogues or only the examples
action = Download(user_request=choice)
action.download(dates)

print("\nDownload done")

#Creation of the deck depending on the answer of the user
first_date_listed = dates[0]
card_creation.creation(create_deck_answer, first_date_listed)