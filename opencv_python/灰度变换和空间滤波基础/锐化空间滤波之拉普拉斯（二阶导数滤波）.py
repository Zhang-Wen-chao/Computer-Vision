import cv2
import numpy as np

def myfilter(image_input):
    image_output = image_input.copy()
    rows, cols = image_input.shape
    for i in range(1, rows-1):
        for j in range(1, cols-1):
            la = 4*image_input[i, j] - image_input[i+1, j] - image_input[i-1, j] - image_input[i, j+1] - image_input[i, j-1]
            image_output[i, j] = np.clip(image_output[i, j] + la, 0, 255)
    return image_output

def myfilter2(image_input):
    image_output = image_input.copy()
    rows, cols = image_input.shape
    for i in range(1, rows-1):
        for j in range(1, cols-1):
            la2 = 8*image_input[i, j] - (image_input[i+1, j] + image_input[i-1, j] + image_input[i, j+1] + image_input[i, j-1]
                 + image_input[i-1, j-1] + image_input[i+1, j+1] + image_input[i-1, j+1] + image_input[i+1, j-1])
            image_output[i, j] = np.clip(image_output[i, j] + la2, 0, 255)
    return image_output

# 读取图像
image = cv2.imread("test.jpg", cv2.IMREAD_GRAYSCALE)
if image is None:
    print("读取错误")
    exit()

cv2.imshow("Original Image", image)

# 使用自定义的滤波函数
image_output = myfilter(image)
cv2.imshow("4-Neighborhood Filtered Image", image_output)

image_output2 = myfilter2(image)
cv2.imshow("8-Neighborhood Filtered Image", image_output2)

cv2.waitKey(0)
cv2.destroyAllWindows()
