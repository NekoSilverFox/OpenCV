import cv2 as cv
import numpy as np
from stackImages import stackImages


CAM_WIDTH = 640
CAM_HEIGHT = 480
CAM_BRIGHTNESS = 150
CAM_ID = 2
PRINT_SIZE = 5
PRINT_COLOR = (0, 255, 255)
gl_path_mask = np.zeros((CAM_HEIGHT, CAM_WIDTH, 3), dtype=np.uint8)


def empty(none):
    pass


def color_picker():
    # 设置摄像头的大小
    cam = cv.VideoCapture(CAM_ID)  # 这里的数字代表摄像头ID
    cam.set(3, CAM_WIDTH)  # 第一个参数`3`代表 `宽度`
    cam.set(4, CAM_HEIGHT)  # 第一个参数`4`代表 `高度`
    cam.set(10, CAM_BRIGHTNESS)  # 第一个参数`10`代表 `亮度`

    # 跟踪杆
    cv.namedWindow("HSY-TrackBars")
    cv.resizeWindow("HSY-TrackBars", CAM_WIDTH, CAM_HEIGHT)

    cv.createTrackbar("Hue Min", "HSY-TrackBars", 0, 179, empty)
    cv.createTrackbar("Sat Min", "HSY-TrackBars", 0, 255, empty)
    cv.createTrackbar("Val Min", "HSY-TrackBars", 0, 255, empty)

    cv.createTrackbar("Hue Max", "HSY-TrackBars", 179, 179, empty)
    cv.createTrackbar("Sat Max", "HSY-TrackBars", 255, 255, empty)
    cv.createTrackbar("Val Max", "HSY-TrackBars", 255, 255, empty)

    #############################################################

    while True:
        is_success, img = cam.read()
        img_HSV = cv.cvtColor(img, cv.COLOR_BGR2HSV)

        h_min = cv.getTrackbarPos("Hue Min", "HSY-TrackBars")
        h_max = cv.getTrackbarPos("Hue Max", "HSY-TrackBars")

        s_min = cv.getTrackbarPos("Sat Min", "HSY-TrackBars")
        s_max = cv.getTrackbarPos("Sat Max", "HSY-TrackBars")

        v_min = cv.getTrackbarPos("Val Min", "HSY-TrackBars")
        v_max = cv.getTrackbarPos("Val Max", "HSY-TrackBars")
        print(h_min, h_max, s_min, s_max, v_min, v_max)

        # 将我们不需要的颜色设为黑色，需要的设为白色
        lower = np.array([h_min, s_min, v_min])
        upper = np.array([h_max, s_max, v_max])
        mask = cv.inRange(img_HSV, lower, upper)
        img_result = cv.bitwise_and(img, img, mask=mask)
        mask = cv.cvtColor(mask, cv.COLOR_GRAY2BGR)

        img_stack = stackImages(0.6, ([img, mask, img_result]))
        cv.imshow("Stack images", img_stack)
        cv.waitKey(1)


def print_path(mask):
    pass


def find_color(img_input, prick_colors_list, print_colors_list):
    img_HSV = cv.cvtColor(img_input, cv.COLOR_BGR2HSV)
    index_color = 0

    for color in prick_colors_list:
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv.inRange(img_HSV, lower, upper)

        x, y = get_contours(mask)
        cv.circle(img_result, (x, y), PRINT_SIZE, print_colors_list[index_color], -1)
        cv.circle(gl_path_mask, (x, y), PRINT_SIZE, print_colors_list[index_color], -1)

        index_color += 1
        if index_color > 3:
            print("ERROR! In dead loop!")

        # print(mask)
        # 将我们不需要的颜色设为黑色，需要的设为白色
        cv.imshow("Mask", mask)


def get_contours(img):
    contours, hierarchy = cv.findContours(img, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
    x = 0
    y = 0
    w = 0
    h = 0
    for event in contours:
        area = cv.contourArea(event)
        if area > 500:
            cv.drawContours(img_result, event, -1, (255, 0, 0), 3)
            peri = cv.arcLength(event, True)
            approx = cv.approxPolyDP(event, 0.02 * peri, True)
            x, y, w, h = cv.boundingRect(approx)
            print("Print point on [%d, %d]" % (x, y))
    return (x + w // 2), (y + h // 2)


##############################################################################

# color_picker()

# 设置摄像头的大小
cam = cv.VideoCapture(CAM_ID)  # 这里的数字代表摄像头ID，如果有多个摄像头，请尝试更改这些ID
cam.set(3, CAM_WIDTH)  # 第一个参数`3`代表 `宽度`
cam.set(4, CAM_HEIGHT)  # 第一个参数`4`代表 `高度`
cam.set(10, CAM_BRIGHTNESS)  # 第一个参数`10`代表 `亮度`

picker_colors_list = [[0, 103, 255, 179, 255, 255],  # Red
                      [104, 102, 134, 179, 255, 255]]  # Blue

print_color_list = [[0, 0, 255],
                    [255, 0, 0]]


while True:
    is_success, img_row = cam.read()
    img_result = img_row.copy()

    find_color(img_row, picker_colors_list, print_color_list)
    img_result_with_path = cv.addWeighted(img_row, 1, gl_path_mask, 1, 0)

    # cv.imshow("Row camera", img)
    cv.imshow("Result camera", img_result)
    cv.imshow("Result path on canvas", gl_path_mask)
    cv.imshow("Result camera with path", img_result_with_path)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break
