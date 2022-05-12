import cv2
#import matplotlib.pyplot as plt

filename = 'C:\Users\julee\Documents\GitHub\kakenkeyboard\kakenkeyboard\otameshi.jpg'

img = cv2.imread(filename)
cv2.imshow(img)
cv2.waitkey()