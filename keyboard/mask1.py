#!/usr/bin/env python
# coding: utf-8

# In[82]:


import cv2
import matplotlib.pyplot as plt
import numpy as np
from IPython import display


# In[83]:


# マスク用単一色画像を作成
height = 100 # 生成画像の高さ
width = 100 # 生成画像の幅
imgMask = np.full((height, width, 1), 1, dtype=np.uint8)



# マスク範囲を四角形で描画
boxFromX = 2 #マスク範囲開始位置 X座標
boxFromY = 50 #マスク範囲開始位置 Y座標
boxToX = 98 #マスク範囲終了位置 X座標
boxToY = 70 #マスク範囲終了位置 Y座標
cv2.rectangle(imgMask, (boxFromX, boxFromY), (boxToX, boxToY),(255), cv2.FILLED)

img_resize = cv2.resize(imgMask, dsize=[1920,1080], fx=None, fy=None)

# マスク結果画像を保存
cv2.imwrite("./imagefile/testMaskImg.jpg", img_resize)
plt.imshow(img_resize)


# In[84]:


white=cv2.imread("./imagefile/white.jpg",cv2.IMREAD_COLOR)
im_mask = cv2.imread('./imagefile/testMaskImg.jpg')
white_resize = cv2.resize(white, dsize=[1920,1080], fx=None, fy=None)
im_out = cv2.bitwise_and(white_resize, im_mask)
cv2.imwrite('./imagefile/whitemask.jpg', im_out)
plt.imshow(im_out)


# In[85]:


black=cv2.bitwise_not(im_out)
plt.imshow(black)
cv2.imwrite("./imagefile/blackmask.jpg",black)


# In[86]:


im_1 = cv2.imread('./imagefile/pianoCE1.jpg', cv2.IMREAD_COLOR)
im_mask = cv2.imread('./imagefile/blackmask.jpg')
plt.imshow(im_1)
plt.imshow(im_mask)
im_out = cv2.bitwise_or(im_1, im_mask)
cv2.imwrite('./imagefile/out.jpg', im_out)
plt.imshow(im_out)


# In[87]:


def imshow(img, format=".jpg", **kwargs):
    """ndarray 配列をインラインで Notebook 上に表示する。
    """
    img = cv2.imencode(format, img)[1]
    img = display.Image(img, **kwargs)
    display.display(img)


# 画像を読み込む。
img = cv2.imread("./imagefile/out.jpg")
imshow(img)

#ここまではうまくいってる


# In[88]:




# グレースケールに変換する。
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 2値化する
ret, bin_img = cv2.threshold(gray, 55, 255, cv2.THRESH_BINARY)
print(ret)
cv2.imwrite("./imagefile/mask_pianoCE1.jpg",bin_img)
imshow(bin_img)


# In[89]:


# 輪郭を抽出する。
contours, hierarchy = cv2.findContours(
    bin_img, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE
)

# 小さい輪郭は誤検出として削除する
contours = list(filter(lambda x: cv2.contourArea(x) > 100, contours))

# 輪郭を描画する。
cv2.drawContours(img, contours, -1, color=(0, 0, 255), thickness=2)
imshow(img)
cv2.imwrite("./imagefile/mask_pianoCE1.jpg",img)


# In[90]:


def draw_contours(ax, img, contours):
    ax.imshow(img)
    ax.set_axis_off()

    for i, cnt in enumerate(contours):
        # 形状を変更する。(NumPoints, 1, 2) -> (NumPoints, 2)
        cnt = cnt.squeeze(axis=1)
        # 輪郭の点同士を結ぶ線を描画する。
        ax.add_patch(plt.Polygon(cnt, color="b", fill=None, lw=2))
        # 輪郭の点を描画する。
        ax.plot(cnt[:, 0], cnt[:, 1], "ro", mew=0, ms=4)
        # 輪郭の番号を描画する。
        ax.text(cnt[0][0], cnt[0][1], i, color="r", size="20", bbox=dict(fc="w"))


fig, ax = plt.subplots(figsize=(8, 8))
draw_contours(ax, img, contours)

plt.show()
