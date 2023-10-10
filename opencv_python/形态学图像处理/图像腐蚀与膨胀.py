import cv2
import numpy as np

def main():
    # 读取图像
    image = cv2.imread('lena.jpg', cv2.IMREAD_GRAYSCALE)
    if image is None:
        print("读取错误")
        exit()

    # 显示原始图像
    cv2.imshow('Original Image', image)

    # 定义结构元素 (5x5 的正方形)
    kernel = np.ones((5,5), np.uint8)

    # 腐蚀操作
    eroded_image = cv2.erode(image, kernel, iterations=1)
    cv2.imshow('Eroded Image', eroded_image)

    # 膨胀操作
    dilated_image = cv2.dilate(image, kernel, iterations=1)
    cv2.imshow('Dilated Image', dilated_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
