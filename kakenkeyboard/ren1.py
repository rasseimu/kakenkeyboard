import cv2
import matplotlib.pyplot as plt

image_path = "./image.jpg" # 画像のパス

img = cv2.imread(image_path)
plt.imshow(img)