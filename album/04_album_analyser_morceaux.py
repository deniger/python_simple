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
    file = open(file, 'r')
    lignes_brutes = file.readlines()
    lignes = []
    for line in lignes_brutes:
        lignes.append(line.strip())
    file.close()
    return lignes


# analyse les lignes et renvoie la structure
def cree_structure(lignes):

    # contiendra les infos générales ( artiste, titre et nb)
    album_info={}
    # contiendra les morceaux
    morceaux=[]

    # je  reprends ton code
    artiste = "artiste"
    titre = "titre"
    nb = "nb"
    # on ajoute les morceaux
    morceau="morceau"
    duree="duree"
    # on itere sur les lignes
    for ligne in lignes:
        # je reprends ton code
        if artiste in ligne:
            nom = ligne.split(':')
            # j'ajoute strip ici pour enlevr les espaces en trop
            # tu peux enlever pour voir la diff
            album_info['artiste'] = nom[1].strip()
        if titre in ligne:
            nom = ligne.split(':')
            album_info['titre'] = nom[1].strip()
        if nb in ligne:
            nom = ligne.split(':')
            album_info['nb'] = nom[1].strip()
    #     morceaux
        if morceau in ligne:
            nom = ligne.split(':')
            morceau_info = {}
            morceau_info['morceau'] = nom[1].strip()
        if duree in ligne:
            nom = ligne.split(':')
            morceau_info['duree'] = nom[1].strip()
            morceaux.append(morceau_info)


    # la structure final
    album = {}
    album["info"] = album_info
    # les morceaux seront dans un tableau de dictionnaires
    album["morceaux"] = morceaux
    return album


# le corps principal du fichier
structure_album = lecture_album("album.txt")
print("la structure du fichier est")
print(structure_album)