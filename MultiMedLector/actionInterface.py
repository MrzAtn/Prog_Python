from myInterface import myInterface
from video_Obj import  myVideo
import cv2
import threading
from tkinter.filedialog import *

class ActionInterface:

    def __init__(self):
        self.interface = myInterface()
        self.video = myVideo()

        # Init actions Btn
        self.interface.playBtn.bind("<Button-1>", self.video.play)
        self.interface.pauseBtn.bind("<Button-1>", self.video.pause)
        self.interface.prevFrameBtn.bind("<Button-1>", self.video.prevFrame)
        self.interface.nextFrameBtn.bind("<Button-1>", self.video.nextFrame)
        self.interface.searchBtn.bind("<Button-1>", self.searchInFinder)
        self.interface.QuitBtn.bind("<Button-1>", self.closeInter)
        self.interface.startBtn.bind("<Button-1>", lambda x:  self.OpenFile(self.interface.videoPath.get(), True))
        self.interface.inter.mainloop()

    def searchInFinder(self, *args):
        self.interface.videoPath.delete(0, END)
        # On recopier le nom du chemin dans la barre blanche
        self.interface.videoPath.insert(0, askopenfilename(title="Ouvrir votre document",filetypes=[('avi files','.avi')]))

    def OpenFile(self, path, flag):
        self.flagThread = False
        self.video.display = cv2.VideoCapture(path)
        self.video.flagRead = flag
        self.video.number_of_frame = self.video.display.get(cv2.CAP_PROP_FRAME_COUNT)

        # Utilisation obligatoire de fonctions initialisant des thread
        # pour l'ouverture synchronisé de la video et de l'interface
        self.my_thread_Vid = threading.Thread(target=self.runVideo)
        self.flagThread = True
        self.my_thread_Vid.start()

    def closeInter(self, *args):
        self.interface.inter.quit()
        self.flagThread = False

    def runVideo(self, *args):
        while self.video.display.isOpened() and self.flagThread:
            if self.video.flagRead:
                _, frame = self.video.display.read()
                self.affichage()
                cv2.imshow('Frame', frame)
                cv2.waitKey(25)
            if self.video.nf:
                _, frame = self.video.display.read()
                self.affichage()
                cv2.imshow('Frame', frame)
                cv2.waitKey(25)
                self.video.nf = False
            if self.video.pf:
                self.video.display.set(1, self.video.display.get(cv2.CAP_PROP_POS_FRAMES)-2)
                _, frame = self.video.display.read()
                self.affichage()
                cv2.imshow('Frame', frame)
                cv2.waitKey(25)
                self.video.pf = False
        self.video.display.release()
        cv2.destroyAllWindows()

    def affichage(self, *args):
        self.posFrame, total = self.video.getFrame()
        self.interface.frame_Label.configure(text="Frame : {}/{}".format(self.posFrame, total))
        self.time = self.video.getTime()
        self.interface.time_Label.configure(text="Time : {}:{}:{}".format(str(self.time[0]), str(self.time[1]), str(self.time[2])))