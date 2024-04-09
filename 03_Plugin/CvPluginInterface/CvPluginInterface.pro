QT = core

CONFIG += c++17 cmdline

# You can make your code fail to compile if it uses deprecated APIs.
# In order to do so, uncomment the following line.
#DEFINES += QT_DISABLE_DEPRECATED_BEFORE=0x060000    # disables all the APIs deprecated before Qt 6.0.0

SOURCES += \
        main.cpp

# Default rules for deployment.
qnx: target.path = /tmp/$${TARGET}/bin
else: unix:!android: target.path = /opt/$${TARGET}/bin
!isEmpty(target.path): INSTALLS += target

HEADERS += \
    CvPluginInterface.h

win32: {
   include("c:/dev/opencv/opencv.pri")
}

unix: !macx {
   CONFIG += link_pkgconfig
   PKGCONFIG += opencv
}

unix: macx {
  include(/Users/fox/AppInstall/opencv-4.9.0/build/opencv.pri)
  INCLUDEPATH += "/usr/local/include"
  LIBS += -L"/usr/local/lib" \
   -lopencv_world
}
