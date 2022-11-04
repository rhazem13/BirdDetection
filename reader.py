import cv2
from threading import *

class CVReader(Thread):
    def __init__(self, cap, path, queue, sentinel):
        super().__init__()
        self.path = path
        self.queue = queue
        self.cap = cap 
        self.sentinel = sentinel

    def read(self):
        cap = self.cap
        ret, frame = cap.read()
        while ret:
            self.queue.put(frame)
            ret, frame = cap.read()
        self.queue.put(self.sentinel)
        self.cap.release()

    def run(self):
        self.read()











