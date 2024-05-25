import cv2
import numpy as np

def midpoint_filter(img_input, m, n):
    img_output = img_input.copy()
    num = m * n
    sortarray = np.zeros(num, dtype=np.uint8)

    img_input = cv2.copyMakeBorder(img_input, (m - 1) // 2, (m - 1) // 2, (n - 1) // 2, (n - 1) // 2, cv2.BORDER_REFLECT)

    for i in range((m - 1) // 2, img_input.shape[0] - (m - 1) // 2):
        for j in range((n - 1) // 2, img_input.shape[1] - (n - 1) // 2):
            h = 0
            for x in range(-(m - 1) // 2, (m + 1) // 2):
                for y in range(-(n - 1) // 2, (n + 1) // 2):
                    sortarray[h] = img_input[i + x, j + y]
                    h += 1
            sortarray.sort()
            img_output[i - (m - 1) // 2, j - (n - 1) // 2] = round((sortarray[0] + sortarray[num-1]) / 2)
    return img_output

def add_gaussian_noise(image, mean=0, sigma=25):
    row, col = image.shape
    gauss = np.random.normal(mean, sigma, (row, col))
    noisy = np.clip(image + gauss, 0, 255)
    return noisy.astype(np.uint8)

if __name__ == "__main__":
    # Generate a grayscale image of size 512x512 with gaussian noise
    image = np.ones((512, 512), dtype=np.uint8) * 127
    noisy_image = add_gaussian_noise(image)
    cv2.imshow("Noisy Image", noisy_image)

    # Apply custom midpoint filter to the noisy image
    filtered_image_custom = midpoint_filter(noisy_image, 7, 7)
    cv2.imshow("Filtered Image (Custom)", filtered_image_custom)

    # Apply OpenCV's official median filter for comparison
    filtered_image_official = cv2.medianBlur(noisy_image, 7)
    cv2.imshow("Filtered Image (OpenCV)", filtered_image_official)

    cv2.waitKey(0)
