import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

img1 = cv.imread("./69.png")
img2 = cv.imread("./70.png")

# 图像的混合
img3 = cv.addWeighted(img2, 0.9, img1, 0.5, 0)  # 最后一个是伽马值

plt.imshow(img3[:, :, ::-1])
plt.show()
