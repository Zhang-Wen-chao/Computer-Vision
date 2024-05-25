import cv2
import numpy as np

def alpha_trimmed_mean_filter(img_input, m, n, d):
    img_output = img_input.copy()
    num = m * n
    sortarray = []

    # 1. 扩展图像边缘，扩展方法为镜像
    img_input = cv2.copyMakeBorder(img_input, (m - 1) // 2, (m - 1) // 2, (n - 1) // 2, (n - 1) // 2, cv2.BORDER_REFLECT)

    # 2. 滤波
    for i in range((m - 1) // 2, img_input.shape[0] - (m - 1) // 2):
        for j in range((n - 1) // 2, img_input.shape[1] - (n - 1) // 2):
            sortarray.clear()
            for x in range(-(m - 1) // 2, (m + 1) // 2):
                for y in range(-(n - 1) // 2, (n + 1) // 2):
                    sortarray.append(img_input[i + x, j + y])
            sortarray.sort()
            img_output[i - (m - 1) // 2, j - (n - 1) // 2] = round(sum(sortarray[d:num-d]) / (num - 2 * d))
    return img_output

def generate_noisy_image(size, salt_prob, pepper_prob):
    image = np.ones(size, dtype=np.uint8) * 255
    total_pixels = size[0] * size[1]

    # Add salt noise
    num_salt = int(total_pixels * salt_prob)
    coords = [np.random.randint(0, i, num_salt) for i in size]
    image[coords[0], coords[1]] = 255

    # Add pepper noise
    num_pepper = int(total_pixels * pepper_prob)
    coords = [np.random.randint(0, i, num_pepper) for i in size]
    image[coords[0], coords[1]] = 0

    return image

if __name__ == "__main__":
    noisy_image = generate_noisy_image((512, 512), 0.05, 0.05)  # 5% salt and 5% pepper noise
    cv2.imshow("Noisy Image", noisy_image)

    filtered_image = alpha_trimmed_mean_filter(noisy_image, 7, 7, 5)
    cv2.imshow("Filtered Image", filtered_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
