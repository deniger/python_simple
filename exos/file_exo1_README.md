# Exo 1: lire un fichier csv

Voir La doc: https://fr.wikipedia.org/wiki/Comma-separated_values

Dans l'exo 1, il faut faire une fonction qui peut lire un fichier csv.
La lecture du fichier donnera un dictionniare avec :

```javascript
{
headers=[header1,header2,header3,...]
lines=
    [
        {header1=value11,header2=value12,header3=value13, ... ,headerM=value1M },
        {header1=value21,header2=value22,header3=value23, ... ,headerM=value2M },
        ...
        {header1=valueN1,header2=valueN2,header3=valueN3, ... ,headerM=valueNM },
]
}
```

`header1`, `header2`,... sont les valeurs lues dans la première ligne du fichier csv qui sont les titres des colonnes.

Attention: ignorer les commentaires présents et les lignes vides dans le fichier

Tester la lecture avec les exemples [example73.csv](./example73.csv), [example74.csv](./example74.csv)
et [examplehotel.csv](./examplehotel.csv)

pour example73, on devrait avoir une liste contenant 3 dicos avec

```javascript
{
  headers=[ Club,Niveau, Nombre de Gymnastes ]
  lines=[
    { Club=Albens,Niveau=Niveau 2,Nombre de Gymnastes=10 },
    { Club=Aix-les-Bains,Niveau=Niveau 4,Nombre de Gymnastes=20 },
    { Club=Montmélian,Niveau=Niveau 3,Nombre de Gymnastes=15 }
  ]
}
```

pour examplehotel, on devrait avoir une liste de 4 dico

```javascript
{
  headers=[Nom,Ville,Nombre de chambres]
  lines=
    [
      {Nom=Carlton,Ville=Paris,Nombre de chambres=500},
      ...
    ]
}
```

# Exo 2: ecrire un fichier csv

ecrire une fonction qui peut écrire un fichier csv avec les headers..

## Exo 2.1

S'en servir pour réécrire le fichier `examplehotel.csv` dans `examplehotel_sanscommentaire.csv` qui contiendra :

```csv
Nom,Ville,Nombre de chambres
Carlton,Paris,500
Ibis,Annecy,20
Formule 1,Lyon,200
Campanil,Marseille,45
``` 

## Exo 2.2

S'en servir pour écrire un fichier csv `gym.csv` qui contiendra le contenu des fichiers example73 et de exemple74 dans
l'ordre de lecture.
Il faudra ajouter une colonne en plus qui sera le département.

le fichier généré sera du style:

```csv
Club,Département,Niveau,Nombre de Gymnastes
ALbens,Savoie,Niveau 2,10
Aix-les-Bains,Savoie,Niveau 4,20
Montmélian,Savoie,Niveau 3,15
Annecy,Haute-Savoie,Niveau 1,50
Rumilly,Haute-Savoie,Niveau 2,50
```

# Exo 3: comparer des fichiers texte ligne par ligne

Ecrire une fonction qui permet de donner les différences entre 2 fichiers.
- 

- si meme fichier la fonction devra donner "aucune différence entre ..."
- Si les fichiers n'ont pas le meme nombre de lignes il faut écrire "nombre de lignes differents: x dans fichier1 et y
  dans fichier2 " et ensuite comparer sur le nombre de ligne commun (minimum)
- indiquer le nombre de lignes différentes et donner la liste des numéros de lignes avec différences

Les fichiers pour tester sont:

- [compare1.txt](./compare1.txt)
- [compare2.txt](./compare2.txt)
- [compare3.txt](./compare3.txt)

Exemples:

`compare('compare1.txt', 'compare1.txt')` devra donner "aucune différence entre compare1.txt et compare1.txt"
`compare('compare1.txt', 'compare2.txt')` devra donner: "2 ligne(s) differente(s) trouvée(s): [2,3]"
`compare('compare1.txt', 'compare3.txt')` devra donner:

"Nombre de lignes différents: 3 dans compare1.txt et 4 dans compare3.txt
1 ligne(s) differente(s) trouvée(s): [1]"

# Exo 4: approche objet

Proposer des objets Fichier et Ligne qui permettront de représenter le contenu du fichier csv y compris les
commentaires.


# Exo 5: objet simple ( pas terrible comme example...)

# Classe Club
Ecrire une classe Club qui a les attributs suivants:
- nom (string)
- membres un tableau de Personne ( voir ci dessous)

Cette classe a un constructeur qui impose nom ( pas de club sans nom)

Cette classe aura 5 methodes:
- ajouteMembre(Person)
- enleveMembre(nom) ( par simplicite on suppose que le nom d'un membre est unique)
- nombreMembre() -> renvoie le nombre de membre
- affiche() -> print "<nom>, nombre de membres=<nombre de membres>"
- afficheMembres() -> print tous les noms des membres, un par ligne ( pas d'ordre particulier et utiliser la méthode `affiche` de Personne voir ci dessous)

# Classe Personne
Personne est une classe avec 2 attributs:
- nom
- prenom

Cette classe a un constructeur qui demande prenom et nom ( on ne peut pas créer de personne sans donner prenom et nom)

et une methode affiche qui va `print` "prenom nom" de la personne

# Classe ClubGym

une classe ClubGym qui herite de Club.
Un paramètre en plus qui est niveau (un entier).
Le constructeur de cette classe aura 2 parametres: nom et niveau.

Cette classe va devoir:
- surcharger ( ou redéfinir) la méthode affiche et devra imprimer "<nom>, nombre de membres=<nombre de membres>, niveau=<niveau>"
- ajouter 2 methodes augmenteNiveau ( ajoute 1 à niveau) et diminueNiveau



# tests
Créer un tableau de Clubs


```python
clubs=[]
clubs.append(Club("Alby"))
clubs.append(ClubGym("Albens",3))
```

parcourir le tableau club et appeler la méthode `affiche()`







