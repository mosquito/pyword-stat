from collections import Counter
from .reader import words_from_stdin


def main():
    counter = Counter()
    for word in words_from_stdin():
        counter[word.lower()] += 1

    for word, count in sorted(counter.items(), key=lambda x: x[1], reverse=True):
        print("%s: %d" % (word, count))
