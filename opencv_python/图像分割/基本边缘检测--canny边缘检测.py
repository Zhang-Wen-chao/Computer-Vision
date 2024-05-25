import cv2

# 读取图像
image = cv2.imread('lena.jpg', cv2.IMREAD_GRAYSCALE)

# 使用Canny边缘检测
edges = cv2.Canny(image, 100, 200)

# 显示结果
cv2.imshow('Canny Edge Detection', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
