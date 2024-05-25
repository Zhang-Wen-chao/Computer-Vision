import cv2
import numpy as np

# 读取图像
image1 = cv2.imread("test.jpg")
if image1 is None:
    print("读取错误")
    exit()

# 克隆图像
output_image = image1.copy()

rows, cols, channels = image1.shape

# 遍历图像像素
for row in range(1, rows - 1):
    for col in range(1, cols - 1):
        for ch in range(channels):
            # 获取当前像素及其邻居像素的值
            previous = image1[row - 1, col, ch]
            current = image1[row, col, ch]
            next_pixel = image1[row + 1, col, ch]
            left = image1[row, col - 1, ch]
            right = image1[row, col + 1, ch]
            
            # 计算新的像素值
            output_image[row, col, ch] = np.clip(5 * current - (previous + left + right + next_pixel), 0, 255)

# 显示原图和处理后的图像
cv2.imshow("image1", image1)
cv2.imshow("output_image", output_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
