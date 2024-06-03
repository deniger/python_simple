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


# liste de clube. "gymnastes" est le nombre de gymnaste par club
# on suppose que le nom du club est unique
clubs = [
    {"nom": "albens", "departement": '73', "gymnastes": 5},
    {"nom": "aix-les-bains", "departement": '73', "gymnastes": 50},
    {"nom": "rumilly", "departement": '74', "gymnastes": 20},
    {"nom": "lyon", "departement": '69', "gymnastes": 120},

]

output = nombre_total_gymnaste()
print("nombre total de gymnaste: " + str(output))
# doit renvoyer le nombre de gymnastes dans les 4 clubs soit 1995


output = nombre_gymnaste_par_department('73')
print("nombre total de gymnaste en 73 ( doit etre 55): " + str(output))  # doit renvoyer 55

output = nombre_gymnaste_par_department('69')
print("nombre total de gymnaste en 69 ( doit etre 120): " + str(output))  # doit renvoyer 120

output = club_avec_le_plus_de_gymnaste()
print("Club avec le plus de gymnaste ( doit etre lyon): " + output)  # doit renvoyer 120
