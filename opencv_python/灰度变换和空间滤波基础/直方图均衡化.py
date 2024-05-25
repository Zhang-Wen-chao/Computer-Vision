import cv2

# 读取图像
image = cv2.imread("test.jpg")

# 检查图像是否正确读取
if image is None:
    print("读取错误")
    exit()

# 转换为灰度图像
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("image_gray", image_gray)

# 直方图均衡化
image_enhanced = cv2.equalizeHist(image_gray)
cv2.imshow("image_enhanced", image_enhanced)

# 暂停，保持图像显示，等待按键结束
cv2.waitKey(0)
cv2.destroyAllWindows()
