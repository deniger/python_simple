# un exo pour supprimer des ligne, entree dans une liste et un dictionnaire.

def supprime_club_dans_clubs(club_nom):
    # supprime le club  club_nom du tableau club
    print("supprime club_nom de club. s'il n'existe pas ne fait rien")

def supprime_club_dans_clubs_dico(club_nom):
    # supprime le club  club_nom du dictionnaire club_dico
    print("supprime club_nom de clubs_dico. s'il n'existe pas ne fait rien")

def supprime_club_avec_dpt_dans_club(dpt):
    # supprime les clubs  des dpt
    print("supprime dans club tous les clubs du dpt")

def supprime_club_avec_dpt_dans_clubs_dico(club_nom):
    # supprime le club  du dpt du dictionnaire club_dico
    print("supprime dans club_dico tous les clubs du dpt")

# liste de clube. "gymnastes" est le nombre de gymnastes par club
# on suppose que le nom du club est unique
clubs = [
    {"nom": "albens", "departement": '73', "gymnastes": 5},
    {"nom": "aix-les-bains", "departement": '73', "gymnastes": 50},
    {"nom": "rumilly", "departement": '74', "gymnastes": 20},
    {"nom": "alby", "departement": '74', "gymnastes": 1},
    {"nom": "lyon", "departement": '69', "gymnastes": 120},
    {"nom": "lyon 2", "departement": '69', "gymnastes": 30}
]

# pour te montrer l'intérêt d'un dictionnaire dans cette exercice.
# en fait j'utilise un dico avec comme clé le nom du club et un dictionnaire comme valeur
clubs_dico = {
    "albens": {"nom": "albens", "departement": '73', "gymnastes": 5},
    "aix-les-bains": {"nom": "aix-les-bains", "departement": '73', "gymnastes": 50},
    "rumilly": {"nom": "rumilly", "departement": '74', "gymnastes": 20},
    "lyon": {"nom": "lyon", "departement": '69', "gymnastes": 120},
}

# Partie 1:
# le club de rumilly arrete.
# on le supprime des clubs et clubs_dico
supprime_club_dans_clubs("aix-les-bains")
supprime_club_dans_clubs_dico("aix-les-bains")
print("après que aix-les-basin arrete")
print(clubs)
print(clubs_dico)

# Partie 2
supprime_club_avec_dpt_dans_club("69")
supprime_club_avec_dpt_dans_clubs_dico("69")
supprime_club_avec_dpt_dans_club("74")
supprime_club_avec_dpt_dans_clubs_dico("74")

print("il ne doit rester qu'albens :)")
print(clubs)
print(clubs_dico)
