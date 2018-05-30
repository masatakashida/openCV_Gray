import cv2
img = cv2.imread("src/umi.jpg", 0)
cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

