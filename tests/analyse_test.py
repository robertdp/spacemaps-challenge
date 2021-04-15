import unittest
import src.spacemaps.analyse as analyse
import src.spacemaps.stream as stream


class TestAnalysis(unittest.TestCase):
    def test_input_under_limit(self):
        input = [
            stream.Row('a', 5),
            stream.Row('b', 2),
            stream.Row('c', 8)
        ]
        expected = [
            input[2],
            input[0],
            input[1]
        ]
        results = analyse.run_analysis(iter(input), 10)
        self.assertListEqual(sorted(results), sorted(expected))

    def test_correct_sorting(self):
        input = [
            stream.Row('a', 5),
            stream.Row('b', 2),
            stream.Row('c', 8)
        ]
        expected = [
            input[2],
            input[0]
        ]
        results = analyse.run_analysis(iter(input), 2)
        self.assertListEqual(sorted(results), sorted(expected))
