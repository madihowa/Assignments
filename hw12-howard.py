"""
Madison Howard
Assignment 12
March 22, 2022
"""

class SampleData:

    def __init__(self, L):
        # Store list of floats and  in attributes of this object.
        self.List = L

    def mean(self):
        # Using the object's attributes to determine the mean:
        summation = 0 #start a variable for the sum
        for element in self.List:
            summation = summation + element
        mean = summation/len(self.List)
        return mean

    def median(self):
    #help from https://www.geeksforgeeks.org/finding-mean-median-mode-in-python-without-libraries/
        n = len(self.List)
        self.List.sort()
        if n % 2 == 0: 
            median_1 = self.List[n//2] 
            median_2 = self.List[n//2 - 1] 
            median = (median_1 + median_2)/2
        else: 
            median = self.List[n//2]
        return median

    def std(self):
    #like from assignment 8...
        s_sum=0
        N= len(self.List)
        for i in self.List:
            s_sum = (i - self.mean())**2 + s_sum
            s = (s_sum/(N-1))**(1/2)
        return s


trialdata = [2, 3, 4, 5, 4532, 7, 1]
mydata = []
x=1
for k in range (20):
    x = (17*x + 31) % 503
    mydata.append(x**(1/2))
X = SampleData(mydata)
print("X has mean {}".format(X.mean()))
print("X has median {}".format(X.median()))
print("X has standard deviation {}".format(X.std()))
