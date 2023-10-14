import cv2
import numpy as np

# 读取图像并转换为灰度图像
image = cv2.imread('lena.jpg', cv2.IMREAD_GRAYSCALE)

# 定义Kirsch算子的8个方向
kirsch_kernels = [
    np.array([[-3, -3, 5], [-3, 0, 5], [-3, -3, 5]]),
    np.array([[-3, 5, 5], [-3, 0, 5], [-3, -3, -3]]),
    np.array([[5, 5, 5], [-3, 0, -3], [-3, -3, -3]]),
    np.array([[5, 5, -3], [5, 0, -3], [-3, -3, -3]]),
    np.array([[5, -3, -3], [5, 0, -3], [5, -3, -3]]),
    np.array([[-3, -3, -3], [5, 0, -3], [5, 5, -3]]),
    np.array([[-3, -3, -3], [-3, 0, -3], [5, 5, 5]]),
    np.array([[-3, -3, -3], [-3, 0, 5], [-3, 5, 5]])
]

# 对每个方向的核应用filter2D函数，并取最大值作为输出
output_images = [cv2.filter2D(image, -1, kernel) for kernel in kirsch_kernels]
kirsch_output = np.max(output_images, axis=0)

# 显示结果
cv2.imshow('Kirsch Edge Detection', kirsch_output)
cv2.waitKey(0)
cv2.destroyAllWindows()
