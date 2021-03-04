import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("./call.png")

# 绝对尺寸
rows, cols = img.shape[:2]
print(rows)
print(cols)

# 放大图像，使用绝对坐标
res = cv.resize(img, (2 * cols, 2 * rows))
# 打印图像大小
print(res.shape)

# 缩小图像，使用相对坐标
res2 = cv.resize(img, None, fx=0.5, fy=0.5)  # None 代表绝对坐标
# 打印图像大小
print(res2.shape)

cv.imshow("CALL", img)
cv.waitKey(0)