# IAP2017: Build your own Multi-Touch Pad

Learn laser cutting, electronics breadboard prototyping, soldering, and computer vision in only two afternoons. In this hands-on IAP, we will build a multi-touch pad using the principles of FTIR (Frustrated Total Internal Reflection).

This code is the part of Session #2: Finger tracking (Jan 20, 2017). 
In the second session, you will use computer vision to track finger gestures on your multi-touch pad using the attached camera. 
For this, we will give an intro to computer vision with OpenCV (color-space conversions, thresholding, blob detection). 
At the end, we will host a contest for the best example application with some unique prizes for the most creative solutions.

__Pre-requirement:__

* We run all this example in 'python version' of OpenCV. 
- [OpenCV 2.4.13](http://opencv.org/downloads.html)
- [Python 2.7.x](https://www.python.org/downloads/)
- Numpy, please run with 'pip install numpy'

__Install:__ 

1.	After install the OpenCV, by default it could going to c:/OpenCV/
2.	Simply, move cv2.pyd from c:/opencv/build/python/2.7/x86 to c:/python27/Lib/site-packages
*Note: we use x86/cv2.pyd when we use python x86 (32-bit), otherwise, you will get the error when running the test*

__Test:__

1.	Open Python IDE or Command-line
2.	Type: ‘import cv2’ <enter> and ‘Print cv2.__version__’
3.	The version of OpenCV should appears ‘2.4.13’

For the course details: http://groups.csail.mit.edu/hcie/iap-multitouch-pad.html

(C) 2017 MIT CSAIL-HCIE
