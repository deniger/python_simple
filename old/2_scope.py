# Exemple pour illustrer les portées (scopes) des variables.

# Une variable définie dans une function est utilisable dans la fonction uniquement: c'est la portée
# dans cet exemple, 2 fonctions vont définir la meme variable Local_var
# Or cette variable est différente: la por

# on reprend les memes fonctions que l' exemple précédent
# on ajoute  la définition d'une variable local: local_var
def my_function():
    # cette variable est définie et utilisable dans cette fonction uniquement
    local_var = "local_var_in_my_function"
    print(f'local_var in my_function is {local_var}')

# une var
def my_function_bis():
    # cette variable est définie et utilisable dans cette fonction uniquement
    # elle a le meme nom que dans le méthode précédente mais valeur différente
    # il faut voir imaginer que chaque fonction est indépendante du reste: on pourrait la créer dans un fichier à part
    local_var = "local_var_in_my_function_bis"
    print(f'local_var in my_function_bis is {local_var}')

def my_function_with_param(param):
    print(f"in my_function_with_param called with {param}")
    # valeur retournée
    return 42

# on appelle les fonctions
my_function()
my_function_bis()
my_function_with_param(" a param")

param_bis="another param"
# on apelle my_function_with_param avec la valeur de la variable param_bis
my_function_with_param(param_bis)
# ces 2 lignes vont générer une erreur
# local_var n'est pas définie globalement
# elle n'est disponible que dans les fonctions my_function et my_function_bis
# génère une erreur
print(f'local var not defined {local_var}')
# param n'est pas définie
print(f'local var not defined {param}')