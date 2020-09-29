import os # Le module os permet de dialoguer avec le système
import pickle # Module pour enregistrer des objets

# Remarque : il sera préférable dans des codes plus important en nombre de variables
# 			 de n'importer que les fonctions dont on a besoin afin d'éviter les conflits de nom

##### Exemple d'ouverture et d'écriture d'un fichier txt #####
# fichier = open("Test_fichier", 'a')
# # La fonction write ne prend que des variables str, donc il faut caster si int ou float.
# fichier.write("Ce fichier sert à s'entrainer pour la manipulation des fichiers via python !\n"
#               "Le confinement me fais gagner de l'argent. \nL'OM est en ligue des champions <3")
# fichier.close()

##### Exemple de lecture de fichier txt #####
# lec = open("Test_fichier", 'r')
# #print(lec.read()) # Sans argument read lit tous le fichier
# print(lec.read(10)) # Lit 10 caractères à partir d'où le curseur est placé dans le fichier
# # Tant que l'on ne close pas le fichier, à chaque fois que l'on appelle la fonction read,
# # celle ci lira à partir du curseur.
# lec.close()

##### Lecture ligne par ligne #####
# lec = open('Test_fichier', 'r')
# while True:
#     ligne = lec.readline() # A chaque appel de la fonction celle ci reprend la lecture au niveau du curseur
#     #  La fonction READLINES() permet de lire toute les ligne d'un fichier et de les sotcker ligne par ligne
#     # dans une liste
#     if ligne == "":
#         print('\n##########################\nLecture du fichier terminée')
#         break # Si on arrive a la fin du fichier on arrete la lecture
#     print(ligne) # Sinon on l'affiche
# lec.close()

##### Ecrire des objets #####
# a, b, c = 27, 34.9890, [5, 8.8, 'lol']
# fichier = open('Test_pickle', 'wb') # Ecriture binaire
# pickle.dump(a, fichier)
# pickle.dump(b, fichier)
# pickle.dump(c, fichier)
# fichier.close()

##### Lecture d'objets #####
# lec = open('Test_pickle', 'rb')
# d = pickle.load(lec) # Lecture de l'objet 1
# e = pickle.load(lec) # Lecture de l'objet 2
# f = pickle.load(lec) # Lecture de l'objet 3
# # Avec cette méthode on peut retrouver avec précision l'identité
# # d'un objet car pickle conserve le typage de chaque variable. => Voir print
# # Dans le cas d'un fichier texte, tous devient str...
# print('1:', type(d), d)
# print('2:', type(e), e)
# print('3:', type(f), f)
# lec.close()



##### EXERCICEs #####

def try_open(fileName):
    try:
        fichier = open(fileName, 'r')
        fichier.close()
        return 1
    except:
        return 0

def under_writing(path):
    writting = True
    buffer = ""
    while writting:
        ajout = input()
        if ajout == "":
            writting = False
            fichier = open(path, 'a')
            fichier.write(buffer)
            fichier.close()
        else:
            buffer += "\n" + ajout

def lector(path):
    fichier = open(path, 'r')
    print(fichier.read())
    fichier.close()

def findTallestLine(path):
    maxSize = 0
    with open(path, 'r') as fichier:
        txt = fichier.read()
        # Une liste séparant le texte par rapport au points
        txt = txt.split(".")
        for phrase in txt:
            size = len(phrase)
            if size > maxSize:
                maxSize = size
                returned_phrase = phrase
        print("La phrase la plus longue du texte est: " + returned_phrase)
        print("Nombre de caractères: " + str(maxSize))

# Définition de la fonction multiplication
def tabMult(x):
    table_x = list()
    for i in range(20):
        table_x.append(str(x*(i+1)))
    return table_x

def createMultFile(min, max):
    range_between = range(min, max+1)
    print(range_between)
    tabOfMult = list()
    for x1 in range_between:
        # On calcul les tables de mult pour l'ensemble des
        # valeurs que l'on vient stocker dans un même tableau
        tabOfMult.append(tabMult(x1))
    with open('MultFile.txt', 'w') as fichier:
        for x2 in tabOfMult:
            fichier.write("Table de " + str(x2[0]) + ":\n ")
            fichier.write(str(x2[:]) + '\n')


if __name__ == '__main__':
    path = "Test_fichier"
    while True:
        # On vérifie la bonne ouverture du fichier
        if try_open(path):
            print('Quel traitement voulez-vous réaliser sur le fichier ?')
            print('1- Ajouter du texte')
            print('2- Lire le contenu')
            print('3- Trouver la plus longue phrase du texte')
            print('4- Generer fichier table de multiplication')
            print('ELSE- Quitter le programme')
            choice = input()
            if choice == '1':
                print("Saisissez votre texte: ")
                under_writing(path)
                print("Fin de la saisie")
            elif choice == '2':
                print("Contenu du fichier: ")
                lector(path)
            elif choice == '3':
                print('Analyse...')
                findTallestLine(path)
            elif choice == '4':
                print('Veuilliez saisir le min et le max :')
                min = int(input())
                max = int(input())
                createMultFile(min, max)
            else:
                print("ERROR: Saisir une valeur possible.")
                print("Fin du programme")
                break
