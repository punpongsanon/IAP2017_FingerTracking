# IAP-2017_MIT_CSAIL-HCIE

import cv2
import numpy as np

def nothing(x):
    pass
 
# Camera 0 is the integrated web cam on a netbook or the one with USB cable (Camera 1)
camera_port = 1
 
#Number of frames to throw away while the camera adjusts to light levels
ramp_frames = 30
 
# Now we can initialize the camera capture object with the cv2.VideoCapture class.
# All it needs is the index to a camera port.
camera = cv2.VideoCapture(camera_port)
 
# Create trackbar for the interface
cv2.namedWindow('trackbar window')
cv2.createTrackbar('H min','trackbar window',0,255,nothing)
cv2.createTrackbar('H max','trackbar window',0,255,nothing)
cv2.createTrackbar('S min','trackbar window',0,255,nothing)
cv2.createTrackbar('S max','trackbar window',0,255,nothing)
cv2.createTrackbar('V min','trackbar window',0,255,nothing)
cv2.createTrackbar('V max','trackbar window',0,255,nothing)
print 'created trackbars'

# define default range
cv2.setTrackbarPos('H min','trackbar window', 50)
cv2.setTrackbarPos('H max','trackbar window', 110)
cv2.setTrackbarPos('S min','trackbar window', 50)
cv2.setTrackbarPos('S max','trackbar window', 255)
cv2.setTrackbarPos('V min','trackbar window', 180)
cv2.setTrackbarPos('V max','trackbar window', 255)

while(True):
    # Capture frame-by-frame
    ret, frame = camera.read()
	
	# convert rgb to hsv
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos('H min','trackbar window')
    h_max = cv2.getTrackbarPos('H max','trackbar window')
    s_min = cv2.getTrackbarPos('S min','trackbar window')
    s_max = cv2.getTrackbarPos('S max','trackbar window')
    v_min = cv2.getTrackbarPos('V min','trackbar window')
    v_max = cv2.getTrackbarPos('V max','trackbar window')
	
	# define range with sliders default or update on time
    lower_green = np.array([h_min,s_min,v_min])
    upper_green = np.array([h_max,s_max,v_max])
	
	# threshold the HSV image to get only green colors
    threshold = cv2.inRange(hsv, lower_green, upper_green)
	
	#find contours
    contours, hierarchy = cv2.findContours(threshold,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    #check contour size
    for contour in contours:
    	area = cv2.contourArea(contour)
    	if area > 1000:
   			cv2.drawContours(frame, contour, -1, (0,255,0), 3)     		#draw contours in image
   			(x,y),radius = cv2.minEnclosingCircle(contour)
			center = (int(x),int(y))
			radius = int(5)
			cv2.circle(frame,center,radius,(0,255,0),2)
			textstring = '(' + str(int(x)) + ', ' + str(int(y)) + ')'
			cv2.putText(frame,textstring,(int(x+50),int(y)), cv2.FONT_HERSHEY_SIMPLEX, 0.5,(255,255,255),1)

    cv2.imshow('trackbar window',frame)

    # Display the resulting frame
    cv2.imshow('hsv',hsv)
	
    if cv2.waitKey(200) & 0xFF == ord('q'):
        break
 
# When everything done, release the capture
cv2.destroyAllWindows()
 
# You'll want to release the camera, otherwise you won't be able to create a new
# capture object until your script exits
del(camera)
