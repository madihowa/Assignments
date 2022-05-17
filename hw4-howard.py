"""
Madison Howard
-------------- Problem 1 --------------------
Use an input statement with a prompt, asking the user to enter a positive integer N. This integer N will be used for each of the remaining problems.
"""
print("*********** Problem 1 **************")

N = float(input("Enter a positive integer for N: "))

"""
---------- Problem 2 ------------------
Then use a while loop to print the value of 1/n^2, for all integers n in the interval [1,N].
"""
print("*********** Problem 2 **************")

n=1
while n <= N:
    x = 1/(n**2)
    n += 1
    print(x)

"""
---------- Problem 3 ------------------
Then use a while loop to calculate
sum from j=1 to N of 1/j^2
and print the result.
    (1) - In PDF
    (2) - If you already know the n-1 value you can easily find the n value by calculating the last term (nth) and adding it to the n-1 value.
    (3) - If we have N=3 then we start with j=1 and calculate that 1/1^2=1 and then with j=2 we calculate that 1/2^2=0.25. Add 1+0.25 giving us 1.25. With j=3 we calculate 1/3^2 = 1/9=.111111. Add that to 1.25 giving us 1.361111111.

Ignore this:    We will use a while loop going through integers up to a predetermined value for N (like we did in problem 1). We can then define a sort of counter variable, j, in which we add 1 to go to the next term in the sequence (i.e., j= 1,j= 2,j= 3,j= 4,...). We will need to calcualte the value for 1/j^2 for as many terms until j=N using the while loop. After every calculation we will add that value to the former term through another variable, n, that is initially set to 0 before the loop.
"""
print("*********** Problem 3 **************")

j=1
n=0
while j <= N:
    x = 1/(j**2)
    j += 1
    n= n+x
    #print("1/j^2 is {0} and the summation of the terms thus far is {1}".format(x,n))
print("The summation of the terms is {0}".format(n))


"""
---------- Problem 4 ------------------
Use a while loop to calculate and print n! (n factorial) for all integers n in the interval [1,N].

    (1) - In PDF
    (2) - If you already know (n − 1)! then you can just multiply whatever n is by the n-1 calculation.
    (3) - If we want to find 5! then we start with the lowest integer, 1, and multiply that by the next lowest until we get to 5: 1*2*3*4*5
"""
print("*********** Problem 4 **************")

n=1
c=1
while c < N+1:
    n=n*c
    c +=1
    print(n)


"""
---------- Problem 5 ------------------
Then use a while loop to calculate
sum from n=0 to N of 1/n!
and print the result.
"""
print("*********** Problem 5 **************")

n=1
c=1
result_sum = 1

while c <= N:
    n=n*c
    c += 1
    result = 1/n
    result_sum = result_sum + result
    #print(result)
print(result_sum)

#print(result)


