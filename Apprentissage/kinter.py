# Module pour les interfaces graphique
from tkinter import*
from random import randrange

# ##############################################################################################################################
# # Creation de l'objet fenetre (maitre)                                                                                       #   
# fen = Tk()                                                                                                                   #
#                                                                                                                              #
# # Creation des widget (esclaves)                                                                                             #
# can = Canvas(master=fen, bg='dark grey', height=200, width=200) # On détermine son maitres (sa position) via l'arg "master"  #
# can.pack(side=LEFT) # Fonction de l'objet pack permettant d'ajuster la taille du maitre en fonction de ses esclaves          #
# b1 = Button(master=fen,text="Quitter", command=fen.quit) # arg "command" permet d'attribuer une fonction à notre boutton     #
# b1.pack(side=BOTTOM)                                                                                                         #
# fen.mainloop() # Fonction permettant d'écouter h24 les interactions ex: clic sur boutton                                     #
#                                                                                                                              #
# ##############################################################################################################################

############################# Exercices 1 #############################
# # Fontion permettant le tracer dans la fenetre graphique
# def drawline():
#     global x1, y1, x2, y2, coul
    
#     can.create_line(x1, y1, x2, y2, width=2, fil=coul)
#     # Modification auto pour le tracer de la prochaine ligne 
#     y2, x2 = y2+30, x2+30

# # Fonction permettant le changement de couleur auto du tracé 
# def changecolor():
#     global coul
#     pal = ["cyan", 'maroon', 'green']
#     choice = randrange(3)
#     coul = pal[choice] 

# def drawline2():
#     h = can.winfo_height()
#     w = can.winfo_width()
#     r = h/w
#     can.create_line(150, h/2, w-150, h/2, width=2, fil='red') # Ligne horizontale 
#     can.create_line(w/2, 150*r, w/2, h-150*r, width=2, fil='red') # Ligne verticale 

# x1, y1, x2, y2 = 0, 20, 500, 20
# coul = 'green'

# fen = Tk()
# can = Canvas(master=fen, bg='dark grey', height=650, width=500)
# can.pack(side=LEFT)
# b1 = Button(master=fen,text="Quitter", command=fen.quit)
# b1.pack(side=BOTTOM)
# b2 = Button(master=fen,text="Tracer une ligne", command=drawline)
# b2.pack()
# b3 = Button(master=fen,text="Autre couleur", command=changecolor)
# b3.pack()
# b4 = Button(master=fen,text="Viseur", command=drawline2)
# b4.pack()
# fen.mainloop()

############################# Exercices 2 Olympique #############################

# # Anneaux r = 50
# def drawJO():
#     # On efface le tableau
#     can.delete(ALL)
#     global coord, col
#     i = 0
#     while i< 5:
#         can.create_oval(coord[i][0],coord[i][1],coord[i][0]+100,coord[i][1]+100, width=2, outline=col[i])
#         i += 1

# def drowCricle(numCicle):
#     global coord, col
#     can.create_oval(coord[numCicle][0],coord[numCicle][1],coord[numCicle][0]+100,coord[numCicle][1]+100, width=2, outline=col[numCicle])

# def drawBlack():
#     drowCricle(1)

# def drawBlue():
#     drowCricle(0)

# def drawRed():
#     drowCricle(2)

# def drawYellow():
#     drowCricle(3)

# def drawGreen():
#     drowCricle(4)


# coord = [[50, 30], [150, 30], [250, 30], [100, 80], [200, 80]]
# col = ['blue', 'black', 'red', 'yellow', 'green']
# fen = Tk()
# can = Canvas(master=fen, bg='white', height=300, width=400)
# can.pack(side=TOP)
# b1 = Button(master=fen,text="Quitter", command=fen.quit)
# b1.pack(side=BOTTOM, pady=3)
# b2 = Button(master=fen,text="JO LOGO", command=drawJO)
# b2.pack(side=BOTTOM, pady=3)

