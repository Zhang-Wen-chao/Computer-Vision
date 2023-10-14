import cv2
import numpy as np

# 读取图像并转换为灰度图像
image = cv2.imread('lena.jpg', cv2.IMREAD_GRAYSCALE)

# 定义Prewitt算子
prewitt_x = np.array([
    [-1, 0, 1],
    [-1, 0, 1],
    [-1, 0, 1]
])

prewitt_y = np.array([
    [-1, -1, -1],
    [0, 0, 0],
    [1, 1, 1]
])

# 使用filter2D函数应用Prewitt算子
gradient_x = cv2.filter2D(image, cv2.CV_32F, prewitt_x)
gradient_y = cv2.filter2D(image, cv2.CV_32F, prewitt_y)

# 计算梯度幅度
edge_magnitude = cv2.magnitude(gradient_x, gradient_y)

# 将结果转换回8位无符号整数
edge_magnitude = cv2.convertScaleAbs(edge_magnitude)

# 显示结果
cv2.imshow('Prewitt Edge Detection', edge_magnitude)
cv2.waitKey(0)
cv2.destroyAllWindows()
