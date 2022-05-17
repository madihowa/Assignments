"""
Madison Howard
March 31, 2022
Assignment 15
I worked with Maygen on the mult part
"""
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


    def __add__(self, g):
        #h = f+g, we wanna add 'em
        h = []
        orderOfMag = len(self.coef)
        m = len(g.coef)
        if m == orderOfMag:
            for i in range(m):
                add = self.coef[i] + g.coef[i]
                h.append(add)
        elif m < orderOfMag:
            n=0
            #diff = orderOfMag-m
            for i in range(m):
                if n < orderOfMag:
                    n+=1
                    add = self.coef[i]+g.coef[i]
                    h.append(add)
            for i in range(m,orderOfMag):
                h.append(self.coef[i])
        else:
            n=0
            for i in range(orderOfMag):
                if n < m:
                    n+=1
                    add = self.coef[i]+g.coef[i]
                    h.append(add)
            for i in range(orderOfMag,m):
                h.append(g.coef[i])
        return Polynomial(h)


    def __mul__(self, g):
        #h = f*g, we wanna multiply 'em
        #this only works for if self.coef and g.coef are the same length...
        orderOfMag = len(self.coef)
        m = len(g.coef)
        ab = (orderOfMag+m)-1
        j_list = [0]*ab
        n_list = [0]*ab
        for i in range(m):
            a = self.coef[i]
            k_list = [0]*i
            for i in range(orderOfMag):
                b = g.coef[i]
                h = a*b
                k_list.append(h)
            k_len = len(k_list)
            if k_len < ab:
                for l in range(ab-k_len):
                    k_list.append(0)
            for p in range(ab):
                n_list[p] = j_list[p]+k_list[p]
            j_list = n_list
        #print(n_list)
        q = len(n_list)
        mult_h = str(n_list[0])
        for i in range(1,q):
            if n_list[i] > 0:
                mult_h += " + {}x".format(n_list[i])
            else:
                mult_h += " - {}x".format(-n_list[i])
            if i>1:
                mult_h += "^{}".format(i)
        return mult_h


N = int(input("Please enter a non−negative integer N: "))
M = int(input("Please enter a non−negative integer M: "))
c = [(j+1)*(-1)**j for j in range(N+1)]
d = [(M+1-j)*(-1)**j for j in range(M+1)]
f = Polynomial(c)
g = Polynomial(d)
print("f is: {}".format(f))
print("g is: {}".format(g))
print("f+g is: {}".format(f+g))
print("f*g is: {}".format(f*g))
