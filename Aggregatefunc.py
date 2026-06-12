import numpy as np

# Aggregate functions = summarize data and typically 
#                       return a single value as a result.

array = np.array([[1,2,3,4,5],[6,7,8,9,10]])
#print(np.sum(array)) # sum of all elements in the array  
# print(np.mean(array)) # mean of all elements in the array
# print(np.median(array)) # median of all elements in the array     
# print(np.min(array)) # minimum value in the array
# print(np.max(array)) # maximum value in the array
#  print(np.std(array)) # standard deviation of all elements in the array
# print(np.var(array)) # variance of all elements in the array
# print(np.argmin(array)) # index of the minimum value in the array
# print(np.argmax(array)) # index of the maximum value in the array


print(np.sum(array,axis=0))
print(np.sum(array,axis=1))
