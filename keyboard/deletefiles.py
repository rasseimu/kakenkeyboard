from __future__ import unicode_literals
import youtube_dl
import glob
import cv2
import matplotlib.pyplot as plt
import os
from os import listdir

folder_path = 'C:\Users\hp\kakenkeyboard\keyboard\imagefile\tryout'

for file_name in listdir(folder_path):

    os.remove(folder_path + file_name)
