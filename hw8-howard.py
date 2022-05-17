"""
Madison Howard
Homework 8
"""
import random
random.seed(1)

#Problem 1
#Input an integer N greater than 1 from the user, with an appropriate prompt. Create a list called rnums consisting of N random numbers in the interval [0,1) using the random function from the random module. Your final program should NOT print that list, because I will test it with a large value of N.

N = int(input("Please input an integer N, that is greater than 1: "))
rnums = []

for i in range(N):
    rnum = random.randint(0,1)
    rnums.append(rnum)
    #print(rnum) #temporary for checking purposes

#Problem 2
#Find and print the maximum and minimum values from the list rnums, clearly indicating which is which.

for i in rnums: #this only works for when both 1 and 0 have been generated in the list. Also, note that the value for rnum can only be 1 or 0.
    if i > 0:
        rnum_max = i
    else:
        rnum_min = i
print("The minimum value in rnums is {}".format(rnum_min))
print("The maximum value in rnums is {}".format(rnum_max))


#Problem 3
#Find and print, with a description (“the mean is: ”), the mean (average) of the numbers in the list rnums.
summation = 0

for j in rnums:
    summation = summation + j
    mean = summation/N

#print("The sum is {}".format(summation))
print("The mean is {}".format(mean))


#Problem 4
#Find and print, with a description, the sample standard deviation s of the numbers in the list rnums using the formula:
#s= sqrt(1/(N-1)(sum(rnums[j]-mean)^2))
#where mean is the mean computed in the previous problem. At the top of your file, immediately after importing the random module, add the line random.seed(1) to facilitate my testing of your code.
s_sum=0

for i in rnums:
    summation = summation + i
    s_mean = summation/N
    s_sum = (i-s_mean)**2 + s_sum

s = (1/(N-1)*(s_sum))**0.5

print("The standard deviation, s, is {}".format(s))
