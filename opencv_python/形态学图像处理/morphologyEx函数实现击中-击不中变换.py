import cv2
import numpy as np

def main():
    # 读取图像
    image = cv2.imread("lena.jpg", cv2.IMREAD_GRAYSCALE)
    if image is None:
        print("读取错误")
        return -1

    cv2.imshow("Original Image", image)

    # 二值化图像
    _, binary_image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
    cv2.imshow("Binary Image", binary_image)

    # 定义结构元素
    # 例如，一个3x3的结构元素，其中中心是1，四个角是0，其余是-1（不关心的部分）
    se = np.array([
        [0, -1, 0],
        [-1, 1, -1],
        [0, -1, 0]
    ], dtype=np.int8)

    # 使用morphologyEx函数进行击中-击不中变换
    hitmiss_image = cv2.morphologyEx(binary_image, cv2.MORPH_HITMISS, se)
    cv2.imshow("Hit-or-Miss Image", hitmiss_image)

    cv2.waitKey(0)  # 暂停，保持图像显示，等待按键结束

if __name__ == "__main__":
    main()
