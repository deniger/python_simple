# comme demandé une fonction qui prend en parametre un fichier et qui va renvoyer la structure du fichier
# la methode principale
def lecture_album(file):
    # on lit les lignes
    lines = lire_file(file)
    # on les analyses
    resultat = cree_structure(lines)
    return resultat;


# une fonction qui prend en parametre un fichier et qui renvoie un tableau de lignes
def lire_file(file):
    print("lecture du fichier " + file)


# analyse les lignes et renvoie la structure
def cree_structure(lines):
    # la structure sous forme de dictionnaire
    album = {}
    # les infos générales ( artiste, titre et nb) seront dans l'entréé info et dans un dico
    album["info"] = {}
    # les morceaux seront dans un tableau de dictionnaire
    album["morceaux"] = []
    return album


# le corps principal du fichier
structure_album = lecture_album("album.txt")
print("la structure du fichier est")
print(structure_album)

print("maintenant il faut completer les fonctions lire_file et cree_structure")
