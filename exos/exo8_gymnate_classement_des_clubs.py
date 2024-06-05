# peut etre compliqué car bcp d étapes
# doit renvoyer un tableau des nom de clubs dans l'ordre du nombre de gymnaste du plus grand au plus petit
# pour faire simple dans un premier temps, on dit que le nombre de gymnastes est unique  (pas 2 clubs avec le meme nombre de gymnastes)
# dans un second temps on fera le cas plus complique
# dans notre cas doit renvoyer "lyon","aix-les-bains","rumilly","albens"
def club_par_nombre_de_gymnastes():
    # utilise le dico clubs
    resultat = []

    # aide: il faudra surement que tu créé des structures intermédaires.
    # En fait, si tu te dis: je dois "classer" les clubs par qqchose, il faut faire dico avec ce qqchose comme cle
    
    # Info: comment trier une liste:
    # tu peux utiliser la méthode sorted.
    # Exemples
    # numbers = [5,6, 9, 3, 1]
    # numbers_sorted=sorted(numbers, reverse=True)
    # print(numbers_sorted)
    # va donner [9, 6, 5, 3, 1]
    
    # A toi.

    return resultat

# si 2 clubs ont le meme nombre de gymnaste leurs noms seront concatene avec le separateur ;
def club_par_nombre_de_gymnastes_complexe():
    # utilise le dico clubs_complique
    resultat = []
    # dans la structure temporaire dico, tu auras surement des valeurs qui seront des listes...


    # A toi.

    return resultat


# liste de clube. "gymnastes" est le nombre de gymnastes par club
# on suppose que le nom du club est unique
clubs = [
    {"nom": "albens", "departement": '73', "gymnastes": 5},
    {"nom": "aix-les-bains", "departement": '73', "gymnastes": 50},
    {"nom": "rumilly", "departement": '74', "gymnastes": 20},
    {"nom": "lyon", "departement": '69', "gymnastes": 120},
]

clubs_complique = [
    {"nom": "albens", "departement": '73', "gymnastes": 5},
    {"nom": "aix-les-bains", "departement": '73', "gymnastes": 50},
    {"nom": "rumilly", "departement": '74', "gymnastes": 20},
    {"nom": "annecy", "departement": '74', "gymnastes": 20},
    {"nom": "lyon", "departement": '69', "gymnastes": 120},
    {"nom": "villeurbanne", "departement": '69', "gymnastes": 120},
]


# Partie 1
output = club_par_nombre_de_gymnastes()
print("doit renvoyer ['lyon','aix-les-bains','rumilly','albens']: ")
print(output)


# Partie 2
output = club_par_nombre_de_gymnastes_complexe()
print("doit renvoyer ['lyon;villeurbanne','aix-les-bains','annecy;rumilly','albens']:")
print(output)