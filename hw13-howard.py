"""
Madison Howard
Assignment 13
Problem 1:
Re-use your SampleData class from Assignment 12.
Find 3 interesting numerical datasets with 20-30 values.
For each dataset
    - Create a SampleData object,
    - Print a description of the data
    - Print the mean, median, and standard deviation of the data.
"""

#from assignment 12
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
        s_sum=0
        N= len(self.List)
        for i in self.List:
            s_sum = (i - self.mean())**2 + s_sum
            s = (s_sum/(N-1))**(1/2)
        return s


#list 1: 
print("List 1: ")
print("Participation of female researchers in Europe by percent.")
list1 = [52.3, 52.2, 51.6, 50, 49.1, 48.5, 47.7, 47.6, 47.2, 46.8, 45.6, 44.7, 44.3, 43.6, 43.5, 41.4, 40.2, 39.7, 39.6, 38.7, 38, 37.6, 37.3, 37, 36.4, 35.3, 35.2, 34.5, 34.1, 33.8, 33.7, 33.6, 32.5, 30.8, 29.5, 28.9, 28.7, 28, 27, 26.8, 25.8]
X1 = SampleData(list1)
print("List 1 has mean {}".format(X1.mean()))
print("List 1 has median {}".format(X1.median()))
print("List 1 has standard deviation {}".format(X1.std()))
print("\n")
print("\n")


#list 2: 
print("List 2: ")
print("Average movie ticket price in USD in the UK and USA from 2005-2017.")
list2 = [8.50, 8.96, 11.56, 10.49, 10.22, 9.35, 10.59, 10.83, 10.90, 11.26, 11.63, 10.39, 6.41, 6.55, 6.88, 7.18, 7.50, 7.89, 7.93, 7.96, 8.13, 8.13, 8.43, 8.97]
X2 = SampleData(list2)
print("List 2 has mean {}".format(X2.mean()))
print("List 2 has median {}".format(X2.median()))
print("List 2 has standard deviation {}".format(X2.std()))
print("\n")
print("\n")



#list 3: 
print("List 3: ")
print("GDP of about 30 countries in 2020 (alphabetically).")
list3 = [-1.9, -3.3, -5.5, -12, -4, -16, -9.9, -7.6, -0.3, -6.6, -4.3, -16.3, -5.8, 2.4, -17.6, -0.9, -6.3, -14, 3.8, -6.8,-7.8, -4.3, -7.9, -4.1, 1.2, -4.2, 2, 0.3, -3.1, 0.7, -5.4, -14.8, -5.8, 2.3, -6.1, -56.3, -6.8, -0.9, 4.9]
X3 = SampleData(list3)
print("List 3 has mean {}".format(X3.mean()))
print("List 3 has median {}".format(X3.median()))
print("List 3 has standard deviation {}".format(X3.std()))
print("\n")
print("\n")

#http://data.uis.unesco.org/ using#http://data.uis.unesco.org/ using#http://data.uis.unesco.org/ using

