#-*- coding: UTF-8 -*-
from __future__ import unicode_literals
import youtube_dl
import glob
import cv2
import matplotlib.pyplot as plt
import os
from os import listdir
import numpy as np
import statistics

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

"""delete previous images"""

def main():
    data_dir_path = u"./keyboard/imagefile/tryout/"
    file_list = os.listdir(r'./keyboard/imagefile/tryout/')

    for file_name in file_list:
        root, ext = os.path.splitext(file_name)
        if ext == u'.png' or u'.jpeg' or u'.jpg':
            abs_name = data_dir_path + '/' + file_name
            
            os.remove(abs_name)

main()

"""asking for url"""
morU = input('Enter mp4file name or youtube url'+"\n")
morU1 = morU.split('.',1)


"""if youtube url"""
if morU1[0]=='https://www':
    ydl_opts = {}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([morU])

    findv = glob.glob("*.mp4")
    new_name = r"./keyboard/before/piano1.mp4"
    os.rename(findv[0],new_name)
    save_all_frames(r"./keyboard/before/piano.mp4", "./keyboard/imagefile/tryout" , 'img')

else:
    save_all_frames(morU, "./keyboard/imagefile/tryout" , 'img')

#写真配列、音符配列
output = []
Musicscore = []
i = 0
j = 1
k = 0
n = 0
def Rest(x):
    Musicscore[k][0] = """休符"""
    Musicscore[k][1] = x
def Sound(x):
    Musicscore[k][0] = output[j-1]
    Musicscore[k][1] = x

#先頭要素"0"の削除
while output[i] == 0:
    output.remove(0)
    i += 1

#写真配列を長さ配列に変更

#BPM
a=[2,1,1,1,3,4,5,6,32,7,45,2,4,3,3,2,2,2,3,4,5,]
#b=np.average(a) #平均値

#print(b)

c=statistics.mode(a)

#print(c)

BPM=1800/c

#print(BPM)


#配列変更の処理
for j in output:#貰った配列の長さ
    if output[j-1] == output[j]:
        n += 1
    else:
        if n > 900/BPM*0.8 & n < 900/BPM*1.5:
            if output[j-1] == 0:
                Rest(0.5)
            else:
                Sound(0.5)
        
        elif n == 900/BPM*1.5 | n > 900/BPM*1.5 & n < 900/BPM*3:
            if output[j-1] == 0:
                Rest(1)
            else:
                Sound(1)
        
        elif n == 900/BPM*3 | n > 900/BPM*3 & n < 900/BPM*6:
            if output[j-1] == 0:
                Rest(2)
            else:
                Sound(2)
        
        elif n == 900/BPM*6 | n > 900/BPM*6 & n < 900/BPM*10:
            if output[j-1] == 0:
                Rest(4)
            else:
                Sound(4)

    k += 1  
    n = 0 
    
