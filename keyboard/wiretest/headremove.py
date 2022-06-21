import numpy as np
output = [0,0.0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,3]
i = 0

print(output)
print('do')

#先頭要素"0"の削除
while output[0] == 0:
    output.remove(0)
    print(output)

print('answer')
print(output)