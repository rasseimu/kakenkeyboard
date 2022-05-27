#鍵盤の数を3と仮定
from re import I
from sys import exec_prefix
import numpy as np

arr=[[0,0,0],[0,0,1],[0,0,1],[0,0,1],[0,0,1]]#元のデータ
arr_n=np.array(arr).T#転地して各鍵盤ごとの出力
#print([len(v) for v in arr])
l=[len(v) for v in arr][1]#鍵盤の数を取得
#print(l)
i=0

for i in range(l):
    exec("arr_%d=arr_n[%d,:]"%(i,i))

#arr_(i)=(arr_n[i,:])
#print(arr_n)

def RLE_numpy(arr_1):
    comp_seq_index, = np.concatenate(([True], arr_1[1:] != arr_1[:-1], [True])).nonzero()
    return arr_1[comp_seq_index[:-1]], np.ediff1d(comp_seq_index)

print(RLE_numpy(arr_1))
