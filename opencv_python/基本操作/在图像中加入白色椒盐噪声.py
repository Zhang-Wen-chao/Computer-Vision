import cv2
import numpy as np

def add_salt_noise(image, n):
    rows, cols, channels = image.shape
    for _ in range(n):
        x = np.random.randint(0, cols)
        y = np.random.randint(0, rows)
        if channels == 1:
            image[y, x] = 255
        else:
            image[y, x] = [255, 255, 255]
    return image

image = cv2.imread("test.jpg")
if image is None:
    print("读取错误")
    exit()

cv2.imshow("Original Image", image)
noisy_image = add_salt_noise(image.copy(), 5000)
cv2.imshow("Noisy Image", noisy_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
