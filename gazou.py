import cv2
import numpy as np
from IPython import display
from matplotlib import pyplot as plt


def imshow(img, format=".jpg", **kwargs):

    img = cv2.imencode(format, img)[1]
    img = display.Image(img, **kwargs)
    display.display(img)

img = cv2.imread("C:\Users\julee\Documents\GitHub\kakenkeyboard\kakenkeyboard\otameshi.jpg")

img_crop = img.crop((400, 150, 1700, 1500))#切り出し
img_crop.save('sample_crop.jpg', quality=95)#保存