import cv2
import pandas as pd
from threading import *

class CVDetector(Thread):
    def __init__(self, queue, path, sentinel):
        super().__init__()
        self.queue = queue
        self.sentinel = sentinel
        self.MAX_NUM_BIRDS = 0
        self.path = path
        self.birdsCascade = cv2.CascadeClassifier("static/birds1.xml")

    def process(self):
        frame = self.queue.get()
        while frame is not self.sentinel:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            birds = self.birdsCascade.detectMultiScale(
                gray,
                scaleFactor=1.4,
                minNeighbors=2,
                #minSize=(10, 10),
                maxSize=(30, 30),
                flags = cv2.CASCADE_SCALE_IMAGE
            )
            if (len(birds)>=self.MAX_NUM_BIRDS):
                self.MAX_NUM_BIRDS = len(birds)
            frame = self.queue.get()
        print('max number is: ',self.MAX_NUM_BIRDS)
        data = {str(self.MAX_NUM_BIRDS)}
        df = pd.DataFrame(data, columns=['Max Num Of Birds'])
        df.to_csv('static/birds.csv', index=False)

    def run(self):
        self.process()