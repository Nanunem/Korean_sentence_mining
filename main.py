from download import Download
from lecturefichier import LectureFichier

# Lecture du fichier semaine.txt définissant les dates à traiter
fichier_dates = LectureFichier("semaine.txt")
dates, choix, nombre_dialogue = fichier_dates.lecture()
correspondance = fichier_dates.dates_to_consider(dates)

# Indication à l'utilisateur des dates traitées
print("Les dates traitées sont :\n")
for item in dates:
    print(f"{item}\n")
print("Modifiez le fichier \"semaine.txt\" si d'autres dates sont à traitées")


# Choix des téléchargements à effectuer
action = Download(demande=choix)
action.download(nombre_dialogue, correspondance, dates)