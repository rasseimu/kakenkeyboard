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

BPM = 0

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
    





