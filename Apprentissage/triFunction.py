# itemgetter pour le tri des objets type tuple/list
from operator import itemgetter
# attrgetter pour le tri des objets fait maison 
from operator import attrgetter

class Etudiant:

    def __init__(self, prenom, age, note):
        self.prenom = prenom
        self.age = age
        self.note = note

    def __repr__(self):
        return"Etudiant {}, ({}, {})".format(self.prenom, self.age, self.note)

if __name__ == "__main__":
    
    # etudiants = [("Clément", 14, 16),
    #             ("Charles", 12, 15),
    #             ("Oriane", 14, 18),
    #             ("Thomas", 11, 12),
    #             ("Damien", 12, 15),]       
    
    # 1er méthode: 
        # La fonction sort() permet de trier les list. De manière 
        # initiale la fonction va trier les éléments de la list  
        # par rapport à leur premier élément. 
    # etudiants.sort()
    # print(etudiants)

    # 2eme méthode: 
        # La fonction sorted permet d'ordonner n'importe quel type 
        # d'objet. Elle renvoie un nouvel objet trié.
    # etudiants = sorted(etudiants, key=lambda etudiant:etudiant[2], reverse=True) # etudiant[2] avec les tuples ou list
    # print(etudiants)


    # Utilsation des fonctions de tri avec les objets
    etudiants = [Etudiant("Clément", 14, 16),
                Etudiant("Charles", 11, 15),
                Etudiant("Oriane", 14, 18),
                Etudiant("Thomas", 11, 12),
                Etudiant("Damien", 12, 15),]
    
    print(etudiants)

    etudiants = sorted(etudiants, key=attrgetter("note", "age"), reverse=True)

    print(etudiants)