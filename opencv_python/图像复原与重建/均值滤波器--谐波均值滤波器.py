import cv2
import numpy as np

def add_gaussian_noise(image, mean=0, sigma=25):
    """为图像添加高斯噪声"""
    row, col = image.shape
    gauss = np.random.normal(mean, sigma, (row, col)).reshape(row, col)
    noisy = image + gauss
    return np.clip(noisy, 0, 255).astype(np.uint8)

def harmonic_mean_filter(img_input, m, n):
    # 扩展图像边缘，扩展方法为镜像
    img_input = cv2.copyMakeBorder(img_input, (m-1)//2, (m-1)//2, (n-1)//2, (n-1)//2, cv2.BORDER_REFLECT)
    img_output = np.zeros_like(img_input)

    # 谐波均值滤波
    k = m * n
    for i in range((m-1)//2, img_input.shape[0] - (m-1)//2):
        for j in range((n-1)//2, img_input.shape[1] - (n-1)//2):
            Sum = np.sum(1 / (img_input[i-(m-1)//2:i+(m-1)//2+1, j-(n-1)//2:j+(n-1)//2+1] + 0.1))
            Sum = k / Sum
            img_output[i, j] = Sum

    # 裁剪图像以移除扩展的边缘
    img_output = img_output[(m-1)//2:-(m-1)//2, (n-1)//2:-(n-1)//2]
    return img_output

if __name__ == "__main__":
    # 创建一张灰度图像
    image = np.ones((512, 512), dtype=np.uint8) * 127

    # 添加高斯噪声
    noisy_image = add_gaussian_noise(image)

    cv2.imshow("Noisy Image", noisy_image)

    # 使用自定义的谐波均值滤波函数
    image_output = harmonic_mean_filter(noisy_image, 7, 7)
    cv2.imshow("Filtered Image", image_output)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
