__author__ = 'TorbenJ'

from itertools import permutations, count


def get_combinations(number=42, length=4):
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    alphadict = dict(zip(alphabet, count(1)))

    wordlist = permutations(alphabet, length)

    result = list()
    for permutation in wordlist:
        i = 0
        for letter in permutation:
            i += alphadict[letter]
        if i == number:
            result.append("".join(permutation))

    return result


if __name__ == "__main__":
    import pprint

    pprint.pprint(get_combinations())