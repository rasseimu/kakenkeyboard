import numpy as np
sequence=np.array([1,1,1,1,1,1,1,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0])
def RLE_numpy(sequence):

    diff_seq = np.diff(sequence) # sequence[i+1] - sequence[i]のアレイ。隣と同じだと0になる。

    # newdata は、前の要素とインデックスが違うときだけTrueになるBoolのアレイ。
    newdata = np.append(True, diff_seq != 0) # 先頭をTrueにして、2番目以降をappendで追加している。
    comp_seq = sequence[newdata]  # sequence から、newdataがTrueの要素だけ抜き出す

    comp_seq_index = np.where(newdata)[0]  # newdataがTrueの要素が、アレイの何番目に来るか取得
    comp_seq_index = np.append(comp_seq_index, len(sequence))  # アレイの終了をつける
    lengths = np.diff(comp_seq_index) # newdataがTrueになっている位置の差がlengthになる

    return comp_seq, lengths

print(RLE_numpy(sequence))