# 050 - 色彩追踪（追踪栏）
import cv2 as cv
import numpy as np


def empty(A):
    pass


def stackImages(scale, imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range(0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape[:2]:
                    imgArray[x][y] = cv.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None,
                                               scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y] = cv.cvtColor(imgArray[x][y], cv.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank] * rows
        hor_con = [imageBlank] * rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None, scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv.cvtColor(imgArray[x], cv.COLOR_GRAY2BGR)
        hor = np.hstack(imgArray)
        ver = hor
    return ver


def InitCanvas(width, height, color=(255, 255, 255)):
    canvas = np.ones((height, width, 3), dtype="uint8")
    canvas[:] = color
    return canvas

def get_odd(num):
    if num % 2 == 0:
        num += 1
    return num

# 跟踪杆
cv.namedWindow("TrackBars")
cv.resizeWindow("TrackBars", 640, 240)

cv.createTrackbar("R", "TrackBars", 0, 255, empty)
cv.createTrackbar("G", "TrackBars", 0, 255, empty)
cv.createTrackbar("B", "TrackBars", 0, 255, empty)
cv.createTrackbar("Blur", "TrackBars", 0, 255, empty)

cam = cv.VideoCapture(2)  # 这里的数字代表摄像头ID，如果有多个摄像头，请尝试更改这些ID
# 设置摄像头的大小
cam.set(3, 640)  # 第一个参数`3`代表 `宽度`
cam.set(4, 480)  # 第一个参数`4`代表 `高度`

while True:
    success, img = cam.read()

    R = cv.getTrackbarPos("R", "TrackBars")
    G = cv.getTrackbarPos("G", "TrackBars")
    B = cv.getTrackbarPos("B", "TrackBars")
    Blur = cv.getTrackbarPos("Blur", "TrackBars")
    print(R, G, B, Blur)

    mask_img = InitCanvas(640, 480, color=(B, G, R))
    img_res = cv.addWeighted(img, 1, mask_img, 0.5, 0)
    val_blur = get_odd(Blur)
    img_blur = cv.GaussianBlur(img, (val_blur, val_blur), 0)

    imgStack = stackImages(0.6, ([img, mask_img, img_res, img_blur]))
    cv.imshow("Stack images", imgStack)
    cv.waitKey(1)
