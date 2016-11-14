#pragma once
#include <opencv2/core.hpp>
#include <opencv2/imgproc.hpp>
#include <opencv2/features2d.hpp>

class FingerTracking
{
	public:
		FingerTracking();
		~FingerTracking();

		void Initialize(int minThreshold, 
						   int maxThershold, 
						   bool filterByArea, 
						   int minArea, 
						   bool filterByCircularity,
						   float minCircularity, 
						   bool filterByConvexity, 
						   float minConvexity, 
						   bool filterByIneritia, 
						   float minInertiaRatio);

	private:
		cv::Ptr<cv::SimpleBlobDetector> blobDetector;
		cv::SimpleBlobDetector::Params params;
};