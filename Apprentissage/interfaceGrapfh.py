from tkinter import*
from random import*

def cercle(canc, x, y, r, coul='black'):
    # Création d'un cercle en fonction des coordonnées de son centre
    canc.create_oval(x-r, y-r, x+r, y+r, outline=coul)


class Application(Tk):

    def __init__(self):
        Tk.__init__(self) # On appelle le constructeur de la classe parent
        self.train = []
        self.can = Canvas(self, width=475, height=130, bg="white")
        self.can.pack(side=TOP, padx=5, pady=5)
        Button(self, text='Train', command=self.dessine).pack(side=LEFT)
        Button(self, text='Hello', command=self.coucou).pack(side=RIGHT)
        Button(self, text='Quitter', command=self.quit).pack(side=BOTTOM)
        Button(self, text='Allumer', command=self.allumerFen).pack(side=BOTTOM)
    
    def dessine(self):
        "Instanciation de 4 wagons dans le canvas de l'application"
        self.w1 = Wagon(self.can, 10, 30, 'blue')
        self.w2 = Wagon(self.can, 130, 30, 'red')
        self.w3 = Wagon(self.can, 250, 30, 'green')
        self.w4 = Wagon(self.can, 370, 30)
    

    def coucou(self):
        "Dessin de personnages de manière aléatoire"
        self.clear()
        self.train = [self.w1, self.w2, self.w3, self.w4]
        for pnj in range(5):
            choice(self.train).perso(choice(range(1, 4)))


    def clear(self):
        for w in self.train:
            for f in range(1, 4):
                w.perso(f, coul='white')


    def allumerFen(self):
        self.w1.allumer()
        self.w2.allumer()
        self.w3.allumer()
        self.w4.allumer()



class Wagon(object):

    def __init__(self, canev, x, y, couleur='black'):
        self.canev = canev
        self.x = x
        self.y = y
        self.couleur = couleur 
        # Contour du wagon
        self.canev.create_rectangle(x, y, x+95, y+60, width=1, outline=couleur)
        # Fenetres du wagon
        self.trainFen = []
        for xf in range(x+5, x+90, 30):
            self.trainFen.append(canev.create_rectangle(xf, y+5, xf+25, y+45, fill='black'))
        # Roues du wagon
        cercle(canev, x+18, y+73, 12, 'gray')
        cercle(canev, x+77, y+73, 12, 'gray')


    def perso(self, fen, coul='black'):
        xf = self.x + fen*30 - 12
        yf = self.y + 25
        cercle(self.canev, xf, yf, 10, coul)
        cercle(self.canev, xf-5, yf-3, 2, coul)
        cercle(self.canev, xf+5, yf-3, 2, coul)
        cercle(self.canev, xf, yf+5, 3, coul)


    def allumer(self):
        # Changement de la couleur de la fenetre pour simuler une lumière
        for f in self.trainFen:
            self.canev.itemconfigure(f, fill='yellow')
            



if __name__ == "__main__":
    app = Application()
    app.mainloop()