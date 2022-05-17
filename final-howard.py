"""
Madison Howard
Final Exam
"""

import random

#Part 1
#takes two lists of three numbers x and y, each representing a point in R3, and returns the distance between those points.
def distance(x,y):
    dist = ((x[0]-y[0])**2 + (x[1]-y[1])**2 + (x[2]-y[2])**2 )**0.5
    return dist

#print(distance(x,y))
#Part 2
#returns a list of three numbers chosen at random from the interval [0, 1)

def random_pt():
    point = []
    count = 0
    while count != 3:
        point.append(random.random())
        count +=1
    return point


#Part 3
#Choose two random points, using the function random pt.
#performs the following experiment N times
#Find the distance between those points, using the function distance
def do_experiment(N):
    count=0
    total = 0
    while count<N:
        x = random_pt()
        y = random_pt()
        total = distance(x, y)
        count+=1
    experiment_avg = total/N
    return experiment_avg

#Part 4
#Use the function do experiment to perform the experiment 103, 104, 105, and 106 times. Is Bob right?
#Bob is not right. As the number of times the experiment is run (N increases) the average value decreases towards zero.
#testing it
"""
for i in range(3, 7):
    N = 10**i #number of times the experiment is run
    print("Magnitude of {}".format(i))
    print(do_experiment(N))
"""
