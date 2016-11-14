#include "Camera.h"
#include "FingerTracking.h"

// Global variables
Camera* camera;
FingerTracking* tracking;

int threshold = 0;

void Trackbars()
{
	cv::createTrackbar("Threshold", "Tracking", &threshold, 255);
}

void main()
{
	cv::Mat frame_rgb;
	cv::Mat frame_grey;

	camera = new Camera(0);
	tracking = new FingerTracking();

	// Create a window to display a captured frame
	cv::namedWindow("Captured", CV_WINDOW_KEEPRATIO);

	while (true)
	{
		// Capture an image
		camera->Capture(frame_rgb);
		// Convert a captured color image to grayscale image
		frame_rgb.convertTo(frame_grey, CV_BGR2GRAY);
		// To do: add the detection and tracking process
		// Follows https://www.learnopencv.com/blob-detection-using-opencv-python-c/
	}

	return;
}