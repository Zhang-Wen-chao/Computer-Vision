import cv2
import numpy as np

# 读取图像并转换为灰度图像
image = cv2.imread('lena.jpg', cv2.IMREAD_GRAYSCALE)

# 使用Sobel函数计算x和y方向的梯度
gradient_x = cv2.Sobel(image, cv2.CV_32F, 1, 0, ksize=3)
gradient_y = cv2.Sobel(image, cv2.CV_32F, 0, 1, ksize=3)

# 计算梯度的幅度和方向
edge_magnitude, edge_angle = cv2.cartToPolar(gradient_x, gradient_y, angleInDegrees=True)

# 将结果转换回8位无符号整数
edge_magnitude = cv2.convertScaleAbs(edge_magnitude)

# 显示结果
cv2.imshow('Sobel Edge Detection', edge_magnitude)
cv2.waitKey(0)
cv2.destroyAllWindows()
