import numpy as np

array = np.array([[['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']],
                  [['J', 'K', 'L'], ['M', 'N', 'O'], ['P', 'Q', 'R']],
                  [['S', 'T', 'U'], ['V', 'W', 'X'], ['Y', 'Z', '!']]])

print(array.ndim) # number of dimensions
print(array.shape) # shape of the array
print(array.size) # total number of elements in the array

#print(array[0,1,2]) # accessing the element at index [0][1][2]

word=array[0,0,0]+array[1,1,1]+array[2,2,2] # concatenating the elements at index [0][0][0], [1][1][1], and [2][2][2
print(word)