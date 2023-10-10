import cv2
import numpy as np

def ideal_low_pass_filter(input_image, cutoff_frequency):
    # 获取图像的行和列
    rows, cols = input_image.shape
    # 创建一个掩模
    mask = np.zeros((rows, cols), np.uint8)
    center = (rows // 2, cols // 2)

    # 设置圆内的值为1，圆外的值为0
    for x in range(rows):
        for y in range(cols):
            if (x - center[0])**2 + (y - center[1])**2 <= cutoff_frequency**2:
                mask[x, y] = 1

    # 对图像进行傅里叶变换并移动到中心
    f = np.fft.fft2(input_image)
    fshift = np.fft.fftshift(f)

    # 应用掩模
    fshift = fshift * mask

    # 逆傅里叶变换
    f_ishift = np.fft.ifftshift(fshift)
    img_back = np.fft.ifft2(f_ishift)
    img_back = np.abs(img_back)
    img_back = cv2.normalize(img_back, None, 0, 255, cv2.NORM_MINMAX)
    return np.uint8(img_back)


if __name__ == "__main__":
    image = cv2.imread("test.jpg", cv2.IMREAD_GRAYSCALE)
    if image is None:
        print("读取错误")
        exit(-1)

    # 设置截止频率
    cutoff = 70 # 30模糊地一塌糊涂
    filtered_image = ideal_low_pass_filter(image, cutoff)

    cv2.imshow("Original Image", image)
    cv2.imshow("Filtered Image", filtered_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
