# copie methode de exo 1
def compte_all_characters_occurence(text):
    # doit contenir un dictionnaire avec le nombre d'occurrence par caractere
    resultat={}
    # copie ici le code de l'exo 1 :)
    return resultat

# retourne le caractere avec le plus d'occurence trouve dans dico_occurence
def renvoie_char_avec_max_occurence(dico_occurence):
    resultat=''
    # attention le dico est un parametre et tu dois parcourir dico_occurence
    # A TOI :)
    return resultat

#  retourne un tableau trié des caracteres trouves "nombre_occurence" fois dans le dico "dico_occurence"
def renvoie_tableau_trie(dico_occurence, nombre_occurence):
    resulat=[]
    #  A TOI :)
    return resulat

#  retourne un dictionnaire qui contient "nb occurence" -> "tableau caracteres triés trouve nb fois"
def renvoie_dico_liste_de_caractere_par_occurence(dico_occurence):
    resulat= {}
    #  A TOI :)
    # tu peux utiliser les autres methodes de cet exo ou pas...
    # ou tu peux refaire ici. Attenion il faut retrier les tableaux après les travaux :). Option...
    return resulat


#  résultat de l'exercice 1
# le résultat doit etre {'z':1,'a':1,'b':1,'c':1,'d':1,'.':3}
output=compte_all_characters_occurence("zabcd...")

# Partie 1
char_avec_max_occurence=renvoie_char_avec_max_occurence(output)
print("le caractere avec le plus d'occurence doit être . et tu trouves: "+char_avec_max_occurence)

# Partie 2
liste_trie=renvoie_tableau_trie(output, 1)
print("la liste triee des caracteres avec 1 occurence doit etre a,b,c,d,z: "+str(liste_trie))

# Partie 3
dico_liste_par_nombre_occurence=renvoie_dico_liste_de_caractere_par_occurence(output)
print("doit renvoyer {1:[a,b,c,d,z],3:[.]}: " + str(dico_liste_par_nombre_occurence))