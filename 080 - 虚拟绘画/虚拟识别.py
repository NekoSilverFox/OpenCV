import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from stackImages import stackImages

CAM_WIDTH = 640
CAM_HEIGHT = 480
CAM_BRIGHTNESS = 150


def empty(A):
    pass


def findColor():
    cam = cv.VideoCapture(2)  # 这里的数字代表摄像头ID，如果有多个摄像头，请尝试更改这些ID

    # 设置摄像头的大小
    cam.set(3, CAM_WIDTH)  # 第一个参数`3`代表 `宽度`
    cam.set(4, CAM_HEIGHT)  # 第一个参数`4`代表 `高度`
    cam.set(10, CAM_BRIGHTNESS)  # 第一个参数`10`代表 `亮度`

    # 跟踪杆
    cv.namedWindow("TrackBars")
    cv.resizeWindow("TrackBars", CAM_WIDTH, CAM_HEIGHT)
    cv.createTrackbar("Hue Min", "TrackBars", 0, 179, empty)
    cv.createTrackbar("Hue Max", "TrackBars", 179, 179, empty)

    cv.createTrackbar("Sat Min", "TrackBars", 0, 255, empty)
    cv.createTrackbar("Sat Max", "TrackBars", 255, 255, empty)

    cv.createTrackbar("Val Min", "TrackBars", 0, 255, empty)
    cv.createTrackbar("Val Max", "TrackBars", 255, 255, empty)

    #############################################################

    while True:
        success, img = cam.read()
        imgHSV = cv.cvtColor(img, cv.COLOR_BGR2HSV)
        h_min = cv.getTrackbarPos("Hue Min", "TrackBars")
        h_max = cv.getTrackbarPos("Hue Max", "TrackBars")

        s_min = cv.getTrackbarPos("Sat Min", "TrackBars")
        s_max = cv.getTrackbarPos("Sat Max", "TrackBars")

        v_min = cv.getTrackbarPos("Val Min", "TrackBars")
        v_max = cv.getTrackbarPos("Val Max", "TrackBars")
        print(h_min, h_max, s_min, s_max, v_min, v_max)

        lower = np.array([h_min, s_min, v_min])
        upper = np.array([h_max, s_max, v_max])
        mask = cv.inRange(imgHSV, lower, upper)
        # 将我们不需要的颜色设为黑色，需要的设为白色

        imgResult = cv.bitwise_and(img, img, mask=mask)
        imgStack = stackImages(0.6, ([img, mask, imgResult]))
        cv.imshow("Stack images", imgStack)
        cv.waitKey(1)


def find_color(img_input, myColors):
    imgHSV = cv.cvtColor(img_input, cv.COLOR_BGR2HSV)
    lower = np.array(myColors[0][0:3])
    upper = np.array(myColors[0][3:6])
    mask = cv.inRange(imgHSV, lower, upper)
    print(mask)
    # 将我们不需要的颜色设为黑色，需要的设为白色
    cv.imshow("img", mask)


cam = cv.VideoCapture(2)  # 这里的数字代表摄像头ID，如果有多个摄像头，请尝试更改这些ID
# 设置摄像头的大小
cam.set(3, CAM_WIDTH)  # 第一个参数`3`代表 `宽度`
cam.set(4, CAM_HEIGHT)  # 第一个参数`4`代表 `高度`
cam.set(10, CAM_BRIGHTNESS)  # 第一个参数`10`代表 `亮度`

myColors = [[127, 179, 99, 255, 25, 255],
            [82, 159, 104, 255, 48, 255],  # Red
            [106, 156, 58, 255, 99, 255]]  # peper

findColor()

while True:
    success, img = cam.read()
    find_color(img, myColors)
    cv.imshow("Res cam", img)
    # plt.imshow(img[:, :, ::-1])
    # plt.show()

    if cv.waitKey(1) & 0xFF == ord('q'):
        break
