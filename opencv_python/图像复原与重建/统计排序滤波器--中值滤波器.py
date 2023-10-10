import cv2
import numpy as np

def generate_gray_image(width, height):
    """生成一个灰色的图像"""
    return np.ones((height, width), dtype=np.uint8) * 128

def add_gaussian_noise(image, mean=0, sigma=25):
    """为图像添加高斯噪声"""
    row, col = image.shape
    gauss = np.random.normal(mean, sigma, (row, col)).astype(np.float32)
    noisy = np.clip(image.astype(np.float32) + gauss, 0, 255).astype(np.uint8)
    return noisy

def median_filter(img_input, m, n):
    # 扩展图像边缘，扩展方法为镜像
    img_input = cv2.copyMakeBorder(img_input, (m-1)//2, (m-1)//2, (n-1)//2, (n-1)//2, cv2.BORDER_REFLECT)
    img_output = np.zeros_like(img_input)

    # 中值滤波
    for i in range((m-1)//2, img_input.shape[0] - (m-1)//2):
        for j in range((n-1)//2, img_input.shape[1] - (n-1)//2):
            window = img_input[i-(m-1)//2:i+(m-1)//2+1, j-(n-1)//2:j+(n-1)//2+1]
            img_output[i, j] = np.median(window)

    # 裁剪图像以移除扩展的边缘
    img_output = img_output[(m-1)//2:-(m-1)//2, (n-1)//2:-(n-1)//2]
    return img_output

if __name__ == "__main__":
    # 生成一个全白的图像
    image = generate_gray_image(512, 512)

    # 为图像添加高斯噪声
    noisy_image = add_gaussian_noise(image)
    cv2.imshow("Noisy Image", noisy_image)

    # 使用自定义的中值滤波函数
    image_output = median_filter(noisy_image, 7, 7)
    cv2.imshow("image_output", image_output)

    # 使用OpenCV的中值滤波函数
    image_output2 = cv2.medianBlur(noisy_image, 7)
    cv2.imshow("image_output2", image_output2)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
