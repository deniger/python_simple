# renvoie dico avec le nombre d'occurence par caractère trouvé dans texte
def compte_all_characters_occurence(text):
    # doit contenir un dictionnaire avec le nombre d'occurrence par caractere
    resultat={}
    # A TOI :)
    return resultat

# renvoie dico avec  le nombre d'occurence de caractère alphanumeric seulement  trouvé dans texte
def compte_only_alpha_occurence(text):
    # doit contenir un dictionnaire avec le nombre d'occurence par caractere alphanumeric seulement
    # pour aide: voir https://www.w3schools.com/python/ref_string_isalnum.asp. Utiliser la méthode isalnum()
    resultat={}
    # A TOI :)
    return resultat



# Partie 1
output=compte_all_characters_occurence("abcd...")
print("doit renvoyer {'a':1,'b':1,'c':1,'d':1,'.':3} et pas tout l'alphabet :)")
print(output)


# Partie 2
# refaire l'exercice mais qu'en comptant les caractères et pas la ponctuation
output=compte_only_alpha_occurence("aabcd...!,")
print("doit renvoyer {'a':2,'b':1,'c':1,'d':1}")
print(output)
