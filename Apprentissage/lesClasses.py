""" Fichier d'explications + exercices pour ce qui est des classes en python"""

class Personne:

    nbDePersonne = 0
    
    # self désigne l'objet qu'on passe en argument de la fonction
    # Dans le main on accède à la méthode avrc le "." qui renvoie
    # l'objet X en argument dans la méthode
    def __init__(self, nom, prenom, lieu):
        # La variable "nbDePersonne" est un attribu de la classe 
        # et non de l'objet donc on doit utilser Personne pour 
        # que python comprenne qu'il s'agit âs d'un attr de l'objet
        print("Oh un nouveau personnage vient d'être créé !")
        Personne.nbDePersonne +=1
        self.nom = nom
        self.prenom = prenom
        # Losque l'on met le signe "_" devant un attr c'est qu'il est 
        # private, on fera de même avec les méthodes privates
        self._lieuDeResidence = lieu
        
    # La fonction __repr__ permet  de présenter les caractéristiques
    # de l'objet lorsqu'on  fait un print.
    def __repr__(self):
        return "Nom: {}, Prenom: {}, Lieu de résidence: {}".format(self.nom, self.prenom, self.lieuDeResidence)

    # cls remplace self et signifie qu'il sagit d'une méthode de 
    # la classe et  non de l'objet
    def combien(cls):
        return print("Nombre d'objet: ", cls.nbDePersonne)
    # Il faut ensuite utiliser la fonction "classmethod" pour que 
    # Python comprenne qu'il s'agit d'une méthode de classe
    combien=classmethod(combien)

    # Une méthode statique est une fonction lamba, qui n'appartient 
    # ni à l'objet ni à la classe. On ne spécifie donc ni self, ni cls 
    def afficher():
        return print("BlaBlaBla")
    afficher=staticmethod(afficher)



if __name__ == "__main__":
    
    print(Personne.nbDePersonne)
    A = Personne(nom="Marzelle", prenom="Antonin", lieu="Versailles")
    Personne.combien()
    B = Personne(nom="BB", prenom="Poney", lieu="Marseille" )
    Personne.combien()