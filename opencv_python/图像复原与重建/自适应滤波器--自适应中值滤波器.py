import cv2
import numpy as np

def salt(img, n):
    for k in range(n):
        i = int(np.random.random() * img.shape[1])
        j = int(np.random.random() * img.shape[0])
        img[j, i] = 255
    return img

def adaptive_median(img_input, i, j, filter_size, size_max):
    num = filter_size * filter_size
    sortarray = []

    for x in range(-int((filter_size - 1) / 2), int((filter_size - 1) / 2) + 1):
        for y in range(-int((filter_size - 1) / 2), int((filter_size - 1) / 2) + 1):
            sortarray.append(img_input[i + x, j + y])

    sortarray.sort()
    z_min = sortarray[0]
    z_med = sortarray[int((num - 1) / 2)]
    z_max = sortarray[num - 1]
    z_xy = img_input[i, j]

    if z_min < z_med < z_max:
        if z_min < z_xy < z_max:
            return z_xy
        else:
            return z_med
    else:
        filter_size += 2
        if filter_size <= size_max:
            return adaptive_median(img_input, i, j, filter_size, size_max)
        else:
            return z_med

def adaptive_median_filter(img_input, size_max):
    img_output = img_input.copy()
    img_input = cv2.copyMakeBorder(img_input, int((size_max - 1) / 2), int((size_max - 1) / 2), int((size_max - 1) / 2), int((size_max - 1) / 2), cv2.BORDER_REFLECT)

    for i in range(int((size_max - 1) / 2), img_input.shape[0] - int((size_max - 1) / 2)):
        for j in range(int((size_max - 1) / 2), img_input.shape[1] - int((size_max - 1) / 2)):
            img_output[i - int((size_max - 1) / 2), j - int((size_max - 1) / 2)] = adaptive_median(img_input, i, j, 3, size_max)

    return img_output

if __name__ == "__main__":
    image = cv2.imread("test.jpg", cv2.IMREAD_GRAYSCALE)
    if image is None:
        print("读取错误")
        exit()

    cv2.imshow("image", image)
    image_salt = salt(image.copy(), 10000)
    cv2.imshow("image_salt", image_salt)
    image_output = adaptive_median_filter(image_salt, 7)
    cv2.imshow("image_output", image_output)
    cv2.waitKey(0)
