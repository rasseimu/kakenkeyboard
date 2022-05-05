from music21 import *
i = input("key=:")
r = input("num=:")
x = i+r
print(x)
s = note.Note(x)
s.show('midi')