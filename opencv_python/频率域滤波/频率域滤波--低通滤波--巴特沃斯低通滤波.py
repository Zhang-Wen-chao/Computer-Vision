import cv2
import numpy as np

def butterworth_low_pass_filter(input_image, cutoff_frequency, order=1):
    # 获取图像的行和列
    rows, cols = input_image.shape
    center = (rows // 2, cols // 2)

    # 创建巴特沃斯滤波器
    x = np.linspace(-center[0], center[0], rows)
    y = np.linspace(-center[1], center[1], cols)
    x, y = np.meshgrid(y, x)
    distance = np.sqrt(x**2 + y**2)
    mask = 1 / (1 + (distance / cutoff_frequency)**(2*order))

    # 对图像进行傅里叶变换并移动到中心
    f = np.fft.fft2(input_image)
    fshift = np.fft.fftshift(f)

    # 应用滤波器
    fshift = fshift * mask

    # 逆傅里叶变换
    f_ishift = np.fft.ifftshift(fshift)
    img_back = np.fft.ifft2(f_ishift)
    img_back = np.abs(img_back)

    # 归一化
    img_back = cv2.normalize(img_back, None, 0, 255, cv2.NORM_MINMAX)
    return np.uint8(img_back)

if __name__ == "__main__":
    image = cv2.imread("test.jpg", cv2.IMREAD_GRAYSCALE)
    if image is None:
        print("读取错误")
        exit(-1)

    # 设置截止频率和滤波器的阶数
    cutoff = 30
    order = 2
    filtered_image = butterworth_low_pass_filter(image, cutoff, order)

    cv2.imshow("Original Image", image)
    cv2.imshow("Filtered Image", filtered_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
