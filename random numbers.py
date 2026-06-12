import numpy as np

rng = np.random.default_rng(seed=2) # Create a random number generator with a specific seed for reproducibility
""" 
print(rng.integers(1,10)) # Generate a random integer between 1 and 9 (inclusive)
print(rng.random()) # Generate a random float between 0 and 1
print(rng.integers(low=1,high=102,size=(3,2))) # Generate a 3x2 array of random integers between 1 and 101 (inclusive)
print(rng.normal(loc=0,scale=1,size=(3,2))) # Generate a 3x2 array of random floats from a normal distribution with mean 0 and standard deviation 

print(np.random.uniform(low=0.0, high=1.0, size=(3,2))) # Generate a 3x2 array of random floats from a uniform distribution between 0 and 1
"""

array=np.array([1,2,3,4])
rng.shuffle(array)
print(array)

fruits = np.array(['apple', 'banana', 'cherry', 'date'])
print(rng.choice(fruits))