# b3 = Button(master=fen,text="Bu", command=drawBlue)
# b3.pack(side=LEFT, padx=2)
# b4 = Button(master=fen,text="Bk", command=drawBlack)
# b4.pack(side=LEFT, padx=2)
# b5 = Button(master=fen,text="Rd", command=drawRed)
# b5.pack(side=LEFT, padx=2)
# b6 = Button(master=fen,text="Yw", command=drawYellow)
# b6.pack(side=LEFT, padx=2)
# b7 = Button(master=fen,text="Gn", command=drawGreen)
# b7.pack(side=LEFT, padx=2)

# fen.mainloop()

############################# Exercices 3 Damier #############################

def ligne_carre(x, y):
    global side 
    i = 0
    while i<5:
        can.create_rectangle(x+i*60, y, x+i*60+side, y+side, fill='black')
        i += 1

def initDamier():
    global side
    y = 0
    while y < 10: # Ligne i
        if y%2: 
            x = 0
            # On construit notre damier ligne par ligne
            ligne_carre(x*side, y*side)

        else: 
            x = 1
            ligne_carre(x*side, y*side)
        y += 1

def cercle(x, y, r): # Definition d'une méthode permettant le tracé d'un cercle à partir de son centre
    can.create_oval(x-r, y-r, x+r, y+r, outline='red', width='2')  

def placerPion():
    global side
    x = side*randrange(10) + side/2
    y = side*randrange(10) + side/2
    print(x, y)
    cercle(x, y, 10)


side = 30
fen = Tk()
can = Canvas(master=fen, bg='white', height=300, width=300)
can.pack(side=TOP)
b1 = Button(master=fen,text="Quitter", command=fen.quit)
b1.pack(side=LEFT, pady=3)
b2 = Button(master=fen,text="Init Damier", command=initDamier)
b2.pack(side=RIGHT, pady=3)
b3 = Button(master=fen,text="Pion", command=placerPion)
b3.pack(side=RIGHT, pady=3)
fen.mainloop()

############################ Exercices 4 Repare clic #############################

# def cercle(x, y, r):
#     can.create_oval(x-r, y-r, x+r, y+r, outline='red', width='2')

# def cliqueur(event): # Argument "event" spécifie que la fonction est lié à un évènement type 'Button-1'
#     chaine.configure(text='Clic détécté au coordonnées: X=' + str(event.x) +', Y='+ str(event.y))
#     cercle(event.x, event.y, 10)

# fen = Tk()
# can = Canvas(master=fen, bg='white', height=300, width=300)
# # La méthode bind lie le clique à notre méthode.
# can.bind("<Button-1>", cliqueur)
# can.pack(side=TOP)
# chaine = Label(master=fen)
# chaine.pack()
# b1 = Button(master=fen,text="Quitter", command=fen.quit)
# b1.pack(side=BOTTOM, pady=3)
# fen.mainloop()

############################# Exercices 5 Organisation GUI #############################

"""L'organisation des widget composant notre interface peuvent être paramètrée via les méthodes grid()/pack() et place()"""

# fen = Tk()

# Label(master=fen, text="Nom:").grid(row=0, column=0) # Row == ligne / column == colonne 
# Label(master=fen, text="Prénom:").grid(row=1, column=0)
# Label(master=fen, text="Mail:").grid(row=2, column=0)
# entr1 = Entry(fen) # Le widget Entry permet de créer des zone de de texte pour l'utilisateur 
# entr2 = Entry(fen)
# entr3 = Entry(fen)
# entr1.grid(row=0, column=1)
# entr2.grid(row=1, column=1)
# entr3.grid(row=2, column=1)
# can = Canvas(master=fen, bg="white", width=160, height=160)
# photo = PhotoImage(file='')
# can.create_image(80, 80, image=photo)
# can.grid(row=0, column=2, rowspan=3, padx=2, pady=2) # padx et pady permette de créer un espace entre les widget
# fen.mainloop()

############################# Exercices 6 Déplacement d'objet #############################

# L'exemple permet d'introduire les méthodes pour déplacer des objets une fenêtre Tkinter.

