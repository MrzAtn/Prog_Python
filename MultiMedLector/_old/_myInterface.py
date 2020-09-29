from tkinter import *
from tkinter.filedialog import *
from video_Obj import myVideo

class myInterface:

    def __init__(self):
        # Init obj
        self.interface = Tk()
        self.video = myVideo()

        self.interface.title("LECTEUR MULTIMEDIA")
        self.can = Canvas(master= self.interface, width=300, height=300)
        self.can.pack()

        # Frame parcours données
        self.frame_d = LabelFrame(self.can, text='Base de donnée', padx=20, pady=20)
        self.frame_d.pack(fill='both', expand='yes')
        path_Label = Label(master=self.frame_d, text='Path : ')
        path_Label.grid(row=0, column=0, sticky=W)
        self.videoPath = Entry(master=self.frame_d) # ajouter ecoute
        self.videoPath.grid(row=0, column=1, columnspan=2)
        Button(master=self.frame_d, text='Search', command=self.searchInFinder).grid(row=0, column=3, padx=10)
        Button(master=self.frame_d, text='Start', command=lambda :  self.video.OpenFile(self.videoPath.get(), True)).grid(row=0, column=4, padx=10)

        # Frame controle
        self.frame_c = LabelFrame(self.can, text='Controle vidéo', padx=20, pady=20)
        self.frame_c.pack(fill='both', expand='yes')
        Button(master=self.frame_c, text='▷', width=4, command= self.video.play).grid(row=0, column=0)
        Button(master=self.frame_c, text='||', width=4, command= self.video.pause).grid(row=0, column=1)
        Button(master=self.frame_c, text='≫', width=4, command= self.video.nextFrame).grid(row=0, column=2)
        Button(master=self.frame_c, text='≪',  width=4, command= self.video.prevFrame).grid(row=0, column=3)
        Button(master=self.frame_c, text='Quitter', command=self.closeInter).grid(row=0, column=4, padx=20)
        
        # Frame Info vidéo
        self.frame_v = LabelFrame(self.can, text='Info Lecture', padx=20, pady=20)
        self.frame_v.pack(fill='both', expand='yes')
        self.frame_Label = Label(master=self.frame_v, text='Frame : 0/0')
        self.frame_Label.grid(row=1, column=0, padx=20)
        self.time_Label = Label(master=self.frame_v, text='Time : 00:00')
        self.time_Label.grid(row=1, column=2, padx=20)

        self.interface.mainloop()
    
    def searchInFinder(self):
        # On recopier le nom du chemin dans la barre blanche
        self.videoPath.insert(0, askopenfilename(title="Ouvrir votre document",filetypes=[('avi files','.avi')]))

    def closeInter(self):
        self.interface.quit()
        self.video.close()

    def affichage(self):
        self.posFrame, total = self.video.getFrame()
        self.frame_Label.configure(text="Frame : {}/{}".format(self.posFrame, total))
        self.time = self.video.getTime()
        self.time_Label.configure(text="Time : {}:{}:{}".format(str(self.time[0]), str(self.time[1]), str(self.time[2])))


if __name__ == '__main__':
    fen = myInterface()