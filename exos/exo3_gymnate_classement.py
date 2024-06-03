# texte vient d'un journal et est du styple "club_premier club_deuxieme club_troisieme".
# les noms des clubs sont séparés par des espaces
# tu dois renvoyer une chaine avec:
# 1- nom du club premier (departement du club)
# 2- nom du club deuxieme (departement du club)
# etc...
# ici tu utilises la variables clubs
def classement(texte):
    resultat = ''
    # A toi. supprime ces 3 lignes qui donnent juste une info pour séparer par un retour chariot
    # utilse le tableau clubs. Tu devras surement faire une methode pour récuperer le club avec un nom donné
    resultat = "1. club premier (73)"
    resultat = resultat + "\n" + "2. club deuxieme (74)"
    resultat = resultat + "\n" + "3. club troisieme (69)"

    return resultat

# ici tu utilises la variables clubs_dico
def classement_avec_dico(texte):
    resultat = ''
    # ici tu utilises le dictionnaire clubs_dico au lieu de club.
    # Tu verras ce sera plus simple :) C'est pour illustrer l'intéret d'un dictionnaire ( au delà des perfs)
    # a toi
    return resultat


def nombre_de_gymnaste_total_avec_dico():
    nombre=0
    # exercice déjà fait mais utilise ici clubs_dico
    # c'est juste pour que tu itères sur les valeurs d'un dictionnaire.
    # a toi
    return nombre

# tansforme liste de clubs soit la variable clubs en dictionnaire identique a club_disco
def renvoie_tableau_transforme_en_dictionnaire():
    resultat=  {}
    # a toi
    return resultat


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

# Partie 1
output = classement("albens rumilly lyon")
print("le classement est (doit renvoyer 1. Albens,...): ")
print(output)

# Partie 2
output = classement_avec_dico("albens rumilly lyon")
print("le classement avec les dico est (doit renvoyer 1. Albens,...): ")
print(output)

# Partie 3. Juste pour que itères sur les valeurs d'un dictionnaire.
output = nombre_de_gymnaste_total_avec_dico()
print("nombre total de gymnaste (doit etre 195): " + str(output))

# Partie 4
output = renvoie_tableau_transforme_en_dictionnaire()
print("dictionnaire des clubs rangés par nom du club: " + str(output))
print("doit etre le meme dico que : " + str(clubs_dico))
