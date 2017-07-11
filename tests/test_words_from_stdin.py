import io
import sys
from contextlib import contextmanager
from pyword_stat.reader import words_from_stdin


@contextmanager
def patch_stdin(io_obj):
    stdin = sys.stdin
    sys.stdin = io_obj

    try:
        yield
    finally:
        sys.stdin = stdin


def test_simple():
    with patch_stdin(io.StringIO('foo bar baz')):
        assert tuple(words_from_stdin()) == ('foo', 'bar', 'baz')


def test_simple_long():
    with patch_stdin(io.StringIO('foo bar baz ' * 1000)):
        assert tuple(words_from_stdin()) == ('foo', 'bar', 'baz') * 1000

