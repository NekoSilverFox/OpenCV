#include "mainwindow.h"

#include <QApplication>

#include "opencv2/opencv.hpp"

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    MainWindow w;
    w.show();

//    using namespace cv;
    cv::Mat image = cv::imread("/Users/fox/雪狸的文件/Programma/OpenCV/fox.png");
    imshow("Output", image);

    return a.exec();
}
