def supprime_club_dans_clubs(club_nom):
    # supprime le club  club_nom du tableau club
    print("supprime club_nom de club. s'il n'existe pas ne fait rien")

def supprime_club_dans_clubs_dico(club_nom):
    # supprime le club  club_nom du dictionnaire club_dico
    print("supprime club_nom de clubs_dico. s'il n'existe pas ne fait rien")

# liste de clube. "gymnastes" est le nombre de gymnastes par club
# on suppose que le nom du club est unique
clubs = [
    {"nom": "albens", "departement": '73', "gymnastes": 5},
    {"nom": "aix-les-bains", "departement": '73', "gymnastes": 50},
    {"nom": "rumilly", "departement": '74', "gymnastes": 20},
    {"nom": "lyon", "departement": '69', "gymnastes": 120},
]

# pour te montrer l'intérêt d'un dictionnaire dans cette exercice.
# en fait j'utilise un dico avec comme clé le nom du club et un dictionnaire comme valeur
clubs_dico = {
    "albens": {"nom": "albens", "departement": '73', "gymnastes": 5},
    "aix-les-bains": {"nom": "aix-les-bains", "departement": '73', "gymnastes": 50},
    "rumilly": {"nom": "rumilly", "departement": '74', "gymnastes": 20},
    "lyon": {"nom": "lyon", "departement": '69', "gymnastes": 120},
}

# le club de rumilly arrete.
# on le supprime des clubs et clubs_dico
supprime_club_dans_clubs("rumilly")
supprime_club_dans_clubs_dico("rumilly")
print("après que rumilly arrete")
print(clubs)
print(clubs_dico)

supprime_club_dans_clubs("aix-les-bains")
supprime_club_dans_clubs_dico("aix-les-bains")
supprime_club_dans_clubs("lyon")
supprime_club_dans_clubs_dico("lyon")

print("il ne doit rester qu'albens :)")
print(clubs)
print(clubs_dico)
