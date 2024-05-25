import cv2

# 读取图像
image = cv2.imread("test.jpg")
if image is None:
    print("读取错误")
    exit()

# 使用中值滤波器进行滤波
kernel_size = 5  # 定义滤波器的大小，必须是奇数，可以根据需要进行调整
blurred_image = cv2.medianBlur(image, kernel_size)

# 显示原始图像和滤波后的图像
cv2.imshow("Original Image", image)
cv2.imshow("Median Blurred Image", blurred_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
