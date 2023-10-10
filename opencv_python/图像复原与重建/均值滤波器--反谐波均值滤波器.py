import cv2
import numpy as np
import random

def add_salt_and_pepper_noise(img, amount=0.02):
    """Add salt and pepper noise to image."""
    row, col = img.shape
    salt_num = np.ceil(amount * img.size * 0.5)
    coords = [np.random.randint(0, i - 1, int(salt_num)) for i in img.shape]
    img[coords[0], coords[1]] = 255

    pepper_num = np.ceil(amount * img.size * 0.5)
    coords = [np.random.randint(0, i - 1, int(pepper_num)) for i in img.shape]
    img[coords[0], coords[1]] = 0
    return img

def contraharmonic_mean_filter(img_input, m, n, q):
    # Extend the image edge using the reflection method
    img_input = cv2.copyMakeBorder(img_input, (m-1)//2, (m-1)//2, (n-1)//2, (n-1)//2, cv2.BORDER_REFLECT)
    img_output = np.zeros_like(img_input)

    # Contraharmonic mean filtering
    for i in range((m-1)//2, img_input.shape[0] - (m-1)//2):
        for j in range((n-1)//2, img_input.shape[1] - (n-1)//2):
            Sum1 = np.sum(np.power(img_input[i-(m-1)//2:i+(m-1)//2+1, j-(n-1)//2:j+(n-1)//2+1], q+1))
            Sum2 = np.sum(np.power(img_input[i-(m-1)//2:i+(m-1)//2+1, j-(n-1)//2:j+(n-1)//2+1], q))
            Sum = Sum1 / Sum2
            img_output[i, j] = np.clip(Sum, 0, 255)

    # Crop the image to remove the extended edge
    img_output = img_output[(m-1)//2:-(m-1)//2, (n-1)//2:-(n-1)//2]
    return img_output

if __name__ == "__main__":
    # Generate a grayscale image with salt and pepper noise
    image = np.ones((512, 512), dtype=np.uint8) * 127
    noisy_image = add_salt_and_pepper_noise(image.copy())

    cv2.imshow("Noisy Image", noisy_image)

    # Apply the contraharmonic mean filter
    filtered_image = contraharmonic_mean_filter(noisy_image, 5, 5, 2)
    cv2.imshow("Filtered Image", filtered_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
