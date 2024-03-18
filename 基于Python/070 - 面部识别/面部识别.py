import cv2 as cv
import numpy as np

# 添加级联
faceCascade = cv.CascadeClassifier("./haarcascade_frontalface_default.xml")

img = cv.imread("./peoples.jpg")
imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)

# 框
for (x, y, w, h) in faces:
    cv.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)

cv.imshow("People", img)
cv.waitKey(0)
