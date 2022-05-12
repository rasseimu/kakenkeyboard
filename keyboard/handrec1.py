import cv2
from PIL import Image, ImageOps
import numpy as np
import matplotlib.pyplot as plt
#画像の読み込み
img = cv2.imread('./imagefile/pianoCE.jpg')
#座標入力
#pts1はカードの4辺、pts2は変換後の座標
pts1 = np.float32([[32,519], [1906,508], [34, 848], [1910, 829]])
pts2 = np.float32([[0,0], [1850,0], [0,400], [1850,400]])
#射影変換を実施
M = cv2.getPerspectiveTransform(pts1, pts2)
dst = cv2.warpPerspective(img, M, (1850, 400))
#ファイル書き出し
cv2.imwrite("./card_result.jpg", dst)

img = cv2.imread('./imagefile/pianoN.jpg')
#座標入力
#pts1はカードの4辺、pts2は変換後の座標
pts1 = np.float32([[33,482], [1901,475], [27, 806], [1911, 801]])
pts2 = np.float32([[0,0], [1850,0], [0,400], [1850,400]])
#射影変換を実施
M = cv2.getPerspectiveTransform(pts1, pts2)
dst = cv2.warpPerspective(img, M, (1850, 400))
#ファイル書き出し
cv2.imwrite("card_N.jpg", dst)

"""
cv2.imshow('image1',dst)
cv2.waitKey(0)
"""

#肌の検出
img=cv2.imread("./card_result.jpg")
img_YCrCb = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
YCrCb_mask = cv2.inRange(img_YCrCb, (80, 145, 85), (255,180,135))
YCrCb_mask = cv2.morphologyEx(YCrCb_mask, cv2.MORPH_OPEN, np.ones((3,3), np.uint8))


 # アパーチャーサイズ 3, 5, or 7 など 1 より大きい奇数。数値が大きいほどぼかしが出る。
ksize=3
#中央値フィルタ
img_mask = cv2.medianBlur(YCrCb_mask,ksize)

cv2.imshow("mask",img_mask)

cv2.imwrite("./YCbCr.jpg",img_mask)

# 画像を読み込む。
fg_img = cv2.imread('./YCbCr.jpg')

# 背景画像を読み込む。
bg_img = cv2.imread("./card_N.jpg")

fg_img = cv2.bitwise_not(fg_img)
bg_img = cv2.bitwise_not(bg_img)

dst1 = bg_img * fg_img

#dst = cv2.imread("./out.jpg")
cv2.imwrite("./diff1.jpg",dst1)
cv2.imshow("dif1",dst1)
cv2.waitKey(0)
bg_img = cv2.imread("./card_result.jpg")
bg_img = cv2.bitwise_not(bg_img)
dst2 = bg_img * fg_img
cv2.imwrite("./diff2.jpg",dst2)
cv2.imshow("dif2",dst2)
cv2.waitKey(0)
#ここまでできた。結構手はきれいに隠してる
#ここから画像の比較
img_1 = cv2.imread('./diff1.jpg',1)
img_2 = cv2.imread('./diff2.jpg',1)
img_1_gray = cv2.cvtColor(img_1, cv2.COLOR_BGR2GRAY)
img_2_gray = cv2.cvtColor(img_2, cv2.COLOR_BGR2GRAY)

#画像を引き算
img_diff = cv2.absdiff(img_1_gray, img_2_gray)

#2値化
ret2,img_th = cv2.threshold(img_diff,20,255,cv2.THRESH_BINARY)

#輪郭を検出
contours, hierarchy = cv2.findContours(img_th, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

#閾値以上の差分を四角で囲う
for i,cnt in enumerate(contours):
    x, y, width, height = cv2.boundingRect(cnt)
    if width > 50 or height > 50:
        cv2.rectangle(img_1, (x, y), (x+width, y+height), (0, 0, 255), 1)

cv2.imwrite("diff.jpg", img_1)
cv2.imshow("diff",img_1)
cv2.waitKey(0)
