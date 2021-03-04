import cv2 as cv
import numpy as np

cam = cv.VideoCapture(2)

# 设置摄像头大小
cam.set(3, 1280)  # 第一个参数`3`代表 `宽度`
cam.set(4, 720)  # 第一个参数`4`代表 `高度`

# 添加级联
faceCascade = cv.CascadeClassifier("./haarcascade_frontalface_default.xml")

while True:
    success, img = cam.read()
    imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    face = faceCascade.detectMultiScale(imgGray, 1.1, 4)
    for (x, y, w, h) in face:
        cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv.imshow("Video Cam", img)

    # 以便打破循环
    if cv.waitKey(1) & 0xFF == ord('q'):
        break