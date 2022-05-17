"""
Madison Howard
Homework 5
"""
import random
import math


B = int(input("Please enter a positive integer: "))

N = random.randint(1,B)

#added from the assignment
max_guesses_needed = 1+math.ceil(math.log(B,2))
print("I’ve chosen a random integer N in the interval [1,{}]".format(B))
print("You should not need more than {} guesses to determine it.".\
format(max_guesses_needed))

"""
Problem 2
Write code which will do the following repeatedly, until the user correctly guesses the number N:
• Prompt the user to enter a guess.
• If the guess is too large, print a message to that effect. If the guess is too small, print
a message to that effect. If the guess is correct, print a message to that effect.
"""

N_guess = -1
n=0

while N!=N_guess:
    n=n+1
    N_guess = int(input("Please guess a value for N: "))
    if N<N_guess:
        print("Your guess is too big... Try again!")
    elif N>N_guess:
        print("Your guess was too low... Try again!")

if n<max_guesses_needed:
    print("Wow! You're so smart! You guess good :) ")
elif max_guesses_needed==n:
    print("Great! You got it...and on your last guess.")
else:
    print("You guessed correctly...unfortunately you're an idiot for taking all those guesses")
