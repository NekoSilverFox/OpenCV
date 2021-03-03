# 003 - 获取并修改图像中的像素点

import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

# 创建全黑的图像，3表示三个色彩通道; 第一个参数指图像大小；第二个参数指为一个图像
img = np.zeros((256, 256, 3), np.uint8)

# 显示图像
plt.imshow(img[:, :, ::-1])
plt.show()

# 获取像素，对于BGR图像，返回的是一个列表
bgr_pixel = img[100, 100]

# 只返回某一个通道的值
b_pixel = img[100, 100, 0]

# 将 100x100 处的像素写为红色，注意事项BGR通道
img[100, 100] = (0, 0, 255)

print(img[100, 100])
plt.imshow(img[:, :, ::-1])
plt.show()

####################################################

# 获取图像属性
# 图像形状
print(img.shape)  # (256, 256, 3)

# 数值类型
print(img.dtype)  # uint8

# 图像的像素数
print(img.size)  #  196608
