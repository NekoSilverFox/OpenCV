import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("./wunder.png")

# 图像平移
rows, cols = img.shape[:2]
print(rows)
print(cols)
M = np.float32([[1, 0, 300], [0, 1, 100]])  # 这个 2x3 的矩阵(平移矩阵)指的是在x轴和y轴上移动的距离
res = cv.warpAffine(img, M, (2 * cols, 2 * rows))  # 最后一个指的是【画布】大小

plt.imshow(res[:, :, ::-1])
plt.show()
