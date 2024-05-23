def lectureMorceau(ligne):
    morceau="morceau"
    duree="duree"
    morceaux=[]
    while ligne!="":
        if morceau in ligne:
            nom = ligne.split(':')
            albummorceau = {}
            albummorceau['morceau'] = nom[1]
            ligne = file.readline().strip()
        if duree in ligne:
            nom = ligne.split(':')
            albummorceau['duree'] = nom[1]
            morceaux.append(albummorceau)
            ligne = file.readline().strip()
        else:
            ligne= file.readline().strip()
    return(morceaux)

def lectureAlbum(ligne):
    artiste = "artiste"
    titre = "titre"
    nb = "nb"
    artistetitre=[]
    while ligne!="":

        if artiste in ligne:
            nom = ligne.split(':')
            albumnom = {}
            albumnom['artiste'] = nom[1]
            ligne = file.readline()
        if titre in ligne:
            nom = ligne.split(':')
            albumnom['titre'] = nom[1]
            ligne = file.readline()
        if nb in ligne:
            nom = ligne.split(':')
            albumnom['nb'] = nom[1]
            artistetitre.append(albumnom)
            ligne = file.readline()
        else:
            ligne= file.readline()
    return(albumnom)

def Albumentier(ligne):
    # Step 2 du code: c'est ici et ligne vaut "artiste :  Bob Dylan"
    print("Ligne lue en premier "+ ligne)
    album=[]
    # Step 3: tu appelles la fonction lectureMorceau avec comme parametre ligne qui
    # vaut toujours "artiste :  Bob Dylan"
    morceaux=lectureMorceau(ligne)
    # Step 3 conséquence:
    # dans cette fonction tu fais appel à file.readline() jusqu'a ce que ligne vaut ""
    # ce qui veut dire que maintenant le pointeur dans le fichier est à la fin du fichier
    print("Preuve que le pointeur est en fait de fichier. Si je fais readline ici j'ai rien: "+file.readline().strip())

    ## attention ici: la variable ligne vaut toujours "artiste :  Bob Dylan"
    ## c'est la portée des variables !
    ## voir https://www.w3schools.com/PYTHON/python_scope.asp ou le fichier 2_scope.py
    ## Si tu assignes une nouvelle variable dans une fonction ce n'est propagé.
    print("valeur de la variable Ligne lue après lecture morceaux "+ ligne)

    # Step 4: donc ici tu essaies de lire l'album.
    # tu passe en parametre ligne qui vaut "artiste :  Bob Dylan" donc tu peux récupérer l'artiste.
    # mais tu n'as pas le titre car ton readline va renvoyer vide pour les raisons ci-dessus.
    albumnoms = lectureAlbum(ligne)
    album.append(albumnoms)
    album.append(morceaux)
    print(album)


# Step 1: tu ouvres le fichier
file = open("album.txt",'r')

# Step 1: tu lis la ligne 1 soit "artiste : artiste :  Bob Dylan"
ligne = file.readline()
# Step 1 conséquence : maintenant le pointeur dans file est à la ligne 2
# donc quand tu vas appeler readline à nouveau la résultat sera "titre : Bob Dylan Greatest Hits"
# go to step 2 de ton code: Albumentier
Albumentier(ligne)
# il faut fermer le fichier:
file.close()

