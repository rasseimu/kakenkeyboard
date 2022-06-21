import numpy as np
import statistics
output = [0,0,0,0,0,0,0,0,0,0,0,'C4','C4','C4','C4','C4','C4','D4','D4','D4','D4','D4','D4','D4','D4','D4','D4','D4',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'C3','C3','C3','C3','C3','C3','C3','C3','C3','C3','C3','C3','C3','C3',0,0,0,0,0,0,0,0,0,0]
Musicscore = []
i = 0
j = 1
k = 0
n = 0
t = 0


def Rest(k,x):
    Musicscore[k][0] = """休符"""
    Musicscore[k][1] = x

def Sound(k,t,j,x):
    Musicscore[k][2*t] = output[j-1][t]
    Musicscore[k][2*t+1] = x

#先頭要素"0"の削除
while output[0] == 0:
    output.remove(0)



#BPM
#output = []
#b=np.average(a) #平均値

#print(b)

#c=statistics.mode(output)

#print(c)

#BPM=1800/c

#print(BPM)

BPM = 120


#配列変更の処理
for j in range(len(output)):#貰った配列の長さ
    #同一音の継続
    if output[j-1] == output[j]:
        n += 1

    #単音の場合の処理
    elif output[j-1][1] == None:#配列に宣言されいないところを指定してはいけない。
        if n > 900/BPM*0.8 & n < 900/BPM*1.5:
            if output[j-1] == 0:
                Rest(k,0.5)
            else:
                Sound(k,0,j,0.5)
        
        elif n == 900/BPM*1.5 | n > 900/BPM*1.5 & n < 900/BPM*3:
            if output[j-1] == 0:
                Rest(k,1)
            else:
                Sound(k,0,j,1)
        
        elif n == 900/BPM*3 | n > 900/BPM*3 & n < 900/BPM*6:
            if output[j-1] == 0:
                Rest(k,2)
            else:
                Sound(k,0,j,2)
        
        elif n == 900/BPM*6 | n > 900/BPM*6 & n < 900/BPM*10:
            if output[j-1] == 0:
                Rest(k,4)
            else:
                Sound(k,0,j,4)

        n = 0

    #複音の場合の処理
    else:
        if n > 900/BPM*0.8 & n < 900/BPM*1.5:
            for t in output[j-1]:
                Sound(k,t,j,0.5)
        
        elif (n == 900/BPM*1.5 | n > 900/BPM*1.5) & n < 900/BPM*3:
            for t in output[j-1]:
                Sound(k,t,j,1)
        
        elif (n == 900/BPM*3 | n > 900/BPM*3) & n < 900/BPM*6:
            for t in output[j-1]:
                Sound(k,t,j,2)
        
        elif (n == 900/BPM*6 | n > 900/BPM*6) & n < 900/BPM*10:
            for t in output[j-1]:
                Sound(k,t,j,4)

        t = 0
        n = 0



    k += 1  

print(Musicscore)
