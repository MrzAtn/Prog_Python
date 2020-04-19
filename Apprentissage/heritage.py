""" Fichier d'explications + exercices pour ce qui est de l'héritage en python"""
# Héritage: 
    # 2 classes, a -> classe mère ;  b-> hérite de a.
    # Toutes les méthode et attribu de la classe "a" seront dispo pour "b"
    # De plus, la classe b pourra modifier les méthodes de la classe a, 
    # avoir ses propres méthodes et attributs.

class A: # On déclare dans un premier temps une class mère
    pass

class B(A): # Syntaxe pour l'héritage. Signifie que  B hérite de A
    pass

# Héritage multiple
class C:
    pass

class D(A, C): # La classe D hérite alors de la classe A et C.
    pass


#################   Cas pratique    #################

class EV:
    def __init__(self, typeEV):
        self.type = typeEV

    def test(self):
        return print("test")

class Personne(EV):

    def __init__(self, nom):
        super.__init__("Humanoïde")
        self.nom = nom
        self.prenom = "Polo"
    
    def __str__(self):
        return "Personne: \n \t Nom: {} \n \t Prenom {}".format(self.nom, self.prenom)


class AgentSpecial(Personne):

    # La méthode "super" permet  d'appeler le constructeur de la class mère. 
    # Si on ne l'utilise pas, notre agent n'aura pas de "prenom".
    def __init__(self, nom, matricule):
        super().__init__(nom)
        self.matricule = matricule

    # Fonction appelée lorsqu'on veut print l'objet
    def __str__(self):
            return "Agent Special: \n \t Matricule: {} \n \t Nom: {}".format(self.matricule, self.nom)


if __name__ == "__main__":
    
    a = AgentSpecial("Bob", "M63AA15")
    # Dans le cas ou on appelle une fonction de la class GM, Python va chercher
    # la méthode dans un premier temps dans la class mère puis dans la  GM s'il 
    # ne la trouve pas.
    a.test() # Méthode de la class GM