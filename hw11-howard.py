"""
Madison Howard
Homework 11
"""
import math


def sum_forward(N):
    sum_fwd = 0
    for n in range(1,N+1):
        calculation = 1/(n**3)
        sum_fwd = sum_fwd + calculation
    return(sum_fwd)


def sum_backward(N):
    sum_bwd = 0
    n=N
    while n != 0:
        calculation = 1/(n**3)
        sum_bwd = sum_bwd + calculation
        n=n-1
    return(sum_bwd)


M = int(input("Give a positive integer to be N: "))
print("The vale of sum forward is {}.".format(sum_forward(M)))
print("The vale of sum backward is {}.".format(sum_backward(M)))
print("I think that at high values for N, the reason sum_forward and sum_backward differ could be due to rounding.")
