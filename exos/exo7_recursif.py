# Etape 1
#  calcul x puissance k (k est un entier) par recursivité
def puissance(x, k):
    #     calcul la puissance par recursivité.
    # toujours penser a arreter la boucle :) donc faire un if...
    # un indice x puissance 0 vaut 1 :)
    return 0


# Etape 2
# voir https://fr.wikipedia.org/wiki/Suite_de_Fibonacci pour la définition d'une suite fibonnaci

# doit renvoyer un tableau de taille n+1 qui contiendra [F0,F1,....Fn]
def suite_fibonacci(n):
    resultat = []
    # tu dois créer une fonction qui s'appelle recursivement et qui calcule les valeurs de fibonacci
    #  cette methode la fera appel a ta fonction
    # rappel pour la recursivite: il faut toujours prévoir une condition qui stoppe la recursivité
    # sinon c'est sans fin ( on dit que c'est une boucle infinie).
    return resultat


# Etape 3
# si tu as du temps refaire mais sans appels recursifs
def suite_fibonacci_sans_recursivite(n):
    resultat = []
    return resultat

# Etape 1

print("5 puissance 2 vaut 25 et tu as:" + str(puissance(5, 2)))
print("2 puissance 8 vaut 256 et tu as:" + str(puissance(2, 8)))

# Etape 2
output = suite_fibonacci(10)
print("fibonnaci de 10 : " + str(output))
print("doit imprimer [0,1,1,2,3,5,8,13,21,34,55]")

# Etape 3 optionnelle
output = suite_fibonacci_sans_recursivite(10)
print("fibonnaci de 10 : " + str(output))
print("doit imprimer [0,1,1,2,3,5,8,13,21,34,55]")