# def mvt(gd, hb):
# 	global x1, y1
# 	x1, y1 = x1+gd, y1+hb
# 	# La méthode coords permet de modifier directement les coordonnées d'un objet
# 	canPP.coords(boule, x1, y1, x1+80, y1+80)

# def depl_gauche():
# 	mvt(-10, 0)

# def depl_droit():
# 	mvt(10, 0)

# def depl_haut():
# 	mvt(0, -10)

# def depl_bas(): 
# 	mvt(0, 10)


# x1, y1 = 10, 10 # Init des coordonnées 
# fen = Tk()
# fen.title("Exemple Animation d'objet") # Titre de la fenêtre 
# # Création du canvas pour l'animation de la boule 
# canPP = Canvas(master=fen, width=300, height=300, bg="grey")
# boule = canPP.create_oval(x1, y1, x1+80, y1+80, width=2, fill='red')
# canPP.grid(row=1, column=2)
# # Création d'un cavas pour la partie commande
# canB = Canvas(master=fen, width=120, height=120)
# canB.grid(row=1, column=1)
# Button(master=canB, text='Quitter', command=fen.quit).grid(row=2, column=0, columnspan=3)
# Button(master=canB, text='Left', command=depl_gauche).grid(row=1, column=0)
# Button(master=canB, text='Up', command=depl_haut).grid(row=0, column=1)
# Button(master=canB, text='Down', command=depl_bas).grid(row=1, column=1)
# Button(master=canB, text='Right', command=depl_droit).grid(row=1, column=2)
# fen.mainloop()

############################# Exercices 7 Astres #############################

# def mvt(n, gd, hb):
# 	global x, y
# 	x[n] += gd
# 	y[n] += hb
# 	# La méthode coords permet de modifier directement les coordonnées d'un objet
# 	canPP.coords(boule[n], x[n], y[n], x[n]+80, y[n]+80)

# def depl_gauche1():
# 	mvt(0, -10, 0)

# def depl_droit1():
# 	mvt(0, 10, 0)

# def depl_haut1():
# 	mvt(0, 0, -10)

# def depl_bas1():
#  	mvt(0, 0, 10)

# def depl_gauche2():
# 	mvt(1, -10, 0)

# def depl_droit2():
# 	mvt(1, 10, 0)

# def depl_haut2():
# 	mvt(1, 0, -10)

# def depl_bas2():
#  	mvt(1, 0, 10)

# # Init des coordonnées
# x = [10, 200]
# y = [10, 200]
# fen = Tk()
# fen.title("Les Astres") # Titre de la fenêtre
# # Création du canvas pour l'animation de la boule
# canPP = Canvas(master=fen, width=300, height=300, bg="grey")
# boule1 = canPP.create_oval(x[0], y[0], x[0]+80, y[0]+80, width=2, fill='red')
# boule2 = canPP.create_oval(x[1], y[1], x[1]+80, y[1]+80, width=2, fill='black')
# boule = [boule1, boule2]
# canPP.grid(row=0, column=1)
# Button(master=fen, text='Quitter', command=fen.quit).grid(row=1, column=0, columnspan=3)
# # Création d'un cavas pour la partie commande de la première boule
# canB1 = Canvas(master=fen, width=120, height=120)
# canB1.grid(row=0, column=0)
# Button(master=canB1, text='Left', command=depl_gauche1).grid(row=1, column=0)
# Button(master=canB1, text='Up', command=depl_haut1).grid(row=0, column=1)
# Button(master=canB1, text='Down', command=depl_bas1).grid(row=1, column=1)
# Button(master=canB1, text='Right', command=depl_droit1).grid(row=1, column=2)
# # Création d'un cavas pour la partie commande de la première boule
# canB2 = Canvas(master=fen, width=120, height=120)
# canB2.grid(row=0, column=2)
# Button(master=canB2, text='Left', command=depl_gauche2).grid(row=1, column=0)
# Button(master=canB2, text='Up', command=depl_haut2).grid(row=0, column=1)
# Button(master=canB2, text='Down', command=depl_bas2).grid(row=1, column=1)
# Button(master=canB2, text='Right', command=depl_droit2).grid(row=1, column=2)
# fen.mainloop()