
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
# Creates a window. The function namedWindow creates a window that can be used as a placeholder for images and trackbars. Created windows are referred to by their names
cv2.namedWindow("TrackBars")

# Resizes the window to the specified size
cv2.resizeWindow("TrackBars", 640, 240)

cv2.createTrackbar("R", "TrackBars", 0, 255, empty)  # 红色色彩通道
cv2.createTrackbar("G", "TrackBars", 0, 255, empty)  # 绿色色彩通道
cv2.createTrackbar("B", "TrackBars", 0, 255, empty)  # 蓝色色彩通道
cv2.createTrackbar("Filter", "TrackBars", 0, 4, empty)  # 蓝色色彩通道
cv2.createTrackbar("Blur", "TrackBars", 0, 255, empty)  # 高斯模糊

# Opens a video file or a capturing device or an IP video stream for video capturing with API Preference
cam = cv2.VideoCapture(0)  # 这里的数字代表摄像头ID，如果有多个摄像头，请尝试更改这些ID
WIDTH = 640
HEIGHT = 480

# 设置摄像头的大小
# Switches exceptions mode
cam.set(3, WIDTH)  # 第一个参数`3`代表 `宽度`
cam.set(4, HEIGHT)  # 第一个参数`4`代表 `高度`
output = cv2.VideoWriter("output.avi", cv2.VideoWriter_fourcc("M", "J", "P", "G"), 29, (WIDTH, HEIGHT))  # 编码格式

while True:
    success, img = cam.read()

    if not success:
        print("[ERROR] Can not read camera")
        break

    # Creates a trackbar and attaches it to the specified window.
    R = cv2.getTrackbarPos("R", "TrackBars")  # 红色色彩通道的值（从控制栏中获得）
    G = cv2.getTrackbarPos("G", "TrackBars")  # 绿色色彩通道的值（从控制栏中获得）
    B = cv2.getTrackbarPos("B", "TrackBars")  # 蓝色色彩通道的值（从控制栏中获得）
    Filter = cv2.getTrackbarPos("Filter", "TrackBars")  # 蓝色色彩通道的值（从控制栏中获得）
    Blur = cv2.getTrackbarPos("Blur", "TrackBars")  # 高斯模糊的值（从控制栏中获得）
    print(R, G, B, Filter, Blur)

    mask_img = init_canvas(WIDTH, HEIGHT, color=(B, G, R))  # 色彩蒙版
    if Filter == 0:
        pass
    elif Filter == 1:
        # Converting the color space of an image to HSV
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    elif Filter == 2:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2HLS)
    elif Filter == 3:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    elif Filter == 4:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)

    img_res = cv2.addWeighted(img, 1, mask_img, 0.5, 0)  # 叠加颜色
    val_blur = get_odd(Blur)  # add Gaussian filter
    img_res = cv2.GaussianBlur(img_res, (val_blur, val_blur), 0)  # Blurs an image using a Gaussian filter

    # 以便打破循环
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    output.write(img_res)

    # Displays an image in the specified window
    cv2.imshow("Row", img)  # 显示原图像
    cv2.imshow("Result", img_res)  # 显示调色后的图像

    # Waits for a pressed key
    cv2.waitKey(1)

cam.release()
output.release()
