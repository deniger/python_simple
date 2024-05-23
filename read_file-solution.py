# dans ton cas, soit tu lis ligne par ligne comme tu as fait
# soit tu stockes toutes les lignes dans un tableau et tu parcours ce tableau

# la logique devrait etre
# tu ouvres le fichier
file = open("album.txt",'r')

# tu lis la partie album avec l'artiste le titre et nb
# il faut faire des readline jusqu'a avoir nb
album_info=litAlbum(file)
nb_morceaux=album_info['nb']
# tu arrêtes la lecture à nb qui doit te donner le nombre de morceau à lire
# tu boucles sur le nombre de morceaus
morceaux=litMorceau(file, nb_morceaux)
file.close()
album={}
album['info']=album_info
album['morceaux']=morceaux

print(album)

