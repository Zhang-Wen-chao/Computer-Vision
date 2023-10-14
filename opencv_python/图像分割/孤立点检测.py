import cv2
import numpy as np

# 读取图像并转换为灰度图像
image = cv2.imread('lena.jpg', cv2.IMREAD_GRAYSCALE)

# 二值化图像
_, binary = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

# 定义一个3x3的结构元素
kernel = np.ones((3,3),np.uint8)

# 使用膨胀操作，但保持原始图像不变
dilated = cv2.dilate(binary, kernel, iterations = 1)

# 孤立点是原始图像中的前景像素，但在膨胀图像中是背景像素
isolated = ((binary == 255) & (dilated != 255)).astype(np.uint8) * 255

# 显示结果
cv2.imshow('Original Image', image)
cv2.imshow('Isolated Points', isolated)
cv2.waitKey(0)
cv2.destroyAllWindows()
