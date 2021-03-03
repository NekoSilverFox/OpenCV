# 007 - 色彩空间的改变
import matplotlib.pyplot as plt
import numpy as np
import cv2 as cv

img = cv.imread("./call.png")

# 色度的转换有150+种方法，但是常用的只有：BGR->灰度 和 BGR->HSV
# BGR -> GRAY
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
plt.imshow(gray_img, cmap=plt.cm.gray)
plt.show()

# BGR -> HSV
hsv_img = cv.cvtColor(img, cv.COLOR_BGR2HSV)
plt.imshow(hsv_img[:, :, ::-1])
plt.show()

