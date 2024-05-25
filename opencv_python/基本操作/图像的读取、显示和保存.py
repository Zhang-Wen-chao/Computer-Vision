import cv2

# 读取图像
image = cv2.imread("test.jpg")

# 检测图像是否加载成功
if image is None:
    print("Could not open or find the image")
    exit()

# 显示图像
cv2.imshow("IMAGE", image)

# 保存图像为png格式，文件名称为1
cv2.imwrite("1.png", image)

# 暂停，保持图像显示，等待按键结束
cv2.waitKey(0)
cv2.destroyAllWindows()
