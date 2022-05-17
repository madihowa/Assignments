"""
Madison Howard
March 29, 2022
Assignment 14
I got some help from Maygen Daniel
"""
#Problem 1
import copy

class Polynomial:

    def __init__(self, coef_list):
        self.coef = copy.deepcopy(coef_list)

    def __str__(self):
        #This method returns a representation of this object as a string
        orderOfMag = len(self.coef)
        res = ""
        mystr = str(self.coef[0])
        for i in range(1, orderOfMag):
            if self.coef[i] >= 0:
                mystr = mystr + " + {}x".format(self.coef[i])
            else:
                mystr = mystr + " - {}x".format(-self.coef[i])
            if i > 1:
                mystr += "^{}".format(i)
        return mystr

    def __call__(self, a):
        out = 0
        orderOfMag = len(self.coef)
        for i in range(orderOfMag):
            out += (self.coef[i])*a**i
        return out

N = int(input("Please enter a non−negative integer N: "))
c = [(j+1)*(-1)**j for j in range(N+1)]
f = Polynomial(c)
print("f is: {}".format(f))
t = float(input("Please enter a floating point number t: "))
print("f({}) = {}".format(t, f(t)))
