import cv2
import numpy as np

# 读取图像
image = cv2.imread("test.jpg")
if image is None:
    print("读取错误")
    exit()

# 转换为灰度图像
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("image_gray", image_gray)

# 计算直方图
histsize = 256
hist = cv2.calcHist([image_gray], [0], None, [histsize], [0, 256])

# 创建直方图显示图像
hist_h = 300
hist_w = 512
bin_w = int(hist_w / histsize)
histImage = np.zeros((hist_h, hist_w, 3), dtype=np.uint8)

# 归一化直方图并绘制
cv2.normalize(hist, hist, alpha=0, beta=hist_h, norm_type=cv2.NORM_MINMAX)
for i in range(1, histsize):
    cv2.line(histImage, (bin_w * (i - 1), hist_h - int(hist[i - 1])),
             (bin_w * i, hist_h - int(hist[i])), (255, 0, 0), thickness=2)

cv2.imshow("histImage", histImage)

# 保存直方图图像
cv2.imwrite("histogram_output.png", histImage)

cv2.waitKey(0)
cv2.destroyAllWindows()
