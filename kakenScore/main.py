
from music21 import *

noteList = []

words = ['C4','D4','E4','F4','G4','A4','B4','C5']

while True:
    
 i = int(input("num=:"))
 if i == -1:
  break
 m = float(input("dur=:"))
 s = words[i]
 n = note.Note(s, quarterLength = m)
 noteList.append(n)


meas = stream.Measure()
meas.append(noteList)
meas.show('midi')