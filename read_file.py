def lectureMorceau(ligne):
    morceau="morceau"
    duree="duree"
    morceaux=[]
    while ligne!="":
        if morceau in ligne:
            nom = ligne.split(':')
            albummorceau = {}
            albummorceau['morceau'] = nom[1]
            ligne = file.readline()
        if duree in ligne:
            nom = ligne.split(':')
            albummorceau['duree'] = nom[1]
            morceaux.append(albummorceau)
            ligne = file.readline()
        else:
            ligne= file.readline()
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
    album=[]
    print("Ligne lue en premier "+ ligne)
    morceaux=lectureMorceau(ligne)
    print("Ligne lue après lecture morceaux "+ ligne)
    albumnoms = lectureAlbum(ligne)
    album.append(albumnoms)
    album.append(morceaux)
    print(album)


# Step 1: tu ouvres le fichier
file = open("album.txt",'r')

# tu lis la ligne 1 soit "artiste : artiste :  Bob Dylan"
ligne = file.readline()
# quand tu fais cela, le pointeur

Albumentier(ligne)

