import cv2
import numpy as np

def homomorphic_filter(input_image, gamma_high=1.5, gamma_low=0.5, cutoff=30):
    # 将图像转换为浮点型并计算其对数
    img_log = np.log1p(np.array(input_image, dtype="float"))

    # 对图像进行傅里叶变换并移动到中心
    img_fft = np.fft.fft2(img_log)
    img_fft_shift = np.fft.fftshift(img_fft)

    # 获取图像的行和列
    rows, cols = input_image.shape
    center = (rows // 2, cols // 2)

    # 创建高斯滤波器
    x = np.linspace(-center[0], center[0], rows)
    y = np.linspace(-center[1], center[1], cols)
    x, y = np.meshgrid(y, x)
    distance = np.sqrt(x**2 + y**2)
    mask = np.exp(-(distance**2) / (2 * cutoff**2))

    # 应用同态滤波器
    img_fft_shift = (gamma_high - gamma_low) * (1 - mask) * img_fft_shift + gamma_low * img_fft_shift

    # 逆傅里叶变换
    img_fft_ishift = np.fft.ifftshift(img_fft_shift)
    img_back = np.fft.ifft2(img_fft_ishift)
    img_back = np.abs(img_back)
    img_exp = np.expm1(img_back)
    img_exp = np.clip(img_exp, 0, 255)
    img_out = np.array(img_exp, dtype="uint8")

    return img_out

if __name__ == "__main__":
    image = cv2.imread("test.jpg", cv2.IMREAD_GRAYSCALE)
    if image is None:
        print("读取错误")
        exit(-1)

    filtered_image = homomorphic_filter(image)

    cv2.imshow("Original Image", image)
    cv2.imshow("Filtered Image", filtered_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
