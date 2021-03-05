import cv2
import numpy as np

def empty(A):
    pass

def init_canvas(width, height, color=(255, 255, 255)):
    canvas = np.ones((height, width, 3), dtype="uint8")
    canvas[:] = color
    return canvas

def get_odd(num):
    if num % 2 == 0:
        num += 1
    return num

# 跟踪杆
cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars", 640, 240)

cv2.createTrackbar("R", "TrackBars", 0, 255, empty)  # 红色色彩通道
cv2.createTrackbar("G", "TrackBars", 0, 255, empty)  # 绿色色彩通道
cv2.createTrackbar("B", "TrackBars", 0, 255, empty)  # 蓝色色彩通道
cv2.createTrackbar("Blur", "TrackBars", 0, 255, empty)  # 高斯模糊

cam = cv2.VideoCapture(2)  # 这里的数字代表摄像头ID，如果有多个摄像头，请尝试更改这些ID
# 设置摄像头的大小
cam.set(3, 640)  # 第一个参数`3`代表 `宽度`
cam.set(4, 480)  # 第一个参数`4`代表 `高度`

while True:
    success, img = cam.read()

    R = cv2.getTrackbarPos("R", "TrackBars")  # 红色色彩通道的值（从控制栏中获得）
    G = cv2.getTrackbarPos("G", "TrackBars")  # 绿色色彩通道的值（从控制栏中获得）
    B = cv2.getTrackbarPos("B", "TrackBars")  # 蓝色色彩通道的值（从控制栏中获得）
    Blur = cv2.getTrackbarPos("Blur", "TrackBars")  # 高斯模糊的值（从控制栏中获得）
    print(R, G, B, Blur)

    mask_img = init_canvas(640, 480, color=(B, G, R))  # 色彩蒙版
    img_res = cv2.addWeighted(img, 1, mask_img, 0.5, 0)  # 叠加颜色
    val_blur = get_odd(Blur)  # 添加高斯模糊
    img_res = cv2.GaussianBlur(img_res, (val_blur, val_blur), 0)  # 叠加高斯模糊

    cv2.imshow("Row", img)  # 显示原图像
    cv2.imshow("Result", img_res)  # 显示调色后的图像
    cv2.waitKey(1)
