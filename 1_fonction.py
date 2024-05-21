# Structure basique d'un script Python

# tu définis les fonctions pour commencer
# la définition d'une fonction commence par def
# tu ne fais que définir et tu n'appelles pas :)
def my_function():
    print("in my_function")

# définition de la fonction my_function_bis
def my_function_bis():
    print("in my_function_bis")


def my_function_with_param(param):
    print(f"in my_function_with_param called with {param}")
    # valeur retournée
    return 42

# maintenant tu peux utiliser les fonctions
# appel basique# Structure basique d'un script Python

# tu définis les fonctions pour commencer
# la définition d'une fonction commence par def
# tu ne fais que définir et tu n'appelles pas :)
def my_function():
    print("in my_function")

# définition de la fonction my_function_bis
def my_function_bis():
    print("in my_function_bis")


#  param est une entrée de la fonction
# param est utilisable à l'intérieur de la fonction
def my_function_with_param(param):
    print(f"in my_function_with_param called with {param}")
    # valeur retournée
    return 42

# maintenant tu peux utiliser les fonctions
# appel basique
my_function()
# encore un appel basique
my_function_bis()
# appel avec un paramètre et qui renvoie une valeur (42):
value_returned=my_function_with_param('a parameter')
print(f'the value returned is {value_returned}')