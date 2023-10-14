import cv2

def main():
    # 读取图像
    image = cv2.imread("lena.jpg")
    if image is None:
        print("读取错误")
        return -1

    cv2.imshow("Original Image", image)

    # 转换为灰度图像
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 转换为二值图
    _, image_bw = cv2.threshold(image_gray, 120, 255, cv2.THRESH_BINARY_INV)
    cv2.imshow("Binary Image", image_bw)

    # 构造矩形结构元素
    se = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))

    # 使用morphologyEx函数进行腐蚀
    eroded_image = cv2.morphologyEx(image_bw, cv2.MORPH_ERODE, se)
    cv2.imshow("Eroded Image", eroded_image)

    # 使用morphologyEx函数进行膨胀
    dilated_image = cv2.morphologyEx(image_bw, cv2.MORPH_DILATE, se)
    cv2.imshow("Dilated Image", dilated_image)

    # 使用morphologyEx函数进行开运算
    opened_image = cv2.morphologyEx(image_bw, cv2.MORPH_OPEN, se)
    cv2.imshow("Opened Image", opened_image)

    # 使用morphologyEx函数进行闭运算
    closed_image = cv2.morphologyEx(image_bw, cv2.MORPH_CLOSE, se)
    cv2.imshow("Closed Image", closed_image)

    cv2.waitKey(0)  # 暂停，保持图像显示，等待按键结束

if __name__ == "__main__":
    main()
