import cv2
import pandas as pd
#cap = cv2.VideoCapture(0) #for automatic USBCam (0-web cam default)

class DetectBirds(object):
    def __init__(self, camera_url):
        self.cap = cv2.VideoCapture(camera_url)
        self.birdsCascade = cv2.CascadeClassifier("static/birds1.xml")
        self.MAX_NUM_BIRDS = 0
        self.running = True

    def detect(self):
        while self.running:
            # Capture frame-by-frame from a video
            ret, frame = self.cap.read()
            if ret:
                # convert the frame into gray scale for better analysis
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                # Detect birds in the gray scale image
                birds = self.birdsCascade.detectMultiScale(
                    gray,
                    scaleFactor=1.4,
                    minNeighbors=5,
                    #minSize=(10, 10),
                    maxSize=(30, 30),
                    flags = cv2.CASCADE_SCALE_IMAGE
                )
                if (len(birds)>=self.MAX_NUM_BIRDS):
                    self.MAX_NUM_BIRDS = len(birds)
                

                

                #if  & 0xFF == ord('q'):
                    #self.running = False
            else:
                self.running = False
            
        print("Detected {0} Birds".format(self.MAX_NUM_BIRDS))
        data = {str(self.MAX_NUM_BIRDS)}
        df = pd.DataFrame(data, columns=['Max Num Of Birds'])
        df.to_csv('static/birds.csv', index=False)
        

        

        # When everything done, release the capture and go back take another one
        self.cap.release()
        #cv2.destroyAllWindows()

# Create the haar cascade that reads the properties of objects to be detected from an already made xml file.
# The xml file is generated as a result of machine learning from all possible object samples provided.


if __name__ == "__main__":
    D = DetectBirds("static/birds.mp4")
    D.detect()
