# 图像的剪裁
import cv2 as cv

img = cv.imread("./call.png")
print(img.shape)

# 指定 起点和结束点
imgCropped = img[100:200, 100:250]

cv.imshow("img", img)
cv.imshow("imgCropped", imgCropped)

cv.waitKey(0)