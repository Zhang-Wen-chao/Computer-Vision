import cv2
import numpy as np

# 读取图像并转换为灰度图像
image = cv2.imread('lena.jpg', cv2.IMREAD_GRAYSCALE)

# 垂直方向的Sobel核
vertical_kernel = np.array([[-1, 0, 1],
                            [-2, 0, 2],
                            [-1, 0, 1]])

# 水平方向的Sobel核
horizontal_kernel = np.array([[-1, -2, -1],
                              [0, 0, 0],
                              [1, 2, 1]])

# 使用filter2D函数应用核
vertical_lines = cv2.filter2D(image, -1, vertical_kernel)
horizontal_lines = cv2.filter2D(image, -1, horizontal_kernel)

# 显示结果
cv2.imshow('Vertical Lines', vertical_lines)
cv2.imshow('Horizontal Lines', horizontal_lines)
cv2.waitKey(0)
cv2.destroyAllWindows()
