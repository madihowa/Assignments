"""
Madison Howard
Homework 10
3/8/2022
"""
import math
#Part 1
#Write a Python function f(x) that computes and returns 2x + 1. The function should NOT print anything.

def f(x):
    y_f = 2*x + 1
    return y_f


#Part 2
#Write a Python function g(x) that computes and returns 1/3x^2 − 2/3x + 4. The function should NOT print anything.

def g(x):
    y_g = (1/3)*x**2 + (2/3)*x + 4
    return y_g

#Part 3
#Write a Python function gf_fg_equal(x) which compares (f ◦ g)(x) to (g ◦ f )(x) and returns True if they’re equal and False otherwise. The function should NOT print anything.
def gf_fg_equal(x):
    comp_g_of_f = g(f(x))
    comp_f_of_g = f(g(x))
    if comp_g_of_f == comp_f_of_g:
        return True
    else:
        return False



"""
Part 4
Write a Python function called silly_test() which takes no arguments. The function should do the following: for each integer n ∈ {0,1,2,...,10},
• Call the function gf_fg_equal to see whether (f ◦ g)(n) and (g ◦ f )(n) are equal.
• Print, on a single line, the value of n and a message indicating whether or not the two
compositions above are equal.
"""
def silly_test():
    for n in range(0, 11):
        if gf_fg_equal(n) is True:
            print("The value of n is {} and the two compositions are equal.".format(n))
        else:
            print("The value of n is {} and the two compositions are NOT equal.".format(n))
        n=n+1



#Part 5
#At the bottom of the file, call the function silly_test(). After running the program and observing the output, add a final print statement explaining whether or not f ◦ g = g ◦ f for these two functions, considered as mathematical functions from R to R.

silly_test()
print("From the program we can see that the compositions f(g) and g(f) are NOT equal.")
