import cv2
import math
from threading import *

class CVReader(Thread):
    def __init__(self, cap, queue, sentinel):
        super().__init__()
        self.queue = queue
        self.cap = cap 
        self.sentinel = sentinel
    

    def getStats(self):
        
        fps = self.cap.get(cv2.CAP_PROP_FPS)
       
        frame_count = int(self.cap.get(cv2.CAP_PROP_FRAME_COUNT))
        
        #https://docs.opencv.org/3.4/d4/d15/group__videoio__flags__base.html
        codec = self.cap.get(cv2.CAP_PROP_FOURCC)
        #total duraiton of video in milli seconds
        durationSec = frame_count/fps * 1000
        return (fps,frame_count,durationSec)

    def read(self):
        (fps,frame_count,durationSec) = self.getStats()
        print ("Total time: {}sec FrameRate: {} FrameCount: {}".format(durationSec, fps, frame_count))
        cap = self.cap
        ret, frame = cap.read()
        while ret:
            self.queue.put(frame)
            ret, frame = cap.read()
        self.queue.put(self.sentinel)
        self.cap.release()

    def run(self):
        self.read()











