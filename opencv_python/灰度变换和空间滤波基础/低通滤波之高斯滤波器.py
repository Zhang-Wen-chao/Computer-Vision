import cv2

# 读取图像
image = cv2.imread("test.jpg")
if image is None:
    print("读取错误")
    exit()

# 使用高斯滤波器进行滤波
kernel_size = (5, 5)  # 定义滤波器的大小，可以根据需要进行调整
sigma = 1.5  # 定义高斯函数的标准差，可以根据需要进行调整
blurred_image = cv2.GaussianBlur(image, kernel_size, sigma)

# 显示原始图像和滤波后的图像
cv2.imshow("Original Image", image)
cv2.imshow("Gaussian Blurred Image", blurred_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
