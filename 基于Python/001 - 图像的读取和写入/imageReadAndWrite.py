import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

# 读取图像
img = cv.imread("./call.png", 0)  # 1 代表彩色通道（不包含透明）；0表示灰度；-1表示彩色包含透明

# OpenCV 显示图像
# cv.imshow("CALL", img)
# cv.waitKey(0)
# cv.destroyAllWindows()

# matplotlib 显示图像
plt.imshow(img[:, :, ::-1])
plt.show()

# 图像的保存
cv.imwrite("new_call.png", img)
