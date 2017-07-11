import sys
from string import punctuation, whitespace


NOT_SYMBOLS = punctuation + whitespace


def strip_characters(word):
    return word.strip(NOT_SYMBOLS)


def words_from_stdin(chunk_size=1024):
    """
    Generator which return one word per iteration from stdin

    :param chunk_size: Should be more than length of the word (in generic)
    """

    data = ''

    while True:
        # read the chunk
        chunk = sys.stdin.read(chunk_size)

        # Checking if data is over
        if not chunk and not data:
            raise StopIteration
        else:
            data += chunk

        # Split words
        words = list(data.split())

        if not words:
            raise StopIteration

        # if string was splitted exactly by word should reset the data
        if data[-1] in NOT_SYMBOLS:
            data = ''
        elif len(words) > 2:
            data = words.pop(-1)
        else:
            data = ''

        for word in map(strip_characters, words):
            yield word
