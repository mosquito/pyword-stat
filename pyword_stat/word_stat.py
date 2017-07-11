import sys
from string import punctuation, whitespace


NOT_SYMBOLS = punctuation + whitespace


def strip_characters(word):
    return word.strip(NOT_SYMBOLS)


def words_from_stdin(chunk_size=1024, charset='utf-8'):
    """
    Generator which return one word per iteration from stdin

    :param charset: Character encoding
    :param chunk_size: Should be more than length of the word (in generic)
    """

    data = ''

    while True:
        data += sys.stdin.read(chunk_size).decode(charset)
        words = list(data.split())

        if not words:
            return

        if data[-1] in NOT_SYMBOLS:
            data = ''
        else:
            data = words.pop(-1)

        for word in map(strip_characters, words):
            yield word
