#Creating arguements

import sys

# Creating an empty list for arguements
word = []

# Simple code attempting to count the occurances of the letter 'a' in a word
def letter_count(word, char='a'):
    count = 0
    for letter in word:
        if letter == char:
            count += 1
    return count

# The three arguements (when you run the code only 1 agruments works at a time?)
word.append(sys.argv[0])
word.append(sys.argv[1])
word.append(sys.argv[2])

print(letter_count(word))
