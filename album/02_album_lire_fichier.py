# Dans cette etape on va juste compléter la fonction lire_file
# je supprime les autres methodes inutile pour l'instant

# une fonction qui prend en parametre un fichier et qui renvoie un tableau de lignes
def lire_file_methode_standard(file):
    print("lecture du fichier " + file)
    file = open(file, 'r')
    lignes_brutes = file.readlines()

    print("les lignes_brutes non FORMATÉES du fichier sont dans ce tableau (avec \\n à la fin):")
    print(str(lignes_brutes))

    print("on va créer un tableau avec les lignes_brutes nettoyées")
    lignes = []
    # on parcourt le tableau de lignes brutes
    for line in lignes_brutes:
        # on ajoute les lignes nettoyées avec strip
        lignes.append(line.strip())
    file.close()
    return lignes


# une fonction qui prend en parametre un fichier et qui renvoie un tableau de lignes
def lire_file_methode_court(file):
    file = open(file, 'r')
    # et on split
    tableau = file.read().splitlines()
    file.close()
    return tableau


lignes = lire_file_methode_standard("album.txt")
print("les lignes du fichier avec la méthode usuelle")
print(str(lignes))
lignes = lire_file_methode_court("album.txt")
print()
print("les lignes du fichier avec la méthode courte")
print(str(lignes))

print("pour la suite il faudra choisir entre les 2 solutions. On prendra la solution usuelle...")
print()
print("Tu as posé la question pour itérer sur un tableau... ")
print()
print("parcourir le tableau avec un iterateur normal")
for ligne in lignes:
    print("je parcours le tableau avec un iteratiom: " + ligne)

print()
print("parcourir le tableau avec un indice dans le tableau")
# i va prendre les valeur de 0 a nombre de ligne
for i in range(len(lignes)):
    print("la ligne "+str(i)+" est "+lignes[i])