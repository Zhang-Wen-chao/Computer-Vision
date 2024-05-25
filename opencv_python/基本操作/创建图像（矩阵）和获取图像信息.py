import cv2

image1 = cv2.imread("test.jpg")
if image1 is None:
    print("读取错误")
    exit()

cv2.imshow("image1", image1)
print("图像的行数为：", image1.shape[0])
print("图像的列数为：", image1.shape[1])
print("图像的通道数为：", image1.shape[2])
print("图像的尺寸为：", image1.shape[0:2])
cv2.waitKey(0)
cv2.destroyAllWindows()
