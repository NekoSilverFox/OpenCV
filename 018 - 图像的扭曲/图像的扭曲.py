# 图像的扭曲
import cv2 as cv
import numpy as np

img = cv.imread("./input.jpg")

width, height = 600, 900
#                     左上         右上         左下          右下
pts1 = np.float32([[550, 255], [900, 165], [800, 690], [1240, 520]])
pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
matrix = cv.getPerspectiveTransform(pts1, pts2)
imgOutput = cv.warpPerspective(img, matrix, (width, height))

cv.imshow("input", img)
cv.imshow("output", imgOutput)
cv.waitKey(0)

