import cv2
import numpy as np

# 读取图像并转换为灰度图
image = cv2.imread("test.jpg", cv2.IMREAD_GRAYSCALE)
if image is None:
    print("读取错误")
    exit()

# 灰度反转
inverted_image = 255 - image

# 对数变换
# 首先确保所有像素值都是正的，然后应用对数变换
c = 255 / np.log(1 + np.max(image))
log_transformed_image = c * np.log(1 + image)
log_transformed_image = np.array(log_transformed_image, dtype=np.uint8)

# 幂律（伽马）变换
gamma = 1.2  # 可以更改此值以获得不同的效果
gamma_corrected_image = np.array(255 * (image / 255) ** gamma, dtype=np.uint8)

# 显示图像
cv2.imshow("Original Image", image)
cv2.imshow("Inverted Image", inverted_image)
cv2.imshow("Log Transformed Image", log_transformed_image)
cv2.imshow("Gamma Corrected Image", gamma_corrected_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
