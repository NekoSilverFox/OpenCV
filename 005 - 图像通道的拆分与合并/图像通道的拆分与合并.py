# 005 - 图像通道的拆分与合并
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

# 创建全白的图像，3表示三个色彩通道; 第一个参数指图像大小；第二个参数指为一个图像
img = np.zeros((255, 255, 3), np.uint8)

# 通道的拆分
b, g, r = cv.split(img)
# print(cv.split(img))

# 通道的合并
img2 = cv.merge([b, g, r])

# 显示图像
plt.imshow(img2[:, :, ::-1])
plt.show()
