from create_file import Download
from parameters_reading import LectureFichier

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