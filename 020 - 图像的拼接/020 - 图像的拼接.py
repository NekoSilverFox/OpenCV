# 020 - 图像的拼接
import cv2 as cv
import numpy as np

img1 = cv.imread("./input1.jpg")
img2 = cv.imread("./input2.jpg")

imgHor = np.hstack((img1, img2))  # 水平拼接
imgVer = np.vstack((img1, img2))  # 垂直拼接

cv.imshow("水平", imgHor)
cv.imshow("垂直", imgVer)

cv.waitKey(0)