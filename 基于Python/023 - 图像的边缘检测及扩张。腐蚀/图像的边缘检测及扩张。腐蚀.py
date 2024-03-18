import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread("./call.png")

############################## 图像边缘检测 ##############################
kernel = np.ones((5, 5), np.uint8)  # uint8 代表 unsigned int 无符号的整型，8位（可表示色彩为 0 ~ 255）

#                        阈值
imgCanny = cv.Canny(img, 100, 100)
cv.imshow("Canny 100 100", imgCanny)

# 如果想减少边缘的数量，就增加值
#                        阈值
imgCanny = cv.Canny(img, 200, 100)
cv.imshow("Canny 200 100", imgCanny)

# 如果想减少边缘的数量，就增加值
#                        阈值
imgCanny = cv.Canny(img, 900, 100)
cv.imshow("Canny 900 100", imgCanny)

############################## 扩张图像？ ##############################
imgDialation = cv.dilate(imgCanny, kernel, iterations=1)
cv.imshow("Dialation img", imgDialation)

############################## 腐蚀 ##############################
imgEroded = cv.erode(imgDialation, kernel, iterations=1)
cv.imshow("imgEroded", imgEroded)







cv.waitKey(0)

# plt.imshow(imgCanny[:, :, ::-1])
# plt.show()
