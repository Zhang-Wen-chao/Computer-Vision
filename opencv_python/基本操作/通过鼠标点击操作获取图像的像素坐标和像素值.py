import cv2

# 鼠标回调函数
def onMouse(event, x, y, flags, param):
    im = param
    if event == cv2.EVENT_LBUTTONDOWN:
        if len(im.shape) == 2:  # 灰度图
            pixel_value = im[y, x]
            print(f"在坐标 ({x}, {y}) 的像素值为: {pixel_value}")
        elif len(im.shape) == 3:  # 彩色图
            b, g, r = im[y, x]
            print(f"在坐标 ({x}, {y}) 的 B 值为: {b}, G 值为: {g}, R 值为: {r}")

# 读取图像
image = cv2.imread("test.jpg")
if image is None:
    print("读取错误")
    exit()

# 显示图像
cv2.imshow("image", image)

# 设置鼠标回调函数
cv2.setMouseCallback("image", onMouse, image)

# 等待用户按键
cv2.waitKey(0)
cv2.destroyAllWindows()
