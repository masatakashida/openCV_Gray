import cv2
# グレースケールに変換
img = cv2.imread("src/umi.jpg", 0)
cv2.imshow("img", img)
# キーボード入力を処理する関数
cv2.waitKey(0)
# 作られたウィンドウを閉じる関数
cv2.destroyAllWindows()
