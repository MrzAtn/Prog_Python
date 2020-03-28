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
    
    inventaire = sorted(inventaire, key=attrgetter("qtt"), reverse=True)
    inventaire = sorted(inventaire, key=attrgetter("prx"), reverse=False)

    print(inventaire)