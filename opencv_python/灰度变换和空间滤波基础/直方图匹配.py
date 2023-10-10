import cv2
import numpy as np

# 读取图像
image1 = cv2.imread("test.jpg")

# 检查图像是否正确读取
if image1 is None:
    print("读取错误")
    exit()

# 转换为灰度图像
image1_gray = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
cv2.imshow("image1_gray", image1_gray)

image2 = cv2.imread("lena.jpg")
if image2 is None:
    print("读取错误")
    exit()

image2_gray = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
cv2.imshow("image2_gray", image2_gray)

# 均衡化处理
image1_gray = cv2.equalizeHist(image1_gray)
image2_gray = cv2.equalizeHist(image2_gray)

# 获取两个均衡化图像的直方图
histsize = 256
hist1 = cv2.calcHist([image1_gray], [0], None, [histsize], [0, 256])
hist2 = cv2.calcHist([image2_gray], [0], None, [histsize], [0, 256])

# 计算两个均衡化图像直方图的累积概率
hist1_cdf = hist1.cumsum()
hist2_cdf = hist2.cumsum()

hist1_cdf_normalized = hist1_cdf / hist1_cdf.max()
hist2_cdf_normalized = hist2_cdf / hist2_cdf.max()

# 两个累计概率之间的差值，用于找到最接近的点
diff_cdf = np.abs(hist1_cdf_normalized - hist2_cdf_normalized[:, None])

lut = np.argmin(diff_cdf, axis=1).astype(np.uint8)
image_enhanced = cv2.LUT(image1_gray, lut)
cv2.imshow("image_enhanced", image_enhanced)

cv2.waitKey(0)
cv2.destroyAllWindows()
