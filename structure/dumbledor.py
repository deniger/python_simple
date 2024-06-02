# je refais l'exo juste pour t'indiquer comme décomposer le probleme

def change_caractere(input):
    # tu as trouvé toute seule qu'il fallait faire un dictionnaire. Donc rien à dire ici
    # pour ne pas t'embrouiller si tu as un dico, nomme le toujours avec dico pour savoir ce que c'est
    dico_chars = {"oi": "ou", "ou": "in", "ne": "au"}

    # il faut que tu décomposes le probleme.
    # je dois parcourir la liste input
    # recuperer 2 caractères qui se suivent dans valeur a tester
    # si cette valeur appartient au dictionnaire il faut la remplacer avec la valeur. Go:
    for i in range(len(input) - 1):
        chaine_a_tester = input[i:i + 2]
        # c'est la ou tu as du mal...
        # tu dois tester si cette variable est dans le dictionnaire
        if chaine_a_tester in dico_chars:
            # la chaine_a_tester est bien dans le dico
            # je prends sa valeur issue du dico
            nouvelle_chaine = dico_chars[chaine_a_tester]
            # la tu sais faire
            input = input[:i] + nouvelle_chaine + input[i + 2:]
    return input


# peut etre compliqué. Mais ave
# il ne faut pas retester
# oubli cela si trop compliqué
def change_caractere_avec_while(input):
    dico_chars = {"oi": "ou", "ou": "in", "ne": "au"}
    i = 0
    while i < len(input) - 1:
        chaine_a_tester = input[i:i + 2]
        if chaine_a_tester in dico_chars:
            nouvelle_chaine = dico_chars[chaine_a_tester]
            input = input[:i] + nouvelle_chaine + input[i + 2:]
            # peut etre compliqué: en fait vu que tu viens de remplacer 2 caractères,
            #  il ne faut pas les retester
            i += 2
        else:
            i += 1
    return input


output = change_caractere("Coicoi Emeloue ! ne dodo ?")
print(" notre premiere methode: " + output)
output = change_caractere_avec_while("Coicoi Emeloue ! ne dodo ?")
print(" notre deuxieme methode: " + output)
