import cv2
import numpy as np

eachdata_type = [( 'key' , 'U10' ),( 'num' , 'i4' ),( 'det' , 'U10' )]
eachdatas = np.array([('C',4,'half'),('D',4,'half')], dtype = eachdata_type)
print(eachdatas[0])
print(eachdatas[0]['key'])


eachdatas[0]['key'] = 'E'

print(eachdatas[0])
print(eachdatas[0]['key'])