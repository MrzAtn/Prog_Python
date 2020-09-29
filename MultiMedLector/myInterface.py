import tkinter

class myInterface:

    def __init__(self):
        # Init obj
        self.inter = tkinter.Tk()

        self.inter.title("LECTEUR MULTIMEDIA")
        self.can = tkinter.Canvas(master= self.inter, width=300, height=300)
        self.can.pack()

        # Frame parcours données
        self.frame_d = tkinter.LabelFrame(self.can, text='Base de donnée', padx=20, pady=20)
        self.frame_d.pack(fill='both', expand='yes')
        path_Label = tkinter.Label(master=self.frame_d, text='Path : ')
        path_Label.grid(row=0, column=0, sticky=tkinter.W)
        self.videoPath = tkinter.Entry(master=self.frame_d) # ajouter ecoute
        self.videoPath.grid(row=0, column=1, columnspan=2)
        self.searchBtn = tkinter.Button(master=self.frame_d, text='Search')
        self.searchBtn.grid(row=0, column=3, padx=10)
        self.startBtn = tkinter.Button(master=self.frame_d, text='Start')
        self.startBtn.grid(row=0, column=4, padx=10)

        # Frame controle
        self.frame_c = tkinter.LabelFrame(self.can, text='Controle vidéo', padx=20, pady=20)
        self.frame_c.pack(fill='both', expand='yes')
        self.playBtn = tkinter.Button(master=self.frame_c, text='▷', width=4)
        self.playBtn.grid(row=0, column=0)
        self.pauseBtn = tkinter.Button(master=self.frame_c, text='||', width=4)
        self.pauseBtn.grid(row=0, column=1)
        self.nextFrameBtn = tkinter.Button(master=self.frame_c, text='≫', width=4)
        self.nextFrameBtn.grid(row=0, column=2)
        self.prevFrameBtn  = tkinter.Button(master=self.frame_c, text='≪', width=4)
        self.prevFrameBtn.grid(row=0, column=3)
        self.QuitBtn = tkinter.Button(master=self.frame_c, text='Quitter')
        self.QuitBtn.grid(row=0, column=4, padx=20)
        
        # Frame Info vidéo
        self.frame_v = tkinter.LabelFrame(self.can, text='Info Lecture', padx=20, pady=20)
        self.frame_v.pack(fill='both', expand='yes')
        self.frame_Label = tkinter.Label(master=self.frame_v, text='Frame : 0/0')
        self.frame_Label.grid(row=1, column=0, padx=20)
        self.time_Label = tkinter.Label(master=self.frame_v, text='Time : 00:00')
        self.time_Label.grid(row=1, column=2, padx=20)