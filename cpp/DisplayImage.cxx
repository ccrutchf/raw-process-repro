#include <libraw/libraw.h>
#include <iostream>
#include <opencv2/opencv.hpp>
#include <fstream>


using namespace cv;
using namespace std;

// void col_to_row_major(ushort *a, ushort *b,)

Mat linearization(Mat I){
    // img[img > 65000] = img.min()

    //Initialize m
    double minVal; 
    double maxVal; 
    Point minLoc; 
    Point maxLoc;

    minMaxLoc( I, &minVal, &maxVal, &minLoc, &maxLoc );

    cout << "min val: " << minVal << endl;
    cout << "max val: " << maxVal << endl;

     // accept only char type matrices
    //CV_Assert(I.depth() == CV_8U);

    int channels = I.channels();
    int nRows = I.rows;
    int nCols = I.cols * channels;
    int g_m;
    int g_s;

    if (I.isContinuous())
    {
    nCols *= nRows;
    nRows = 1;
    }


    int i,j;
    uchar* p;
    for( i = 0; i < nRows; ++i){
    p = I.ptr<uchar>(i);
    for ( j = 0; j < nCols; ++j){
    // p[j] = table[p[j]];
    p[j] = p[j] - minVal;
        }
    }

    minMaxLoc( I, &minVal, &maxVal, &minLoc, &maxLoc );

    for( i = 0; i < nRows; ++i){
    p = I.ptr<uchar>(i);
    for ( j = 0; j < nCols; ++j){
    // p[j] = table[p[j]];
    p[j] = 255 * (p[j]/maxVal);
    cout << sizeof(maxVal) << endl;
        }
    }

    //int* lin_img = ((img - img.min()) * (1/(img.max() - img.min()) * 65535)).astype('uint16')

    minMaxLoc( I, &minVal, &maxVal, &minLoc, &maxLoc );

    cout << "min val: " << minVal << endl;
    cout << "max val: " << maxVal << endl;

    return I;
}

int main(int argc, char** argv )
{

LibRaw iProcessor;
Mat output;
Mat output_norm;
Mat output_bayer;

for(int i = 0; i < 3; i++){
// Open the file and read the metadata
if(i == 0) iProcessor.open_file("P5050051.ORF");
if(i==1) iProcessor.open_file("P5050052.ORF");
if(i==2) iProcessor.open_file("P5050055.ORF");

// Let us unpack the image
iProcessor.unpack();

cv::Mat image(iProcessor.imgdata.rawdata.sizes.raw_height , iProcessor.imgdata.rawdata.sizes.raw_width, CV_16U, iProcessor.imgdata.rawdata.raw_image);

output = linearization(image);
//normalize(image, output, 0, 255, NORM_MINMAX, CV_8U);
cvtColor(output, output, COLOR_BayerGR2BGR);
//resize(output, output, Size(1508, 2007), 0, 0, INTER_NEAREST_EXACT);
imshow("RAW Image", output);

if(i == 0) imwrite("Image-1.png", output);
if(i == 1) imwrite("Image-2.png", output);
if(i == 2) imwrite("Image-3.png", output);


waitKey(0);

}

return 0;

}