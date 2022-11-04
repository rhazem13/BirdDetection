import cv2
from threading import *

class CVReader(Thread):
    def __init__(self, path, queue, sentinel):
        super().__init__()
        self.path = path
        self.queue = queue
        self.cap = cv2.VideoCapture(path)
        self.sentinel = sentinel

    def read(self):
        ret = True
        cap = self.cap
        while ret:
            ret, frame = cap.read()
            self.queue.put(frame)
        self.queue.put(self.sentinel)
        print('sentinel value is ', self.sentinel)
        self.cap.release()

    def run(self):
        self.read()











