import cv2
import numpy as np

# 读取图像
image1 = cv2.imread("test.jpg")
if image1 is None:
    print("读取错误")
    exit()

# 创建滤波器
kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]], dtype=np.float32)

# 使用filter2D函数进行卷积
output_image = cv2.filter2D(image1, -1, kernel)

# 显示原图和处理后的图像
cv2.imshow("image1", image1)
cv2.imshow("output_image", output_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
