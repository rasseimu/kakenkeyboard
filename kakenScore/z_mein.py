
from music21 import *

noteList = []

words = ['C4','D4','E4','F4','G4','A4','B4','C5']
for i in words:

    n = note.Note(i,quarterLength = 1)
    noteList.append(n)


meas = stream.Measure()
meas.append(noteList)
meas.show()