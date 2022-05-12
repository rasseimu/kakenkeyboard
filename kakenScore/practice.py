from music21 import *
from numpy import half
s = stream.Score(id='mainScore')
p0 = stream.Part(id='part0')
p1 = stream.Part(id='part1')

m01 = stream.Measure(number=1)
m01.append(note.Note('G', type="whole"))
m02 = stream.Measure(number=2)
m02.append(note.Note('E', type="whole"))

p0.append([m01, m02])

m10 = stream.Measure(number=1)
m10.append(note.Note('C', type="whole"))
m11 = stream.Measure(number=2)
m11.append(note.Note('G', type="whole"))
p1.append([m10, m11])
          
s.insert(0, p0)
s.insert(0, p1)
s.show('midi')