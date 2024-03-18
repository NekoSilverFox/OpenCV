# 019 - 图像的旋转
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("./call.png")

rows, cols = img.shape[:2]

# 图像的旋转                       旋转中心   旋转角度↓   ↓缩放比例
M = cv.getRotationMatrix2D((cols / 2, rows / 2), 45, 1)  # 旋转矩阵

res = cv.warpAffine(img, M, (cols, rows))  # 最后一个参数是缩放比例

plt.imshow(res[:, :, ::-1])
plt.show()
