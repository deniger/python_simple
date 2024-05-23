
# Step 1: tu ouvres le fichier
file = open("album.txt",'r')

# tu lis la ligne 1 soit "artiste : artiste :  Bob Dylan"
ligne = file.readline().strip() # Je mets strip pour enlever le \n
print("ligne 1: "+ ligne)
# quand tu fais cela, le pointeur passe à la ligne suivante:
# donc si tu rappelles la file.readline() tu es à la ligne 2
ligne = file.readline().strip()
print("ligne 2: "+ ligne)


