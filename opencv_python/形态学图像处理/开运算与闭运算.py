import cv2

def main():
    # 读取图像
    image = cv2.imread("lena.jpg")
    if image is None:
        print("读取错误")
        return -1

    cv2.imshow("image", image)

    # 转换为灰度图像
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 转换为二值图
    _, image_bw = cv2.threshold(image_gray, 120, 255, cv2.THRESH_BINARY_INV)
    cv2.imshow("image_bw", image_bw)

    # 构造矩形结构元素
    se = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))

    # 闭运算
    image_bw = cv2.dilate(image_bw, se, iterations=5)
    image_bw = cv2.erode(image_bw, se, iterations=5)

    # 如果要进行开运算，可以取消以下注释
    # image_bw = cv2.erode(image_bw, se, iterations=2)
    # image_bw = cv2.dilate(image_bw, se, iterations=2)

    cv2.imshow("image_bw", image_bw)

    cv2.waitKey(0)  # 暂停，保持图像显示，等待按键结束

if __name__ == "__main__":
    main()
