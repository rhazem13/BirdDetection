from detector import CVDetector
from reader import CVReader
from queue import Queue
import cv2

SENTINEL =object()
queue = Queue()
video_url = 'static/birds.mp4'
output_path = 'static/birds.csv'
cap = cv2.VideoCapture(video_url)
cv_reader = CVReader(cap , queue, SENTINEL )
cv_detector = CVDetector(cap, queue, output_path, SENTINEL)

cv_reader.start()
cv_detector.start()
