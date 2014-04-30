__author__ = 'LPC'

length = 4
number = 42

from itertools import permutations, count
alphabet = "abcdefghijklmnopqrstuvwxyz"

alphadict = dict(zip(alphabet, count(1)))

print(alphadict)
print("######")

wordlist = permutations(alphabet, length)

for permutation in wordlist:
    i = 0
    for letter in permutation:
        i += alphadict[letter]
    if i == number:
        print("".join(permutation))