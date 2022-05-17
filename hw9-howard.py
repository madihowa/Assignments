"""
Madison Howard
Assignment 9
"""
import random
import math
import time

#Problem 1
#Input an integer N greater than 1 from the user, with an appropriate prompt.

N = int(input("Please input an integer, N, greater than 1. "))


#Problem 2
#Create a list of the integers in the interval [0, N) by starting with an empty list and creating a loop that appends each integer to the list using the append method. Do NOT print anything.


time_app_0 = time.perf_counter()
int_list = []
for i in range(0, N):
    int_list.append(i)
time_app_1 = time.perf_counter()

#Problem 3
#Create a list of the integers in the interval [0,N) by starting with an empty list clist and creating a loop that appends each integer to the list using the list concatenation operator, like this (where n is your loop variable): clist = clist + [n]


time_con_0 = time.perf_counter()
clist = []
for n in range(0, N):
    clist= clist +[n]
time_con_1 = time.perf_counter()

#Problem 4
#At the top of your file, import the time module. This module contains a function time.perf counter() which will return the current value of a system clock with high resolution (typically at least microseconds). Use this function to determine the time used for each of those two methods for building the same list, and print those times (with a descriptive message, of course).

time_app = time_app_1 - time_app_0
time_con = time_con_1 - time_con_0
print("The time it took to append was {} seconds. ".format(time_app))
print("The time it took to concatenate was {} seconds. ".format(time_con))

#Problem 5
#Run your program several times in succession, using these values of N: 1000, 10000, 100000, 10000000. If done correctly, you should observe that one of the two techniques is asymptotically slower. Try to understand why that is the case, and add a print statement(s) explaining what you think is happening. I will explain in detail next week.
print("At higher values of N the concatenation method takes significantly longer.")
print("I think the reason for this is that the concatenation technique might have to reassign the list's content to where the computer is storing that information. For the append technique, I think it might just add the new element to the end of the already exsisting list.")
