#ifndef BUOY_H
#define BUOY_H

//#include <ros/ros.h>
//#include <image_transport/image_transport.h>
//#include <cv_bridge/cv_bridge.h>
//#include <actionmsg/buoyAction.h>
//#include <actionlib/server/simple_action_server.h>
#include <opencv/cv.h>
#include <opencv/cxcore.h>
#include <opencv/highgui.h>
#include <iostream>
#include <fstream>


using namespace std;
using namespace cv;

bool drawing = false;
std::vector<cv::Point> blob;
std::vector<cv::Vec3b> Pixels;
Mat img, img2;
Mat img3;
std::string getImageType(int number)
{
	// find type
	int imgTypeInt = number%8;
	std::string imgTypeString;

	switch (imgTypeInt)
	{
		case 0:
			imgTypeString = "8U";
			break;
		case 1:
			imgTypeString = "8S";
			break;
		case 2:
			imgTypeString = "16U";
			break;
		case 3:
			imgTypeString = "16S";
			break;
		case 4:
			imgTypeString = "32S";
			break;
		case 5:
			imgTypeString = "32F";
			break;
		case 6:
			imgTypeString = "64F";
			break;
		default:
			break;
	}

	// find channel
	int channel = (number/8) + 1;

	std::stringstream type;
	type<<"CV_"<<imgTypeString<<"C"<<channel;

	return type.str();
}

void CallBackFunc(int event, int x, int y, int flags, void* userdata)
{
	Point mp;
	mp.x = x;
	mp.y = y;
	if  ( event == EVENT_LBUTTONDOWN )
	{
		drawing = true;
		// cout << "Left button of the mouse is clicked - position (" << x << ", " << y << ")" << endl;
		cv::Vec3b pix = img.at<cv::Vec3b>(y,x);
		// int a = pix.val[0];
		// int b = pix.val[1];
		// int c = pix.val[2];
		// img3.at<cv::Vec3b>(y,x) = img.at<cv::Vec3b>(y,x);
		// circle(img3,mp,15,Scalar(a,b,c),-1);
		circle(img2, mp, 5, Scalar(0,0,255), -1);
		// cout << static_cast<float>(pix[0])<<" "<<static_cast<float>(pix[1])<<" "<<static_cast<float>(pix[2])<<endl;
		if (!(std::find(blob.begin(), blob.end(), mp) != blob.end()))
		{
			blob.push_back(mp);
			Pixels.push_back(pix);       	
		}
	}
	else if ( event == EVENT_MOUSEMOVE )
	{
		if (drawing == true)
		{
			cv::Vec3b pix = img.at<cv::Vec3b>(y,x);
			// img3.at<cv::Vec3b>(y,x) = img.at<cv::Vec3b>(y,x);
			circle(img2, mp, 5, Scalar(0,0,255), -1);

			// cout << pix.val[0]
			// 		<<" "<<pix.val[1]
			// 		<<" "<<pix.val[2]<<endl;

			if (!(std::find(blob.begin(), blob.end(), mp) != blob.end()))
			{
				Pixels.push_back(pix);       	
				blob.push_back(mp);        	
			}
		}
	}    
	else if  ( event == EVENT_LBUTTONUP )
	{
		drawing = false;
		cout << "done drawing - position (" << x << ", " << y << ")" << endl;
	}
	imshow("draw", img2);
	// imshow("draw2", img3);
	waitKey(0);
}

int main(int argc, char ** argv)
{
	// Write all the training data to the file
	ofstream file;

	if (argc < 3) {
		printf("You need to enter video path as first arg and text file name as second arg");
		return 0;
	}

	file.open(argv[2], std::ios_base::app);
	VideoCapture cap(argv[1]);

	if(!cap.isOpened())  // check if we succeeded

		return -1;

	namedWindow("ImageDisplay", 1);
	setMouseCallback("ImageDisplay", CallBackFunc, NULL);

	while(1)
	{
		cap >> img;
		img2 = img.clone();
		imshow("ImageDisplay", img);
		long long int a;
		a = waitKey(33);
		//cout << a << endl;
		// on pressing the escape key write all the pixels in the array
		// to the file buffer.
		if (a%256==27)
		{
			cout << blob.size() << endl;
			cout << Pixels.size() << endl;
			for (int i = 0; i < Pixels.size(); ++i)
			{
				cv::Vec3b pix = Pixels[i];
				file<<static_cast<int>(pix.val[0])<<" "
					<<static_cast<int>(pix.val[1])<<" "
					<<static_cast<int>(pix.val[2])<<endl;
				cout<<static_cast<int>(pix.val[0])<<" "
					<<static_cast<int>(pix.val[1])<<" "
					<<static_cast<int>(pix.val[2])<<endl;
			}
			blob.clear();
			Pixels.clear();
			continue;
		}
		// on pressing the tab key stop the video
		else if (a%256==9)
		{
			break;
		}
	}
	file.close();
	return 0;

}
#endif BUOY_H
