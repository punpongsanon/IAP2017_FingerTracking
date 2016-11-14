#pragma once
#include<opencv2/opencv.hpp>

class Camera
{
	public:
		Camera(int cameraid);
		~Camera();

		void Capture(cv::Mat &frame);

	private:
		cv::VideoCapture camera;
		int camera_id;
};