"""
MADISON HOWARD
Homework #7
2/22/22
In this assignment, you’ll write a program which will play the same game as in Assignment 5, except that the user will choose a number and the program will guess that number.
"""
#Part 1
import math
import random

B = 10**random.randint(1,5)
max_guesses_needed = 1+math.floor(math.log(B,2))
input( ("Choose a random integer in the interval [1, {}],"+
" and press RETURN when ready.").format(B))
print("I should be able to guess your number with no more"+
" than {} guesses.".format(max_guesses_needed))

#Part 2
num_guesses=1
guess=B//2
prev_guess=1
check = input("My guess is {}. Is this larger (L), smaller (S) or equal to (E) your integer? ".format(guess))
print("I have made {} guesses.".format(num_guesses))
lower = 1
upper = B

while check != "E":
    if lower-upper == 0:
        print("Your number is {}! Game over.".format(lower))
        check = 'E'
    else:
        if check == "S":
            lower = guess + 1
            guess = (upper+lower)//2
            num_guesses=num_guesses+1
            check = input("My guess is {}. Is this larger (L), smaller (S) or equal to (E) your integer? ".format(guess))
            print("I have made {} guesses.".format(num_guesses))
        elif check == "L":
            upper = guess - 1
            guess = (lower+upper)//2
            num_guesses=num_guesses+1
            check = input("My guess is {}. Is this larger (L), smaller (S) or equal to (E) your integer? ".format(guess))
            print("I have made {} guesses.".format(num_guesses))

print("Great! I guessed it in only {} guesses!".format(num_guesses))
