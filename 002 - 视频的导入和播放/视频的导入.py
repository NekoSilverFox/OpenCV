import cv2 as cv

video = cv.VideoCapture("./Output.mp4")

# 因为视频是由帧构成的，所以可以使用while循环遍历这些帧
while True:
    success, img = video.read()  # success 的值为 True 或 False
    cv.imshow("Video", img)

    # 以便使用键盘打破中断
    if cv.waitKey(1) & 0xFF == ord("q"):
        break
