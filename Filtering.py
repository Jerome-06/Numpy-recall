import numpy as np

# Filtering = Refers to the process of selecting specific elements
#             from an array that matches the current condition.


ages= np.array([[21,25,45,12,55,63,15],[18,22,30,28,40,19,17]])

"""
teenagers = ages [(ages <18)|(ages ==18)]
adults = ages [(ages >=18) & (ages <=40)]
seniors = ages [ages >40]
evens = ages [ages % 2 == 0]
print(teenagers)
print(adults)
print(seniors)
print(evens)
"""
adults = np.where(ages >= 18,ages,"-") # if the condition is true, return the value in ages, otherwise return "-"
print(adults)