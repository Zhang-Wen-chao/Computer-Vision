import cv2
import numpy as np

# 读取图像
image = cv2.imread('lena.jpg', cv2.IMREAD_GRAYSCALE)

# 定义结构元素
kernel = np.ones((3,3), np.uint8)

# 计算形态学梯度
gradient = cv2.morphologyEx(image, cv2.MORPH_GRADIENT, kernel)

# 显示结果
cv2.imshow('Original Image', image)
cv2.imshow('Morphological Gradient', gradient)
cv2.waitKey(0)
cv2.destroyAllWindows()
