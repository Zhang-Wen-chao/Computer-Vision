import cv2
import numpy as np

# 读取图像并转换为灰度图像
image = cv2.imread('lena.jpg', cv2.IMREAD_GRAYSCALE)

# 使用高斯滤波器进行平滑处理
gaussian_blur = cv2.GaussianBlur(image, (5, 5), 0)

# 使用拉普拉斯算子进行边缘检测
laplacian = cv2.Laplacian(gaussian_blur, cv2.CV_64F)

# 将拉普拉斯的结果归一化到0-255
laplacian_abs = cv2.convertScaleAbs(laplacian)

# 显示结果
cv2.imshow('LoG Edge Detection', laplacian_abs)
cv2.waitKey(0)
cv2.destroyAllWindows()
