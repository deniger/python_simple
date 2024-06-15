# Exo 1: lire un fichier csv
Voir La doc: https://fr.wikipedia.org/wiki/Comma-separated_values

Dans l'exo 1, il faut faire une fonction qui peut lire un fichier csv.
La  lecture du fichier donnera une liste de dicos du style:

```
[
{header1=value11,header2=value12,header3=value13},
{header1=value21,header2=value22,header3=value23},
...etc
{header1=valueN1,header2=valueN2,header3=valueN3}
]
```

`header1`, `header2`,... sont les valeurs lues dans la première ligne du fichier csv.

Attention: ignorer les commentaires présents et les lignes vides dans le fichier 


Tester la lecture avec les exemples [example73.csv](./example73.csv), [example74.csv](./example74.csv) et [examplehotel.csv](./examplehotel.csv)


pour example73, on devrait avoir une liste contenant  3 dicos avec

```
[
{Club=Albens,Niveau=Niveau 2,Nombre de Gymnastes=10},
{Club=Aix-les-Bains,Niveau=Niveau 4,Nombre de Gymnastes=20},
{Club=Montmélian,Niveau=Niveau 3,Nombre de Gymnastes=15},
]
```

pour examplehotel, on devrait avoir une liste de 4 dico


```
[
{Nom=Carlton,Ville=Paris,Nombre de chambres=500},
etc...
]
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
S'en servir pour écrire un fichier csv `gym.csv` qui contiendra le contenu des fichiers example73 et de exemple74 dans l'ordre de lecture.
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

# Exo 3: comparer des fichiers

Ecrire une fonction qui permet de donner les différences entre 2 fichiers.
- 
- si meme fichier la fonction devra donner "aucune différence entre ..."
- Si les fichiers n'ont pas le meme nombre de lignes il faut écrire "nombre de lignes differents: x dans fichier1 et y dans fichier2 " et ensuite comparer sur le nombre de ligne commun (minimum)
- indiquer le nombre de lignes différentes  et donner la liste des numéros de lignes avec différences

Exemples:

`compare('compare1.txt', 'compare1.txt')` devra donner "aucune différence entre compare1.txt et compare1.txt"
`compare('compare1.txt', 'compare2.txt')` devra donner: "2 ligne(s) differente(s) trouvée(s): [2,3]"
`compare('compare1.txt', 'compare3.txt')` devra donner: 

"Nombre de lignes différents: 3 dans compare1.txt et 4 dans compare3.txt
1 ligne(s) differente(s) trouvée(s): [1]"

# Exo 4: approche objet
Proposer des objets Fichier et Ligne qui permettront de représenter le contenu du fichier csv y compris les commentaires.
