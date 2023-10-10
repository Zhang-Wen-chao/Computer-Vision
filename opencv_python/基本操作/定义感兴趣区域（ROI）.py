import cv2

image1 = cv2.imread("test.jpg")
if image1 is None:
    print("读取错误")
    exit()

cv2.imshow("image1", image1)
imageROI = image1[0:10, 0:10]
cv2.imshow("ROI", imageROI)
cv2.waitKey(0)
cv2.destroyAllWindows()
