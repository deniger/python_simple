# pour lire toutes les lignes d'un fchier
print("---------------------------")
print("Solution qui ne fait pas de strip et donc avec les retours chariots")
file = open("album.txt",'r')
ligne=file.readline()
tableau=[]
while ligne!="":
    tableau.append(ligne)
    ligne=file.readline()
file.close()
print("fichier lu avec readLine et sans strip est \n"+str(tableau))
print()
print("---------------------------")
print("Solution qui fait appel à strip et donc sans les retours chariots")
file = open("album.txt",'r')
ligne=file.readline();
tableau=[]
while ligne!="":
    tableau.append(ligne.strip())
    ligne=file.readline()
file.close()
print("fichier lu avec readLine et utilisant strip est \n"+str(tableau))

