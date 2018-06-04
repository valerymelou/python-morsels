import unittest


from loop_helper import loop_helper


class LoopHelperTests(unittest.TestCase):

    """Tests for loop_helper."""

    def assertIterableEqual(self, iterable1, iterable2):
        self.assertEqual(list(iterable1), list(iterable2))

    def test_empty_lists(self):
        self.assertIterableEqual(loop_helper([]), [])

    def test_empty_iterator(self):
        self.assertIterableEqual(loop_helper(n**2 for n in range(0)), [])

    def test_single_item(self):
        item, info = next(iter(loop_helper(['a'])))
        self.assertEqual(item, 'a')
        self.assertEqual(info.index, 0)
        self.assertTrue(info.is_first)

    def test_three_items(self):
        response = iter(loop_helper(['a', 'b', 'c']))

        item, info = next(response)
        self.assertEqual(item, 'a')
        self.assertEqual(info.index, 0)
        self.assertTrue(info.is_first)

        item, info = next(response)
        self.assertEqual(item, 'b')
        self.assertEqual(info.index, 1)
        self.assertFalse(info.is_first)

        item, info = next(response)
        self.assertEqual(item, 'c')
        self.assertEqual(info.index, 2)
        self.assertFalse(info.is_first)

    # To test the Bonus part of this exercise, comment out the following line
    # @unittest.expectedFailure
    def test_returns_iterator(self):
        response = loop_helper(n**2 for n in range(0))
        self.assertEqual(iter(response), response)

    # To test the Bonus part of this exercise, comment out the following line
    # @unittest.expectedFailure
    def test_current_and_previous_attributes(self):
        response = loop_helper(['a', 'b', 'c'])

        item, info = next(response)
        self.assertEqual(item, 'a')
        self.assertEqual(info.current, 'a')
        self.assertEqual(info.previous, None)

        item, info = next(response)
        self.assertEqual(item, 'b')
        self.assertEqual(info.current, 'b')
        self.assertEqual(info.previous, 'a')

        item, info = next(response)
        self.assertEqual(item, 'c')
        self.assertEqual(info.current, 'c')
        self.assertEqual(info.previous, 'b')

        response = loop_helper(['a', 'b', 'c'], previous_default='')

        item, info = next(response)
        self.assertEqual(item, 'a')
        self.assertEqual(info.current, 'a')
        self.assertEqual(info.previous, '')

        item, info = next(response)
        self.assertEqual(item, 'b')
        self.assertEqual(info.current, 'b')
        self.assertEqual(info.previous, 'a')

        item, info = next(response)
        self.assertEqual(item, 'c')
        self.assertEqual(info.current, 'c')
        self.assertEqual(info.previous, 'b')

    # To test the Bonus part of this exercise, comment out the following line
    # @unittest.expectedFailure
    def test_next_and_is_last(self):
        response = loop_helper(['a', 'b', None, None])

        item, info = next(response)
        self.assertEqual(item, 'a')
        self.assertEqual(info.next, 'b')
        self.assertFalse(info.is_last)

        item, info = next(response)
        self.assertEqual(item, 'b')
        self.assertEqual(info.next, None)
        self.assertFalse(info.is_last)

        item, info = next(response)
        self.assertEqual(item, None)
        self.assertEqual(info.next, None)
        self.assertFalse(info.is_last)

        item, info = next(response)
        self.assertEqual(item, None)
        self.assertEqual(info.next, None)
        self.assertTrue(info.is_last)


if __name__ == "__main__":
    unittest.main(verbosity=2)