"""Fichier d'explications + exemple pour ce qui est des générateurs et iterateur"""

class MyStr(str):
    
    def __iter__(self):
        return MyIter(self)

class MyIter:
    
    def __init__(self, myChaine):
        self.myChaine = myChaine
        self.position = len(self.myChaine) # On veut lire la chaine de droite à gauche

    def __next__(self):
        # Index 0 correspond à la fin de la chaine à l'envers
        if self.position == 0:
            print("Fin de la chaine")
            raise StopIteration
        else:
            self.position -= 1 
            return self.myChaine[self.position]
            

if __name__ == "__main__":
    a = MyStr("Salut !")
    print(a)
    for l in a:
        print(l)