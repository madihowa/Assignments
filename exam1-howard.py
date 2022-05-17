"""
Madison Howard
Exam 1

Simulate the result of playing game above with 100000 coin flips. Simulate each coin flip by using random.randint to pick a random integer coin which is either 0 or 1, each being equally likely.
If coin is 0, this should be interpreted as ’heads’. If coin is 1, this should be interpreted as tails.
After all 100000 coin flips, print out:
• The number of times the coin was ‘Heads’,
• The number of times the coin was ‘Tails’,
• Player 1’s ending balance.
"""
import math
import random

num_heads=0
num_tails=0
flips=0
player1=1 #starting bet
player2=0

while flips<100000:
    coin = random.randint(0,1)
    flips=flips+1
    if coin == 0:
        #print("heads")
        num_heads= num_heads + 1
        player1=player1+(player1*0.11)
    else:
        #print("tails")
        num_tails= num_tails + 1
        player1=player1-(player1*0.1)

print("Number of flips: {}".format(flips))
print("Number of heads: {}".format(num_heads))
print("Number of tails: {}".format(num_tails))
print("Player 1 now has ${}".format(player1))
