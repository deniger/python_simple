le problème:
ecrire une fonction qui prend en paramètre un nom de fichier de type album et qui donne la structur

il faut diviser le probleme pour mieux régner...

# Etape 1:01_album_structure.py
faire la structure du programme comme demandé:
- on crée une fonction qui prend en parametre le fichier
- on lit le fichier et on met le tout dans un tableau de string
- on analyse la structure

Pourquoi mettre le fichier dans un tableau ?
Comme cela la problématique de lecture du fichier est faite et plus besoin de mettre des readline de partout
dans le code

Si tu fais tourner ce fichier tu aura juste des messages et rien ne se fait mais tu as une structure et ton probleme
est divisé en problèmes plus petit

# Etape 2: 02_album_lire_fichier.py
- lire le fichier et mettre toutes les lignes dans un tableau
- plusieurs options pour cela (tu peux utiliser chatgpt pour générer le code)
- ce fichier ne montre que la lecture
- comme tu posais la question à la fin je mets 2 façons d'itérer sur le tableau


# Etape 3: 03_album_analyser_info_principale.py
lire les infos principales du de l'album soit artiste, titre nb


# Etape 4: 04_album_analyser_morceaux.py
lire les morceaux en reprenant ton code
tout le fichier est désormais analysé mais on ne prend pas en compte nb

# Etape 5: 05_album_utilisation_nb.py ( peut etre optionel)
prise en compte de nb qui doit donner le nombre de morceaux

# Etape 6: correction de bug (optionel et complexe surement)
il y a des bugs possible dans le code
il faut utiliser
`if ligne.startswith(artiste):`
pour etre sur que la ligne commence par "artiste: " (de meme pour le reste)
Par exemple si tu as

artiste: Bob nb Dylan

Cela sera vu comme nb