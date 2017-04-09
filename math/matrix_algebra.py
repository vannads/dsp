#-------------------
#matrix_algebra.py
#-------------------

import numpy as np
from numpy import linalg as LA

A = np.matrix([[1,2,3], [2,7,4]])
B = np.matrix([[1,-1], [0,1]])
C = np.matrix([[5,-1], [9,1], [6,0]])
D = np.matrix([[3, -2, -1], [1, 2,3]])
u = np.matrix([6,2,-3, 5])
v = np.matrix([3,5,-1,4])
w = np.matrix([[1], [8], [0], [5]])
alpha = 6

#1. MatriX Dimensions
print("1. MatriX Dimensions")
print("--------------------")
print("1.1:", A.shape)
print("1.2:", B.shape)
print("1.3:", C.shape)
print("1.4:", D.shape)
print("1.5:", u.shape)
print("1.6:", w.shape)
print("")

'''
***Results
1. MatriX Dimensions
--------------------
1.1: (2, 3)
1.2: (2, 2)
1.3: (3, 2)
1.4: (2, 3)
1.5: (1, 4)
1.6: (4, 1)

'''

#2. Vector Operations
print("2. Vector Operations")
print("--------------------")
print("2.1:", u+v)
print("2.2:", u-v)
print("2.3:", alpha*u)
print("2.4:", np.multiply(u,v))
print("2.5:", LA.norm(u))
print("")

'''
***Results
2. Vector Operations
--------------------
2.1: [[ 9  7 -4  9]]
2.2: [[ 3 -3 -2  1]]
2.3: [[ 36  12 -18  30]]
2.4: [[18 10  3 20]]
2.5: 8.60232526704

'''
#3. Matrix Operations
print("3. Matrix Operations")
print("--------------------")
print("3.1:", "Not defined.")
A32 = A - C.transpose()
print("3.2:", A32)
A33 = C.transpose()+3*D
print("3.3:", A33)
A34 = B*A
print("Q3.4:", A34)
print("Q3.5:", "Not defined.")

#Optional
print("")
print("Optional")
print("--------------------")
print("3.6:", "Not defined.")

A37 = C*B
print("3.7:", A37)

A38 = B**4
print("3.8:", A38)

A39 = A*A.transpose()
print("3.9:", A39)

A310 = D.transpose()*D
print("3.10:", A310)

'''
***Results
3. Matrix Operations
--------------------
3.1: Not defined.
3.2: [[-4 -7 -3]
 [ 3  6  4]]
3.3: [[14  3  3]
 [ 2  7  9]]
Q3.4: [[-1 -5 -1]
 [ 2  7  4]]
Q3.5: Not defined.

Optional
--------------------
3.6: Not defined.
3.7: [[ 5 -6]
 [ 9 -8]
 [ 6 -6]]
3.8: [[ 1 -4]
 [ 0  1]]
3.9: [[14 28]
 [28 69]]
3.10: [[10 -4  0]
 [-4  8  8]
 [ 0  8 10]]

'''