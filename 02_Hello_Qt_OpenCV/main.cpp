#include "hello_qt_opencv.h"
#include "opencv2/opencv.hpp"

#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);

    Hello_Qt_OpenCV w;
    w.show();

    return a.exec();
}
