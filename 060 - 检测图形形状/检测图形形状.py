# 060 - 检测图形形状
import cv2 as cv
import numpy as np
from stackImages import *


def getContours(img):
    #                                    图像         检测范围
    contours, hierarchy = cv.findContours(img, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv.contourArea(cnt)
        print(area)
        if area > 500:
            cv.drawContours(imgContours, cnt, -1, (0, 0, 255), 3)
            peri = cv.arcLength(cnt, True)
            print(peri)
            approx = cv.approxPolyDP(cnt, 0.02 * peri, True)
            print(len(approx))
            objCor = len(approx)
            x, y, w, h = cv.boundingRect(approx)
            cv.rectangle(imgContours, (x, y), (x + w, y + h), (0, 255, 0), 2)

            objType = "None"
            if objCor == 3:
                objType = "Tri"
            elif objCor == 4:
                if (w / float(h) > 0.95) and (w / float(h) < 1.05):
                    objType = "Square"
                else:
                    objType = "Rec"
            elif objCor > 4:
                objType = "Circle"
            else:
                objType = "None"

            cv.putText(imgContours, objType,
                       (x + w // 2 - 10, y + h // 2), cv.FONT_HERSHEY_COMPLEX,
                       0.7, (0, 0, 0), 3)


path = "./shapes.png"
img = cv.imread(path)

# 首先转换为灰度，以便找到拐角
imgContours = img
imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
imgBlur = cv.GaussianBlur(imgGray, (7, 7), 1)  # 最后一个越大，模糊越厉害
imgCanny = cv.Canny(imgBlur, 50, 50)
imgBlack = np.zeros_like(img)
# cv.imshow("img", img)
# cv.imshow("imgGray", imgGray)
# cv.imshow("imgBlur", imgBlur)

getContours(imgCanny)

imgStack = stackImages(0.6, ([img, imgGray, imgBlur],
                             [imgBlack, imgCanny, imgContours]))

cv.imshow("imgStack", imgStack)
cv.waitKey(0)
