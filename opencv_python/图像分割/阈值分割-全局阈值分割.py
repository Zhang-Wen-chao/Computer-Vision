import cv2

# 读取图像并转换为灰度图像
image = cv2.imread('lena.jpg', cv2.IMREAD_GRAYSCALE)

# 使用全局阈值分割
ret, thresh = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

# 显示结果
cv2.imshow('Global Thresholding', thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()
