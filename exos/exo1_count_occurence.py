# ecrire le nombre d'occurence
def compte_all_characters_occurence(text):
    # doit contenir un dictionnaire avec le nombre d'occurrence par caractere
    resultat={}
    # A TOI :)
    return resultat

# ecrire le nombre d'occurence de caractère alphanumeric seulement
def compte_only_alpha_occurence(text):
    # doit contenir un dictionnaire avec le nombre d'occurence par caractere alphanumeric seulement
    # pour aide: voir https://www.w3schools.com/python/ref_string_isalnum.asp. Utiliser la méthode isalnum()
    resultat={}
    # A TOI :)
    return resultat




output=compte_all_characters_occurence("abcd...")
# doit renvoyer un dictionnaire avec
# a -> 1
# b -> 1
# c -> 1
# d -> 1
# . -> 3
print(output)


# refaire l'exercice mais qu'en comptant les caractères et pas la ponctuation
output=compte_only_alpha_occurence("aabcd...!,")
# doit renvoyer un dictionnaire avec
# a -> 2
# b -> 1
# c -> 1
# d -> 1
print(output)
