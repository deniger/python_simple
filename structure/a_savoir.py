dico_inscrit_club={}

# ajouter des entrées dans un dico
dico_inscrit_club["albens"]=8
dico_inscrit_club["aix-les-bains"]=10
dico_inscrit_club["compiegne"]=20

# ecrire nombre inscript
def print_nombre_inscrit(club):
    # si le club est connu
    if(club in dico_inscrit_club):
        # je recupere le nombre inscript
        nb_inscript=dico_inscrit_club[club]
        print("il y a "+str(nb_inscript)+" au club "+club)
        print("autre facon d ecrire:")
        print(f"il y a {nb_inscript} au club {club}")
        print("----------------------------")
    # si pas trouvé, club inconnu
    else:
        print("club "+club+" non connu !")
        print("----------------------------")


def supprime_un_club(club):
    # as tu vu cela dans tes cours
    dico_inscrit_club.pop(club,None)
#     ou plus
    if club in dico_inscrit_club:
        del dico_inscrit_club[club]

print_nombre_inscrit("albens")
print_nombre_inscrit("alby")

# pour débuguer tu peux faire des print
print( "on imprime tous les clubs")
print(dico_inscrit_club)
# je supprime compiegne
supprime_un_club("compiegne")
print("Tous les club apres suppression compiegne")
print(dico_inscrit_club)
supprime_un_club("existe pas")
print("Tous les club apres suppression club inconnu")
print(dico_inscrit_club)



