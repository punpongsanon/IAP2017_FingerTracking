#include "FingerTracking.h"

FingerTracking::FingerTracking()
{

}

FingerTracking::~FingerTracking()
{

}

void FingerTracking::Initialize(int minThreshold,
								int maxThershold,
								bool filterByArea,
								int minArea,
								bool filterByCircularity,
								float minCircularity,
								bool filterByConvexity,
								float minConvexity,
								bool filterByIneritia,
								float minInertiaRatio)
{
	params.minThreshold = minThreshold;
	params.maxThreshold = maxThershold;
	params.filterByArea = filterByArea;
	params.minArea = minArea;
	params.filterByCircularity = filterByCircularity;
	params.minCircularity = minCircularity;
	params.filterByConvexity = filterByConvexity;
	params.minConvexity = minConvexity;
	params.filterByInertia = filterByIneritia;
	params.minInertiaRatio = minInertiaRatio;

	blobDetector = cv::SimpleBlobDetector::create(params);

	return;
}