"""
Madison Howard
MATH 3430
January 18, 2022

(1) To the following code, add three print statements to print the Python type of each variable in the form: “myvar* has type: *” (of course the asterisks should be something else).
"""
print("−−−−−−−−−−−−−−− Problem 1 −−−−−−−−−−−−−−−−")
myvar1 = 42
myvar2 = 42.0
myvar3 = "42"
myvar1_type = type(myvar1)
myvar2_type = type(myvar2)
myvar3_type = type(myvar3)
print("myvar1 has type: ", myvar1_type)
print("myvar2 has type: ", myvar2_type)
print("myvar3 has type: ", myvar3_type)


"""
(2) Before the following code, insert a print statement displaying the problem number. Try to guess what the code will do before you run it. Then follow the code with another print statement explaining what it has done.

"""
print("----------------Problem 2--------------------")

x=5 #assigns the value of 5 to x
y = x*x+1 #assigns the "variable" y the value that is x times x then adds one (should be 26, the computer does the arithmetic here)
print("y = {0}".format(y)) # prints y = 26 (because y =26 because x*x+1= 5*5+1= 26)
print("The code from Problem 2 ultimately prints y = 26. First it assigns the value of 5 to x. Next, it tells the computer to calculate the value of y where y is equal to the product of the value assigned to x by itself and finally adds 1 to that value. (y=26 because x*x+1 = 5*5+1 = 26)")

"""
(3) Before the following code, insert a print statement displaying the problem number. Try to guess what the code will do before you run it. Then follow the code with another print statement explaining what it has done and why it gives the result it does.

"""
print("-----------------------Problem 3--------------------")
a=5 #assigns the value of 5 to a
b = a*a+1 #calculates the value of a*a+1 which is the above assigned value of 5, thus 5*5 = 25, and then adds 1 to that value, giving us 26. it then assigns that to the "variable" b
a=1 #reassigns the "variable" a to be 1
print("b = {0}".format(b)) #prints b = 26.
print("The code for problem 3 does as follows...")
print("First it assigns the value of 5 to a. Then calculates the value of a*a+1 which is the above assigned value of 5, thus 5*5 = 25, and then adds 1 to that value, giving us 26. It then assigns that to the variable b. Next it reassigns the variable a to be 1. Finally it takes the stored value for b (26) and prints b=26")
"""
(4) Before the following code, insert a print statement displaying the problem number. Try to guess what the code will do before you run it. Then follow the code with another print statement explaining what it has done (or why it has failed, if it fails).
"""
print("------------------------Problem 4------------------------------")
print("First the program will try to assign the value that is c*c+1 but since it doesn't know what c is it will then fail. It won't go past that point.")
d = c*c+1 #the code will try to assign the value that is c*c+1 but since it doesn't "know" what c is it will be angry and fail
c=5 #the program will not go past the above statement because it fails before then. If this were above the assignment for d it would work almost identically to Problem 2
print("d = {0}".format(c))
