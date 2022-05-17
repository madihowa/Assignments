"""
Madison Howard
Assigment 16
April 6, 2022
Megan Cuevas was my partner on this assignment
"""

import numpy as np
import random

N = int(input("Please input a positive integer: "))

def matrix_func(N):
    mat = np.zeros(shape = (N,N))
    for i in range(N):
        for j in range(N):
            mat[i][j] = random.random()
    return mat

def AliceBob(N):
    deter_s= 0
    for i in range(100000):
        mat = matrix_func(N)
        A = mat@mat
        deter = np.linalg.det(A)
        deter_s = deter_s + deter
    avg_deter = deter_s/100000
    print("The average determinant of A^2 for 100000 randomly chosen N×N matrices A is {}".format(avg_deter))
    return avg_deter

AliceBob(N)

print("Bob is not right. This should return a value close to zero but still not zero.")




