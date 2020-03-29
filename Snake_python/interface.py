"""
@CopyRight: Come down Bro
@Description: fileContent
@Author: Antonin Marzelle
@Date: 2019-08-04 15:45:34
"""
from tkinter import *


class Interface:

    def __init__(self):
        self.fe = Tk()


    def quit_Wind(self):
        fen = Tk()
        fen.title("Quit")
        test_I = Label(fen, text="Êtes vous sûr de vouloir quitter ?")
        b_yes = Button(fen, test="Yes", command=self.fe.destroy)
        b_no = Button(fen, text="No", command=fen.destroy)
        test_I.pack()
        b_yes.pack()
        b_no.pack()
        fen.mainloop()

    def myInterface(self):
        self.fe.title("RED SNAKE")
        label = Label(self.fe, text="Bienvenue dans Snake")
        b_play = Button(self.fe, text="Jouer")
        b_close = Button(self.fe, text="Quitter", command=self.fe.quit)
        fond = PhotoImage(file="/Users/antoninmarzelle/Documents/Programmation/ProG_PY/Snake_python/111.png")
        canvas = Canvas(self.fe, width=fond.width(), height=fond.height())
        canvas.create_image(0, 0, anchor=NW, image=fond)
        canvas.pack()
        label.pack()
        b_play.pack()
        b_close.pack()
        self.fe.mainloop()