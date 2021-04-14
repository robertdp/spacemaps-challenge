import unittest
import src.spacemaps.stream as stream

TEST_FILE = 'https://amp-spacemaps-technical-challenge.s3-ap-northeast-1.amazonaws.com/spacemaps_technical_challenge.txt'

class TestStream(unittest.TestCase):
    def test_to_row(self):
        a = stream.to_row(b'someid 44')
        self.assertEqual(a.id == 'someid', a.value == 44)

    def test_request_stream(self):
        with stream.create_stream(TEST_FILE) as stream_:
            self.assertTrue(all([True for _ in stream_]))

    def test_mapped_iterator(self):
        input = [1, 2, 3, 4]
        expected = ['1', '2', '3', '4']
        iterator = stream.MappedIterator(iter(input), str)
        self.assertListEqual([x for x in iterator], expected)
