# Bird Detection using OpenCV2
**A console application that determines the maximum number of any type of bird that appeared in any frame from any video that contains birds and this process based on a model that was trained and designed specifically to perform the process of birds detection, after the detection the result stored in CSV file.**

# Project Files Details
### ◉Static File
Contain the trained model which we used to detect birds, the video which we make detection on it and the result's CSV file.
### ◉reader.py
Contain a thread which read frames of the video (frame by frame) and make frames ready to detection process.
### ◉detector.py
Contain a thread which load the trained model and detect birds in each frame of the video then print the max number of birds in console and save it into CSV file.
