import cv2
import matplotlib.pyplot as plt

image_path = "imagefile/tryout/sample_video_img_0070.jpg" # 画像のパス

img = cv2.imread(image_path)
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

plt.imshow(img,'gray')

plt.hist(img.flatten(), 256, [0,256]);

print(img.shape)