"""
The local shop sells 3 types of pies.
•   Apple pies cost $3 each
•   Cherry pies cost $4 each
•   Blueberry pies cost $2 each
And this is how many they sold in 4 days:
Apples 13 , 9, 7, 15
Cherry 8 , 7 , 4, 6
Blueberry 6 , 4 , 0 , 3
Calculate Sale for each day and all 4 days.
"""
import numpy as np
A = np.array([3 , 4 , 2])
B = np.array([[13 , 9, 7, 15],
             [8 , 7 , 4, 6],
             [6 , 4 , 0 , 3]])

print(A)
print(B)
mul=A.dot(B)
print(mul)
print(sum(mul))
