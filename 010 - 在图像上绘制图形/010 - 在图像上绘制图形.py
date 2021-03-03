import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

# 创建一个全黑的图像
img = np.zeros((512, 512, 3), np.uint8)

# 绘制直线 图像  起点     结束点        颜色     线径
cv.line(img, (0, 0), (511, 511), (255, 0, 0), 5)

# 绘制圆形 图形     圆心     半径     颜色     线径/ -1表示填充
cv.circle(img, (256, 256), 60, (0, 0, 255), -1)

# 绘制矩形    图形    左上角        右下角        颜色     线径
cv.rectangle(img, (100, 100), (400, 500), (0, 255, 0), 5)

# 图像中写字 图形    内容          位置              字体                  字体大小    颜色    线径宽度  线形(缺省)
cv.putText(img, "Hello Fox!", (100, 150), cv.FONT_HERSHEY_COMPLEX_SMALL, 3, (255, 255, 255), 3, )
plt.imshow(img[:, :, ::-1])
plt.show()
