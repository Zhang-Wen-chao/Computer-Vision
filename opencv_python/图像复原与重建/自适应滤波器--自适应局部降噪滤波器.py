import cv2
import numpy as np

def adaptive_local_noise_reduction_filter(img_input, m, n):
    img_output = img_input.copy()
    sortarray = np.zeros((m * n), dtype=np.uint8)

    # 1. 扩展图像边缘，扩展方法为镜像
    img_input = cv2.copyMakeBorder(img_input, (m - 1) // 2, (m - 1) // 2, (n - 1) // 2, (n - 1) // 2, cv2.BORDER_REFLECT)

    # 2. 计算图像方差
    mean1, stddev1 = cv2.meanStdDev(img_input)

    # 3. 自适应局部降噪滤波
    for i in range((m - 1) // 2, img_input.shape[0] - (m - 1) // 2):
        for j in range((n - 1) // 2, img_input.shape[1] - (n - 1) // 2):
            h = 0
            for x in range(-(m - 1) // 2, (m + 1) // 2):
                for y in range(-(n - 1) // 2, (n + 1) // 2):
                    sortarray[h] = img_input[i + x, j + y]
                    h += 1

            # 计算局部均值和方差
            mean2, stddev2 = cv2.meanStdDev(sortarray)

            # 滤波器
            k = (stddev1**2) / (stddev2**2 + 0.00001)
            if k <= 1:
                img_output[i - (m - 1) // 2, j - (n - 1) // 2] = img_input[i, j] - k * (img_input[i, j] - mean2)
            else:
                img_output[i - (m - 1) // 2, j - (n - 1) // 2] = mean2

    return img_output

def generate_gaussian_noisy_image(size, mean=127, sigma=25):
    image = np.ones(size, dtype=np.uint8) * mean
    noise = np.random.normal(0, sigma, size).astype(np.int16)
    noisy_image = np.clip(image + noise, 0, 255).astype(np.uint8)
    return noisy_image


if __name__ == "__main__":
    noisy_image = generate_gaussian_noisy_image((512, 512))
    cv2.imshow("Noisy Image", noisy_image)

    filtered_image = adaptive_local_noise_reduction_filter(noisy_image, 7, 7)
    cv2.imshow("Filtered Image", filtered_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
