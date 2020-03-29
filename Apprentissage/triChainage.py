""" Fichier d'explications + exercices pour ce qui est des méthodes de tri chainés en python"""

from operator import  attrgetter

class Inventaire:

    def __init__(self, prod, prx, qtt):
        self.prod = prod
        self.prx = prx
        self.qtt = qtt

    def __repr__(self):
        return "\nProduit: {} <{}*{}".format(self.prod, self.prx, self.qtt)

if __name__ == "__main__":
    
    # Création de l'inventaire
    inventaire = [Inventaire("pomme rouge", 1.2, 19),
                Inventaire("orange", 1.4, 24),
                Inventaire("banane", 0.9, 21),
                Inventaire("poire", 1.2, 24),]
    
    # Pour les tri chainés, il faut commencer par trier selon l'axe le moins 
    # important et finir par le principal. Exemple si on veut trier par prix 
    # ET par quantité vendue, on commencera par trier selon les qtt et ensuite via le prix.
    inventaire = sorted(inventaire, key=attrgetter("qtt"), reverse=True)
    inventaire = sorted(inventaire, key=attrgetter("prx"), reverse=False)

    print(inventaire)