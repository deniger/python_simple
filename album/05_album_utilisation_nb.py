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
    album_info = {}
    # contiendra les morceaux
    morceaux = []

    # je  reprends ton code
    artiste = "artiste"
    titre = "titre"
    nb = "nb"
    # on ajoute les morceaux
    morceau = "morceau"
    duree = "duree"

    # permet de savoir si la ligne nb a été lue
    is_nb_lu_dans_album_info = False
    # le nombre lu dans nb:
    nb_lu_dans_album_info = 0
    # le nombre de morceau
    nb_morceau_lu = 0

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
            # ok nb : a été trouvé
            is_nb_lu_dans_album_info = True
            nb_lu_dans_album_info = int(album_info['nb'])
        #     morceaux
        if morceau in ligne:
            # un morceau est défini mais on n'a pas encore lu la ligne nb:
            if is_nb_lu_dans_album_info == False:
                print("ERREUR: fichier non valide car nb non lu et morceau trouvé")
                break
            nom = ligne.split(':')
            morceau_info = {}
            morceau_info['morceau'] = nom[1].strip()
        if duree in ligne:
            nom = ligne.split(':')
            morceau_info['duree'] = nom[1].strip()
            morceaux.append(morceau_info)
            # on incremente le compteur
            nb_morceau_lu = nb_morceau_lu + 1
            # on pourrait faire un break pour ne lire que nb_lu_dans_album_info

    # la structure final
    album = {}
    album["info"] = album_info
    # les morceaux seront dans un tableau de dictionnaires
    album["morceaux"] = morceaux

    if is_nb_lu_dans_album_info == False:
        print("ERREUR: nb: non trouvé dans le fichier")
    elif nb_lu_dans_album_info == nb_morceau_lu:
        print("OK: le nombre lu de morceau est valide comme annoncé soit: " + str(nb_lu_dans_album_info))
    else:
        print("ERREUR: le nombre lu de morceau n'est pas valide")
        print("\tle nombre de morceaux annoncés: " + str(nb_lu_dans_album_info))
        print("\tle nombre de morceaux lus: " + str(nb_morceau_lu))
    return album


# le corps principal du fichier
lecture_album("album.txt")
print("")
lecture_album("album_pas_nb.txt")
print("")
lecture_album("album_pas_assez_morceau.txt")