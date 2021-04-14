from collections import namedtuple
from contextlib import contextmanager
from requests import get

Row = namedtuple('Row', ['id', 'value'])


def to_row(line):
    id, value = line.rsplit(b' ', 1)
    return Row(id.decode('ascii'), int(value))


@contextmanager
def create_stream(filename):
    with get(filename, stream=True, headers={'Accept-Encoding': 'gzip'}) as req:
        req.raw.decode_content = True
        yield MappedIterator(req.iter_lines(), to_row)


class MappedIterator:
    def __init__(self, iterator, fmap):
        self.iterator = iterator
        self.fmap = fmap

    def __iter__(self):
        for x in self.iterator:
            yield self.fmap(x)

    def __next__(self):
        return next(self.__iter__())

