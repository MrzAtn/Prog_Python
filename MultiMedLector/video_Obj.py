import cv2

class myVideo:

    def __init__(self):
        self.flagRead = False
        self.display = None
        self.nf = False
        self.pf = False


    def pause(self, *args):
        self.flagRead = False

    def play(self, *args):
        self.flagRead = True

    def nextFrame(self, *args):
        self.pause()
        self.nf = True

    def prevFrame(self, *args):
        self.pause()
        self.pf = True

    def getFrame(self, *args):
        return str(self.display.get(cv2.CAP_PROP_POS_FRAMES)), str(self.display.get(cv2.CAP_PROP_FRAME_COUNT))

    def getTime(self, *args):
        # s, ms = divmod(self.display.get(cv2.CAP_PROP_POS_MSEC), 1000)
        # min, s = divmod(s, 60)
        ## OU ##
        ms = int(self.display.get(cv2.CAP_PROP_POS_MSEC)%1000)
        s = int((self.display.get(cv2.CAP_PROP_POS_MSEC)/1000)%60)
        min = int((self.display.get(cv2.CAP_PROP_POS_MSEC)/60000)%60)
        return (min, s, ms)



