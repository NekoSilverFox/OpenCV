# https://www.coder.work/article/2087334
"""
实际上，dst是基于以下公式创建的:

dst = src1*alpha + src2*beta + gamma

就是说，当您将实际上是3D数组的图像与alpha相乘时，您将对所有项相乘。
例如，对于一个蓝色像素，您具有[255, 0, 0]和白色[255, 255, 255]，
并且在将矩阵相加时，如果您希望结果为蓝色，则应将白色像素转换为0，
而实际上是黑色(不会从物理学的 Angular 来看是正确的)。
您可以使用高级numpy索引简单地找到白色像素，然后将其转换为零
"""

import cv2

img1 = cv2.imread('./blue.png')
img2 = cv2.imread('./red.png')

img1[img1[:, :, 1:].all(axis=-1)] = 0
img2[img2[:, :, 1:].all(axis=-1)] = 0

dst = cv2.addWeighted(img1, 1, img2, 1, 0)

cv2.imshow('sas', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()