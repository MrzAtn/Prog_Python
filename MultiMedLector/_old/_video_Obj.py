import threading
import cv2
import numpy

class myVideo:

    def __init__(self):
        self.flagRead = False
        self.display = None
        self.number_of_frame = None
        self.nf = False
        self.pf = False


    def OpenFile(self, path, flag):
        self.display = cv2.VideoCapture(path)
        self.flagRead = flag
        self.number_of_frame = self.display.get(cv2.CAP_PROP_FRAME_COUNT)

        # Utilisation obligatoire de fonctions initialisant des thread
        # pour l'ouverture synchronisé de la video et de l'interface
        self.thread_runvid()

    def thread_runvid(self):
        self.my_thread_Vid = threading.Thread(target=self.runVideo)
        self.flagThread = True
        self.my_thread_Vid.start()

    def pause(self):
        self.flagRead = False

    def play(self):
        self.flagRead = True

    def close(self):
        self.flagThread = False

    def nextFrame(self):
        self.pause()
        self.nf =  True

    def prevFrame(self):
        self.pause()
        self.pf = True

    def runVideo(self):
        while self.display.isOpened() and self.flagThread:
            if self.flagRead:
                _, frame = self.display.read()
                self.interface.affichage()
                # Appel de la fonction pour afficher num de la frame
                # self.majPosFrame()
                cv2.imshow('Frame', frame)
                cv2.waitKey(25)
            if self.nf:
                _, frame = self.display.read()
                self.interface.affichage()
                cv2.imshow('Frame', frame)
                cv2.waitKey(25)
                self.nf = False
            if self.pf:
                self.display.set(1, self.display.get(cv2.CAP_PROP_POS_FRAMES)-2)
                _, frame = self.display.read()
                self.interface.affichage()
                cv2.imshow('Frame', frame)
                cv2.waitKey(25)
                self.pf = False
        self.display.release()
        cv2.destroyAllWindows()

    def getFrame(self):
        return str(self.display.get(cv2.CAP_PROP_POS_FRAMES)), str(self.display.get(cv2.CAP_PROP_FRAME_COUNT))

    def getTime(self):
        # s, ms = divmod(self.display.get(cv2.CAP_PROP_POS_MSEC), 1000)
        # min, s = divmod(s, 60)
        ## OU ##
        ms = self.display.get(cv2.CAP_PROP_POS_MSEC)%1000
        s = (self.display.get(cv2.CAP_PROP_POS_MSEC)/1000)%60
        min = (self.display.get(cv2.CAP_PROP_POS_MSEC)/60000)%60

        return (min, s, ms)



