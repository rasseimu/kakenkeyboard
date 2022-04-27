#-*- coding: UTF-8 -*-
from __future__ import unicode_literals
import youtube_dl
import glob
import cv2
import matplotlib.pyplot as plt
import os
from os import listdir


"""asking for url"""
morU = input('Enter mp4file name or youtube url')
morU1 = morU.split('.',1)


"""if youtube url"""
if morU1[0]=='https://www':
    ydl_opts = {}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([morU])

    findv = glob.glob("*.mp4")
    new_name = r"C:/Users/hp/kakenkeyboard/keyboard/piano1.mp4"
    os.rename(findv[0],new_name)

"""
else:
    if file uploaded"""


"""delete previous images"""
folder_path = 'C:/Users/hp/kakenkeyboard/keyboard/imagefile/tryout'

for file_name in listdir(folder_path):

    os.remove(folder_path + file_name)


"""video to images"""
def save_all_frames(video_path, dir_path, basename, ext='jpg'):
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        return

    os.makedirs(dir_path, exist_ok=True)
    base_path = os.path.join(dir_path, basename)

    digit = len(str(int(cap.get(cv2.CAP_PROP_FRAME_COUNT))))

    n = 0

    while True:
        ret, frame = cap.read()
        if ret:
            cv2.imwrite('{}_{}.{}'.format(base_path, str(n).zfill(digit), ext), frame)
            n += 1
        else:
            return
save_all_frames(new_name, folder_path , 'img')
