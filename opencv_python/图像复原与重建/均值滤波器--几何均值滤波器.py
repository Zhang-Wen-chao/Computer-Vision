import cv2
import numpy as np

def geometric_mean_filter(img_input, m, n):
    # 扩展图像边缘，扩展方法为镜像
    img_input = cv2.copyMakeBorder(img_input, (m-1)//2, (m-1)//2, (n-1)//2, (n-1)//2, cv2.BORDER_REFLECT)
    img_output = np.zeros_like(img_input)

    # 几何均值滤波
    k = m * n
    for i in range((m-1)//2, img_input.shape[0] - (m-1)//2):
        for j in range((n-1)//2, img_input.shape[1] - (n-1)//2):
            Sum = np.sum(np.log10(img_input[i-(m-1)//2:i+(m-1)//2+1, j-(n-1)//2:j+(n-1)//2+1] + 0.1))
            Sum = Sum / k
            img_output[i, j] = round(10**Sum)

    # 裁剪图像以移除扩展的边缘
    img_output = img_output[(m-1)//2:-(m-1)//2, (n-1)//2:-(n-1)//2]
    return img_output

if __name__ == "__main__":
    image = cv2.imread("test.jpg", cv2.IMREAD_GRAYSCALE)
    if image is None:
        print("读取错误")
        exit(-1)

    cv2.imshow("image", image)

    # 使用自定义的几何均值滤波函数
    image_output = geometric_mean_filter(image, 7, 7)
    cv2.imshow("image_output", image_output)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
