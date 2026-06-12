import numpy as np
array=np.array([[1,2,3,4],
                [5,6,7,8],
                [9,10,11,12],
                [13,14,15,16]])


#Array[start:stop:step]
print(array[0:4:2])    #Row selection

print(array[:,::-1])    # Column selection 
 
print(array[2:4,0:2])    # Subarray selection