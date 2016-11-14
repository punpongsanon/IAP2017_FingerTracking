#include "Camera.h"

#include <opencv2/highgui.hpp>

Camera::Camera(int cameraid)
{
	// Set camera ID
	camera_id = cameraid;

	// Connect to the camera and initialize capture
	camera = cv::VideoCapture(camera_id);
}

Camera::~Camera()
{
	// Release camera
	camera.release();
}

void Camera::Capture(cv::Mat &frame)
{
	// Capture a frame from the 'camera' device
	camera >> frame;

	return;
}