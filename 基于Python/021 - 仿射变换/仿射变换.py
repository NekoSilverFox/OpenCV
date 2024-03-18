# 仿射变换
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("./call.png")
pts1 = np.float32([[50, 50], [200, 50], [50, 200]])
pts2 = np.float32([[100, 100], [200, 50], [100, 250]])

M = cv.getAffineTransform(pts1, pts2)
print(M)

res = cv.warpAffine(img, M, img.shape[:2])
plt.imshow(res[:, :, ::])
plt.show()
