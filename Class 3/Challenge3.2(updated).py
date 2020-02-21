import sys

word = []

def letter_count(word, char='a'):
    count = 0
    for letter in word:
        if letter == char:
            count += 1
    return count


word1 = sys.argv[1]
word2 = sys.argv[2]
word3 = sys.argv[3]

print(letter_count(word1))
print(letter_count(word2))
print(letter_count(word3))

