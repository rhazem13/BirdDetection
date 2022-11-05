# Bird Detection using OpenCV2
**A console application that determines the maximum number of any type of bird that appeared in any frame from any video that contains birds and this process based on a model that was trained and designed specifically to perform the process of birds detection, after the detection the result stored in CSV file.**

# Project Files Details
### ◉ static file
Contain the trained model which we used to detect birds, the video which we make detection on it and the result's CSV file.
### ◉ reader.py
Contain a thread which read frames of the video (frame by frame) and make frames ready to detection process.
### ◉ detector.py
Contain a thread which load the trained model and detect birds in each frame of the video then print the max number of birds in console and save it into CSV file.

# Output
![ed5f73ac-efa2-4e3b-a631-373b37e6b65a](https://user-images.githubusercontent.com/58918060/200135295-57dd6883-c96a-4c1d-bee2-6fb63f335376.jpg)
![image](https://user-images.githubusercontent.com/58918060/200135293-e0525581-1bcd-4201-9ffc-30bc7733866c.png)

# License
MIT License

Copyright (c) 2022 Hazem Ragab

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
