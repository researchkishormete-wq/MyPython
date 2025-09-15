"""
A group took a trip on a bus, at Rs. 3 per child and Rs. 3.20 per adult
for a total of Rs. 118.40.
They took the train back at Rs. 3.50 per child and Rs. 3.60 per adult
for a total of Rs. 135.20.
How many children, and how many adults?
"""
import numpy as np
from numpy.linalg import inv
A = np.array([[3.0, 3.5], 
              [3.2, 3.6]])
B = np.array([118.4, 135.2])

print(A)
print(B)
invA=inv(A)
X = B.dot(invA)
print(X)
