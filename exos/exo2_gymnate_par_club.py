# ecrire nombre total de gymnastes
def nombre_total_gymnaste():
    resultat = 0
    # a toi
    return resultat

# ecrire nombre total de gymnastes dans le departement dpt
def nombre_gymnaste_par_department(dpt):
    resultat = 0
    # a toi
    return resultat


# renvoi le nom du club avec le plus de gymnastes
def club_avec_le_plus_de_gymnaste():
    club = ''
    # a toi
    # aide: pour calcul un max tu peux commencer avec une valeur bidon comme -1 et après tu compares...
    return club

# ecrire nombre total de gymnastes dans le departement dpt
def nombre_moyen_de_gymnaste_par_club():
    resultat = 0
    # a toi. 2 approches: tu réutilises les methodes et cela tu peux faire le calcul en 1 ligne ou tu refais le tout..
    return resultat

# liste de clube. "gymnastes" est le nombre de gymnaste par club
# on suppose que le nom du club est unique
clubs = [
    {"nom": "albens", "departement": '73', "gymnastes": 5},
    {"nom": "aix-les-bains", "departement": '73', "gymnastes": 50},
    {"nom": "rumilly", "departement": '74', "gymnastes": 20},
    {"nom": "lyon", "departement": '69', "gymnastes": 120},

]

# Partie 1
output = nombre_total_gymnaste()
print("nombre total de gymnastes (doit etre 195): " + str(output))

# Partie 2
output = nombre_gymnaste_par_department('73')
print("nombre total de gymnastes en 73 ( doit etre 55): " + str(output))

# Partie 3
output = nombre_gymnaste_par_department('69')
print("nombre total de gymnastes en 69 ( doit etre 120): " + str(output))

# Partie 4
output = club_avec_le_plus_de_gymnaste()
print("Club avec le plus de gymnastes ( doit etre lyon): " + output)

# Partie 4
output = nombre_moyen_de_gymnaste_par_club()
print("nombre moyen de gymaste par club ( doit renvoyer 48.75): " + str(output))
