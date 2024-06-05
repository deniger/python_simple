# ici je définis une classe.
# il faut voir cela comme un contrat: les objets utilisant cette classe auront tous la meme structure.
class ClubGym:
    # cela resemble aux clé du dico
    # la notation :str permet de dire que ce champ est un string
    # c'est bien car cela permet d'éviter les erreurs
    nom: str = ''
    dept: str = ''
    nb_gymnaste: int = 0

    # ca c'est un constructeur: commet tu peux créer une instance de cette classe qui deviendra un objet
    # __init__ c'est un mot clé à savoir
    def __init__(self, init_nom: str, init_dpt: str, init_nb_gymnaste):
        self.nom = init_nom
        self.dept = init_dpt
        self.nb_gymnaste = init_nb_gymnaste

    # c'est une méthode ici. pas une fonction car c'est attaché à la classe
    def get_info(self) -> str:
        return "club: " + self.nom + "(" + self.dept + "), bn_gymnaste=" + str(self.nb_gymnaste)

    # une méthode pour ajouter une gymnaste
    def ajoute_une_gymnaste(self):
        self.nb_gymnaste += 1

    # une méthode pour enlever une gymnaste
    def enleve_une_gymnaste(self):
        self.nb_gymnaste -= 1


# ici je créé des instances on dit objets. c'est plus lisible
# je dois utiliser le constructeur qui définit comment instancier l'objet
#  je met :ClubGym pour indiquer que albens est une instance de la class ClubGym. On dit est du type
albens: ClubGym = ClubGym("albens", '73', 5)
aixlesbains: ClubGym = ClubGym("aix-les-bains", '73', 50)
rumilly: ClubGym = ClubGym("rumilly", '74', 20)
lyon: ClubGym = ClubGym("lyon", '69', 120)

# un avantage c'est que tes données sont plus structurées.

print("j'imprime les info d'aix en appelant la methode get_info")
print(aixlesbains.get_info())
# on ajouter une gymnaste à aix
aixlesbains.ajoute_une_gymnaste()
print("j'imprime les info d'aix après l'ajout d'une gymaste")
print(aixlesbains.get_info())

# le tableau clubs:
clubs: list[ClubGym] = [albens, aixlesbains, rumilly, lyon]


# exemple d'utilisation des objets:
def nombre_total_gymnaste():
    resultat = 0
    for club in clubs:
        resultat = resultat + club.nb_gymnaste
    # a toi
    return resultat


print("nombre total de gymnaste")
print(nombre_total_gymnaste())
lyon.enleve_une_gymnaste()
print("nombre total de gym apres un depart de lyon")
print(nombre_total_gymnaste())

