import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

x = np.uint8([250])
y = np.uint8([10])
print(cv.add(x, y))  # OpenCV中的加法是饱和操作 如果 250 + 10 --> 255
print(x + y)  # Numpy 添加是模运算 250 + 10 = 260 % 256 = 4

# 注意，图像一定要是相同大小！！！
img1 = cv.imread("./69.png")
img2 = cv.imread("./70.png")

merge1 = cv.add(img1, img2)
merge2 = img1 + img2

# 图像显示
plt.imshow(merge1[:, :, ::-1])
plt.show()

plt.imshow(merge2[:, :, ::-1])
plt.show()

# 当然除了加法，还可以进行其他操作。比如减法，乘法，除法等操作