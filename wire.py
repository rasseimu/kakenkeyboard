import numpy as np
import statistics
output = [[],
[],
[],
[],
[],
[],
[],
[],
[],
[],
[],
[],
[],
[],
[],
[],
[],
[],
[],
[],
[],
[],
[],
[],
['C4'],
['C4'],
['C4'],
['C4'],
['C4'],
['C4'],
['C4'],
['C4'],
[],
[],
[],
[],
[],
[],
[],
[],
['C4'],
['C4'],
['C4'],
['C4'],
['C4'],
['C4'],
['C4'],
['C4'],
['C4'],
['C4'],
['C4'],
[],
[],
[],
[],
[],
['G4'],
['G4'],
['G4'],
['G4'],
['G4'],
['G4'],
['G4'],
['G4'],
['G4'],
['G4'],
[],
[],
[],
[],
[],
[],
['G4'],
['G4'],
['G4'],
['G4'],
['G4'],
['G4'],
['G4'],
['G4'],
['G4'],
['G4'],
[],
[],
[],
[],
[],
[],
['A4'],
['A4'],
['A4'],
['A4'],
['A4'],
['A4'],
['A4'],
['A4'],
['A4'],
['A4'],
['A4'],
[],
[],
[],
[],
[],
[],
['A4'],
['A4'],
['A4'],
['A4'],
['A4'],
['A4'],
['A4'],
['A4'],
['A4'],
['A4'],
['A4'],
['A4'],
['A4'],
[],
[],
[],
[],
[],
['G4'],
['G4'],
['G4'],
['G4'],
['G4'],
['G4'],
['G4'],
['G4'],
['G4'],
['G4'],
['G4'],
['G4'],
['G4'],
['G4'],
['G4'],
['G4'],
['G4'],
['G4'],
['G4'],
['G4'],
[],
[],
[],
[],
[],
[],
[],
[],
[],
[],
[],
['F4'],
['F4'],
['F4'],
['F4'],
['F4'],
['F4'],
['F4'],
['F4'],
['F4'],
['F4'],
['F4'],
[],
[],
[],
[],
[],
['F4'],
['F4'],
['F4'],
['F4'],
['F4'],
['F4'],
['F4'],
['F4'],
['F4'],
['F4'],
['F4'],
[],
[],
[],
[],
[],
[],
[],
['E4'],
['E4'],
['E4'],
['E4'],
['E4'],
['E4'],
['E4'],
['E4'],
['E4'],
[],
[],
[],
[],
[],
[],
[],
[],
[],
['E4'],
['E4'],
['E4'],
['E4'],
['E4'],
['E4'],
['E4'],
['E4'],
['E4'],
[],
[],
[],
[],
[],
[],
[],
['D4'],
['D4'],
['D4'],
['D4'],
['D4'],
['D4'],
['D4'],
['D4'],
['D4'],
['D4'],
['D4'],
['D4'],
[],
[],
[],
[],
[],
['D4'],
['D4'],
['D4'],
['D4'],
['D4'],
['D4'],
['C4'],
['C4'],
['C4'],
['D4'],
['D4'],
[],
[],
[],
[],
[],
[],
[],
['C4'],
['C4'],
['C4'],
['C4'],
['C4'],
['C4'],
['C4'],
['C4'],
['C4'],
['C4'],
['C4'],
['C4'],
['C4'],
['C4'],
['C4'],
['C4'],
['C4'],
['C4'],
['C4'],
['C4'],
['C4'],
['C4'],
[],
[],
[],
[],
[],
[],
[],
[],
[],
[],
[],
[],
[],
[],
[],
[],
[],
[],
[],
[],
[],
[],
[],
[],
[],
[],
[],
]
#output = [0,0,0,0,0,'D4','D4','D4','D4','D4','D4','D4',0,0,0,0,0,0,0,0,0,0,0,0]
Musicscore = []
for a in range(len(output)):
    Musicscore.append([0,0])
i = 0
j = 1
k = 0
n = 0
t = 0


def Rest(k,x):
    Musicscore[k][0] = '休符'
    Musicscore[k][1] = x

def SoloSound(k,j,x):
    Musicscore[k][0] = output[j-1]
    Musicscore[k][1] = x

def CoSound(k,t,j,x):
    Musicscore[k][2*t] = output[j-1][t]
    Musicscore[k][2*t+1] = x

#先頭要素"0"の削除
while output[0] == []:
    output.remove([])



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
for j in range(1,len(output)):#貰った配列の長さ
    #同一音の継続
    if output[j-1] == output[j]:
        n += 1

    #単音の場合の処理
    elif not isinstance(output[j-1], list):
        n += 1
        if (n > 900/BPM*0.8) & (n < 900/BPM*1.5):
            
            if output[j-1] == []:
                Rest(k,0.5)
            else:
                SoloSound(k,j,0.5)
            n = 0
            k += 1
        
        elif ((n == 900/BPM*1.5) | (n > 900/BPM*1.5)) & (n < 900/BPM*3):
            if output[j-1] == []:
                Rest(k,1)
            else:
                SoloSound(k,j,1)
            n = 0
            k += 1
        
        elif ((n == 900/BPM*3) | (n > 900/BPM*3)) & (n < 900/BPM*6):
            if output[j-1] == []:
                Rest(k,2)
            else:
                SoloSound(k,j,2)
            n = 0
            k += 1

        elif ((n == 900/BPM*6) | (n > 900/BPM*6)) & (n < 900/BPM*10):
            if output[j-1] == []:
                Rest(k,4)
            else:
                SoloSound(k,j,4)
            n = 0
            k += 1


    #複音の場合の処理
    else:
        n += 1
        if (n > 900/BPM*0.8) & (n < 900/BPM*1.5):
            for t in range(len(output[j-1])):
                CoSound(k,t,j,0.5)
            k += 1
            n = 0
            t = 0
        
        elif ((n == 900/BPM*1.5) | (n > 900/BPM*1.5)) & (n < 900/BPM*3):
            for t in range(len(output[j-1])):
                CoSound(k,t,j,1)
            k += 1
            n = 0
            t = 0
        
        elif ((n == 900/BPM*3) | (n > 900/BPM*3)) & (n < 900/BPM*6):
            for t in range(len(output[j-1])):
                CoSound(k,t,j,2)
            k += 1
            n = 0
            t = 0
        
        elif ((n == 900/BPM*6) | (n > 900/BPM*6)) & (n < 900/BPM*10):
            for t in range(len(output[j-1])):
                CoSound(k,t,j,4)
            k += 1
            n = 0
            t = 0



print(Musicscore)
