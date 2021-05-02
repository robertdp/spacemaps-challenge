from collections import namedtuple
from contextlib import contextmanager
from requests import get

Row = namedtuple('Row', ['id', 'value'])


def to_row(line):
    id, value = line.rsplit(b' ', 1)
    return Row(id.decode('ascii'), int(value))


@contextmanager
def create_stream(filename):
    # Streaming the request should allow for constant memory usage (mostly)
    with get(filename, stream=True, headers={'Accept-Encoding': 'gzip'}) as response:
        # Different content encodings can be used based on the requirements, and hooked into the stream as an extra
        # transformation step. Or handled by libraries, as is the case here.
        response.raw.decode_content = True
        yield MappedIterator(response.iter_lines(), to_row)


class MappedIterator:
    def __init__(self, iterator, fmap):
        self.iterator = iterator
        self.fmap = fmap

    def __iter__(self):
        for x in self.iterator:
            yield self.fmap(x)

    def __next__(self):
        return next(self.__iter__())
