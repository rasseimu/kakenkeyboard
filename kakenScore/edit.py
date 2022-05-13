#鍵盤の数を6と仮定
import numpy as np
arr=[[0,0,0],[0,0,1,],[0,0,1],[0,0,1],[0,0,1]]
arr_t=np.array(arr).T.tolist()
l=len(arr_t)
print(arr_t)
print(arr_t.count('1'))