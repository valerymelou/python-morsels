from collections import deque
import unittest

from deep_flatten import deep_flatten


class DeepFlattenTests(unittest.TestCase):

    """Tests for deep_flatten."""

    def assertIterableEqual(self, iterable1, iterable2):
        self.assertEqual(list(iterable1), list(iterable2))

    def test_deep_lists(self):
        inputs = [0, [1, [2, 3]], [4]]
        outputs = [0, 1, 2, 3, 4]
        self.assertIterableEqual(deep_flatten(inputs), outputs)

    def test_tuples(self):
        inputs = (0, (1, (2, 3)), [4])
        outputs = [0, 1, 2, 3, 4]
        self.assertIterableEqual(deep_flatten(inputs), outputs)

    def test_deep_empty_list_with_tuple(self):
        self.assertIterableEqual(deep_flatten([[()]]), [])

    # To test the Bonus part of this exercise, comment out the following line
    # @unittest.expectedFailure
    def test_other_iterables(self):
        self.assertIterableEqual(
            deep_flatten((n, (n**3, n**2)) for n in [2, 3]),
            [2, 8, 4, 3, 27, 9],
        )
        self.assertIterableEqual(deep_flatten([(1, 2), deque([3])]), [1, 2, 3])
        self.assertIterableEqual(
            deep_flatten(iter([n]) for n in [1, 2, 3]),
            [1, 2, 3]
        )

    # To test the Bonus part of this exercise, comment out the following line
    @unittest.expectedFailure
    def test_returns_iterator(self):
        self.assertEqual(next(deep_flatten([0, [1, [2, 3]]])), 0)
        squares = (n**2 for n in [1, 2, 3])
        self.assertEqual(next(deep_flatten(squares)), 1)
        self.assertEqual(next(squares), 4)
        self.assertEqual(next(deep_flatten(squares)), 9)

    # To test the Bonus part of this exercise, comment out the following line
    # @unittest.expectedFailure
    def test_flatten_with_strings(self):
        inputs = [
            ['cats', ['carl', 'cate']],
            ['dogs', ['darlene', 'doug']],
        ]
        outputs = ['cats', 'carl', 'cate', 'dogs', 'darlene', 'doug']
        self.assertEqual(list(deep_flatten(inputs)), outputs)


if __name__ == "__main__":
    unittest.main(verbosity=2)