import cv2 as cv
"""
摄像头的使用和视频非常相似
"""


cam = cv.VideoCapture(2)  # 这里的数字代表摄像头ID，如果有多个摄像头，请尝试更改这些ID

# 设置摄像头的大小
cam.set(3, 640)  # 第一个参数`3`代表 `宽度`
cam.set(4, 480)  # 第一个参数`4`代表 `高度`
# cam.set(10, 1000)  # 第一个参数`10`代表 `亮度`

while True:
    success, img = cam.read()
    cv.imshow("Video Cam", img)

    # 以便打破循环
    if cv.waitKey(1) & 0xFF == ord('q'):
        break