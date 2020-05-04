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

# def ligne_carre(x, y):
#     global side 
#     i = 0
#     while i<5:
#         can.create_rectangle(x+i*60, y, x+i*60+side, y+side, fill='black')
#         i += 1

# def initDamier():
#     global side
#     y = 0
#     while y < 10: # Ligne i
#         if y%2: 
#             x = 0
#             # On construit notre damier ligne par ligne
#             ligne_carre(x*side, y*side)

#         else: 
#             x = 1
#             ligne_carre(x*side, y*side)
#         y += 1

# def cercle(x, y, r): # Definition d'une méthode permettant le tracé d'un cercle à partir de son centre
#     can.create_oval(x-r, y-r, x+r, y+r, outline='red', width='2')  

# def placerPion():
#     global side
#     x = side*randrange(10) + side/2
#     y = side*randrange(10) + side/2
#     print(x, y)
#     cercle(x, y, 10)


# side = 30
# fen = Tk()
# can = Canvas(master=fen, bg='white', height=300, width=300)
# can.pack(side=TOP)
# b1 = Button(master=fen,text="Quitter", command=fen.quit)
# b1.pack(side=LEFT, pady=3)
# b2 = Button(master=fen,text="Init Damier", command=initDamier)
# b2.pack(side=RIGHT, pady=3)
# b3 = Button(master=fen,text="Pion", command=placerPion)
# b3.pack(side=RIGHT, pady=3)
# fen.mainloop()

############################# Exercices 4 Repare clic #############################

# def cercle(x, y, r):
#     can.create_oval(x-r, y-r, x+r, y+r, outline='red', width='2')  

# def cliqueur(event): # Argument "event" spécifie que la fonction est lié à un évènement type 'Button-1' 
#     chaine.configure(text='CLic détécté au coordonnées: X=' + str(event.x) +', Y='+ str(event.y))
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

