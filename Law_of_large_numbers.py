import numpy as np
from numpy.random import randn

n = 100
counter = 0

for x in randn(n):
    if x<1 and x>-1:
        counter = counter + 1 

answer = counter/n
print(counter)
print(answer)