# Madison Howard
# Assignment 20



def read_wordlist(filename):
    f = open(filename, 'r')
    wordlist = f.read().splitlines() 
    f.close()
    return [x.upper() for x in wordlist if (len(x)==5) and x.isalpha()]

# Problem 1

def get_frequencies(WL):
    dictionary = {'A':0, 'B':0, 'C':0, 'D':0, 'E':0, 'F':0, 'G':0, 'H':0, 'I':0, 'J':0, 'K':0, 'L':0, 'M':0, 'N':0, 'O':0, 'P':0, 'Q':0, 'R':0, 'S':0, 'T':0, 'U':0, 'V':0, 'W':0, 'X':0, 'Y':0, 'Z':0 }
    for word_i in WL:
        for letter_i in word_i:
            if letter_i in dictionary:
                dictionary[letter_i] += 1
            else:
                pass
    return(dictionary)

# Problem 2
read = read_wordlist('american-english')
g = get_frequencies(read)

#print(g)

# Problem 3
# Bob is wrong :) 
# The most common letters are E,S,A,R,O,I,L
# This is a generally good statistic but it would be better to look at all the words that are 5 letters long. Shorter and longer words in the dictionary tend to skew the results.
