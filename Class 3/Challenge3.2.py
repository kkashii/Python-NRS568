import sys

word = []

def letter_count(word, char='a'):
    count = 0
    for letter in word:
        if letter == char:
            count += 1
    return count


word.append(sys.argv[0])
word.append(sys.argv[1])
word.append(sys.argv[2])

print(letter_count(word))