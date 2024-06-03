def reverse_tableau(tableau_chars):
    # tu dois inverser le tableau tableau_chars mais sans creer de nouveau tableau.
    # tout doit se faire dans tableau_chars
    # pense à une variable temporaire pour stocker des caractere temporairement...
    # aide: avec [ toto1 toto2 toto3 toto 4 toto 5]
    # pour inverser, il suffirait d'iterer sur la moitié du tableau et
    # d'inverser toto1 et toto 5
    # puis toto2 et toto4,....
    return tableau_chars



output = reverse_tableau(['a','b','c','d'])
print("tableau dans l'ordre inverse est : "+str(output))
print("doit imprimer [d', 'c', 'b', 'a']")

output = reverse_tableau(['a','b','c','d','e'])
print("tableau dans l'ordre inverse est : "+str(output))
print("doit imprimer ['e','d', 'c', 'b', 'a']")
