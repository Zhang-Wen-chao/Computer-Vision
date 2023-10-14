import cv2
import numpy as np

def laplacian_frequency_filter(input_image):
    # 对图像进行傅里叶变换并移动到中心
    img_fft = np.fft.fft2(input_image)
    img_fft_shift = np.fft.fftshift(img_fft)

    # 获取图像的行和列
    rows, cols = input_image.shape
    center = (rows // 2, cols // 2)

    # 创建拉普拉斯滤波器
    x = np.linspace(-center[0], center[0], rows)
    y = np.linspace(-center[1], center[1], cols)
    x, y = np.meshgrid(y, x)
    distance = np.sqrt(x**2 + y**2)
    mask = -4 * np.pi**2 * distance**2
    mask = mask / np.max(np.abs(mask))  # Normalize the filter

    # 应用拉普拉斯滤波器
    img_fft_shift = mask * img_fft_shift

    # 逆傅里叶变换
    img_fft_ishift = np.fft.ifftshift(img_fft_shift)
    img_back = np.fft.ifft2(img_fft_ishift)
    img_back = np.abs(img_back)
    
    # 将拉普拉斯滤波器的输出与原始图像相加以实现锐化
    sharpened = np.clip(input_image + img_back, 0, 255)
    img_out = np.array(sharpened, dtype="uint8")

    return img_out

if __name__ == "__main__":
    image = cv2.imread("test.jpg", cv2.IMREAD_GRAYSCALE)
    if image is None:
        print("读取错误")
        exit(-1)

    filtered_image = laplacian_frequency_filter(image)

    cv2.imshow("Original Image", image)
    cv2.imshow("Filtered Image", filtered_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
