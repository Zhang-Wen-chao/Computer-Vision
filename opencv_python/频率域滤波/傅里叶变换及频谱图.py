import cv2
import numpy as np

def My_DFT(input_image):
    # 1. 扩展图像矩阵，为2，3，5的倍数时运算速度快
    m = cv2.getOptimalDFTSize(input_image.shape[0])
    n = cv2.getOptimalDFTSize(input_image.shape[1])
    input_image = cv2.copyMakeBorder(input_image, 0, m - input_image.shape[0], 0, n - input_image.shape[1], cv2.BORDER_CONSTANT, value=0)

    # 2. 创建一个双通道矩阵planes，用来储存复数的实部与虚部
    planes = [np.float32(input_image), np.zeros(input_image.shape, np.float32)]
    
    # 3. 合并这两个通道以形成一个复数矩阵
    transform_image = cv2.merge(planes)

    # 4. 进行傅立叶变换
    cv2.dft(transform_image, transform_image)

    # 5. 计算复数的幅值，并保存为频谱图
    planes = cv2.split(transform_image)
    output_image = cv2.magnitude(planes[0], planes[1])

    # 6. 调整频谱图的尺度以便于显示
    output_image += 1
    output_image = np.log(output_image)
    cv2.normalize(output_image, output_image, 0, 1, cv2.NORM_MINMAX)

    # 7. 重新排列频谱图的象限，使原点位于图像的中心
    cx = output_image.shape[1] // 2
    cy = output_image.shape[0] // 2
    q0 = output_image[0:cy, 0:cx]
    q1 = output_image[0:cy, cx:]
    q2 = output_image[cy:, 0:cx]
    q3 = output_image[cy:, cx:]
    tmp = np.copy(q0)
    np.copyto(q0, q3)
    np.copyto(q3, tmp)
    tmp = np.copy(q1)
    np.copyto(q1, q2)
    np.copyto(q2, tmp)

    return output_image, transform_image

if __name__ == "__main__":
    image = cv2.imread("test.jpg")
    if image is None:
        print("读取错误")
        exit(-1)
    cv2.imshow("image", image)

    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow("image_gray", image_gray)

    image_output, image_transform = My_DFT(image_gray)
    cv2.imshow("image_output", image_output)

    cv2.waitKey(0)
