
import numpy as np
import statistics
from music21 import *
output = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],['C4'],['C4'],['C4'],['C4'],['C4'],['C4'],['C4'],['C4'],[],[],[],[],[],[],[],[],['C4'],['C4'],['C4'],['C4'],['C4'],['C4'],['C4'],['C4'],['C4'],['C4'],['C4'],[],[],[],[],[],['G4'],['G4'],['G4'],['G4'],['G4'],['G4'],['G4'],['G4'],['G4'],['G4'],[],[],[],[],[],[],['G4'],['G4'],['G4'],['G4'],['G4'],['G4'],['G4'],['G4'],['G4'],['G4'],[],[],[],[],[],[],['A4'],['A4'],['A4'],['A4'],['A4'],['A4'],['A4'],['A4'],['A4'],['A4'],['A4'],[],[],[],[],[],[],['A4'],['A4'],['A4'],['A4'],['A4'],['A4'],['A4'],['A4'],['A4'],['A4'],['A4'],['A4'],['A4'],[],[],[],[],[],['G4'],['G4'],['G4'],['G4'],['G4'],['G4'],['G4'],['G4'],['G4'],['G4'],['G4'],['G4'],['G4'],['G4'],['G4'],['G4'],['G4'],['G4'],['G4'],['G4'],[],[],[],[],[],[],[],[],[],[],[],['F4'],['F4'],['F4'],['F4'],['F4'],['F4'],['F4'],['F4'],['F4'],['F4'],['F4'],[],[],[],[],[],['F4'],['F4'],['F4'],['F4'],['F4'],['F4'],['F4'],['F4'],['F4'],['F4'],['F4'],[],[],[],[],[],[],[],['E4'],['E4'],['E4'],['E4'],['E4'],['E4'],['E4'],['E4'],['E4'],[],[],[],[],[],[],[],[],[],['E4'],['E4'],['E4'],['E4'],['E4'],['E4'],['E4'],['E4'],['E4'],[],[],[],[],[],[],[],['D4'],['D4'],['D4'],['D4'],['D4'],['D4'],['D4'],['D4'],['D4'],['D4'],['D4'],['D4'],[],[],[],[],[],['D4'],['D4'],['D4'],['D4'],['D4'],['D4'],['C4'],['C4'],['C4'],['D4'],['D4'],[],[],[],[],[],[],[],['C4'],['C4'],['C4'],['C4'],['C4'],['C4'],['C4'],['C4'],['C4'],['C4'],['C4'],['C4'],['C4'],['C4'],['C4'],['C4'],['C4'],['C4'],['C4'],['C4'],['C4'],['C4'],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],
]
outputs = [[],[],[],[],[],['D4'],['D4'],['D4'],['D4'],['D4'],['D4'],['D4'],[],[],[],[],[],[],[],[],[],[],[],[],['D4'],['D4'],['D4'],['D4'],['D4'],['D4'],['D4'],[]]
Musicscore = []
i = 0
j = 1
k = 0
n = 0
t = 0
def Rest(k,x):
    Musicscore[k][0] = '休符'
    Musicscore[k][1] = x
def Sound(k,t,j,x):
    Musicscore[k][2*t] = output[j-1][t]
    Musicscore[k][2*t+1] = x
def appending(t):
    if t == 1:
        Musicscore.append([0,0])
    elif t == 2:
        Musicscore.append([0,0,0,0])
    elif t == 3:
        Musicscore.append([0,0,0,0,0,0])
    elif t == 4:
        Musicscore.append([0,0,0,0,0,0,0,0])
    elif t == 5:
        Musicscore.append([0,0,0,0,0,0,0,0,0,0])

while output[0] == []:
    output.remove([])

BPM = 140
for j in range(1,len(output)):
    if output[j-1] == output[j]:
        n += 1
    elif output[j-1] == []:
        n += 1
        if (n > 900/BPM*0.8) & (n < 900/BPM*1.5):
            Musicscore.append([0,0])
            Rest(k,0.5)
            n = 0
            k += 1
        elif ((n == 900/BPM*1.5) | (n > 900/BPM*1.5)) & (n < 900/BPM*3):
            Musicscore.append([0,0])
            Rest(k,1)
            n = 0
            k += 1
        elif ((n == 900/BPM*3) | (n > 900/BPM*3)) & (n < 900/BPM*6):
            Musicscore.append([0,0])
            Rest(k,2)
            n = 0
            k += 1
        elif ((n == 900/BPM*6) | (n > 900/BPM*6)) & (n < 900/BPM*10):
            Musicscore.append([0,0])
            Rest(k,4)
            n = 0
            k += 1
    #音の処理
    else:
        n += 1
        if (n > 900/BPM*0.8) & (n < 900/BPM*1.5):
            appending(len(output[j-1]))
            for t in range(len(output[j-1])):
                Sound(k,t,j,0.5)
            k += 1
            n = 0
            t = 0
        elif ((n == 900/BPM*1.5) | (n > 900/BPM*1.5)) & (n < 900/BPM*3):
            appending(len(output[j-1]))
            for t in range(len(output[j-1])):
                Sound(k,t,j,1)
            k += 1
            n = 0
            t = 0
        elif ((n == 900/BPM*3) | (n > 900/BPM*3)) & (n < 900/BPM*6):
            appending(len(output[j-1]))
            for t in range(len(output[j-1])):
                Sound(k,t,j,2)
            k += 1
            n = 0
            t = 0
        elif ((n == 900/BPM*6) | (n > 900/BPM*6)) & (n < 900/BPM*10):
            appending(len(output[j-1]))
            for t in range(len(output[j-1])):
                Sound(k,t,j,4)
            k += 1
            n = 0
            t = 0

noteList = []


#print(Musicscore)

for c,num in Musicscore :
    if c=='休符':
        n=note.Rest(quarterLength = num)
    else:
        n = note.Note(c, quarterLength = num)
    noteList.append(n)


meas = stream.Measure()
meas.append(noteList)
meas.show()







