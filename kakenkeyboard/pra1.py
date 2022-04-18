
import cv2
import matplotlib.pyplot as plt

# 画像の読み込み
img = cv2.imread('imagefile/tryout/sample_video_img_0070.jpg') 
# カラーデータの色空間の変換 
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB)) 
print(img.shape)
# 画像の表示
plt.show()
