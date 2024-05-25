import cv2
import numpy as np

# 读取图像并转换为灰度图像
image = cv2.imread('lena.jpg', cv2.IMREAD_GRAYSCALE)

# 二值化图像
_, binary = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY_INV)

# 提取连通域
num_labels, labels = cv2.connectedComponents(binary)

# 创建一个空彩色图像来可视化结果
output = np.zeros((image.shape[0], image.shape[1], 3), dtype=np.uint8)

# 为每个标签分配一个随机颜色
colors = []
for i in range(1, num_labels):
    colors.append(np.array([np.random.randint(0, 255), np.random.randint(0, 255), np.random.randint(0, 255)]))

# 填充输出图像
for y in range(output.shape[0]):
    for x in range(output.shape[1]):
        if labels[y, x] > 0:
            output[y, x, :] = colors[labels[y, x] - 1]

# 显示结果
cv2.imshow('Original Image', image)
cv2.imshow('Connected Components', output)
cv2.waitKey(0)
cv2.destroyAllWindows()
