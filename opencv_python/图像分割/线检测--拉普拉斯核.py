import cv2
import numpy as np

# 读取图像并转换为灰度图像
image = cv2.imread('lena.jpg', cv2.IMREAD_GRAYSCALE)

# 定义拉普拉斯核
laplacian_kernel = np.array([
    [0, 1, 0],
    [1, -4, 1],
    [0, 1, 0]
])

# 使用filter2D函数应用拉普拉斯核
laplacian = cv2.filter2D(image, -1, laplacian_kernel)

# 将拉普拉斯的结果归一化到0-255
laplacian_abs = cv2.convertScaleAbs(laplacian)

# 显示结果
cv2.imshow('Laplacian Line Detection', laplacian_abs)
cv2.waitKey(0)
cv2.destroyAllWindows()
