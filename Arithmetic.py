import numpy as np

#Scalar arithmetic

array = np.array([1,2,3])
print(array+1) # adding a scalar to an array
print(array-1) # subtracting a scalar from an array
print(array*2) # multiplying an array by a scalar
print(array/2) # dividing an array by a scalar
print(array**2) # raising an array to the power of a scalar
print(array%2) # modulus of an array by a scalar

#vectorized math function
print(np.sqrt(array)) # square root of each element in the array
print(np.exp(array)) # exponential of each element in the array
print(np.log(array)) # natural logarithm of each element in the array
print(np.sin(array)) # sine of each element in the array
#Element-wise arithmetic
array1=np.array([1,2,3])
array2=np.array([4,5,6])

print(array1+array2) # adding two arrays element-wise
print(array1-array2) # subtracting two arrays element-wise
print(array1*array2) # multiplying two arrays element-wise  
print(array1/array2) # dividing two arrays element-wise     
print(array1**array2) # raising one array to the power of another array element-wise

#comparison Operators
Scores=np.array([85,90,78,92,88])
print(Scores>80) # returns a boolean array where each element is True if the condition
print(Scores==90) # returns a boolean array where each element is True if the condition
print(Scores<85) # returns a boolean array where each element is True if the condition
