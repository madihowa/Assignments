#Madison Howard
import math

print("**********Part 1************")
x = float(input("Enter a number: "))
n=0
sum=0

while n<=10:
    denom=math.factorial(2*n)
    term_n = ((-1)**n)*((x**(2*n))/(denom))
    sum = sum + term_n
    print(sum)
    n=n+1
print("Library Calculation")
print(math.cos(x))
