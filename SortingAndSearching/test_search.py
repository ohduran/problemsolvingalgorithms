import unittest
from search import sequential_search, ordered_sequential_search, binary_search


class TestSearch(unittest.TestCase):
    """Test Search methods."""

    def test_sequential(self):
        """Test Sequential Search method."""
        test = [1, 2, 32, 8, 17, 19, 42, 13, 0]
        self.assertTrue(sequential_search(test, 13))
        self.assertFalse(sequential_search(test, 3))

    def test_ordered_sequential(self):
        """Test Ordered Sequential Search method."""
        test = sorted([1, 2, 32, 8, 17, 19, 42, 13, 0])
        self.assertTrue(ordered_sequential_search(test, 13))
        self.assertFalse(ordered_sequential_search(test, 3))

    def test_binary_search(self):
        """Test Binary Search method."""
        test = sorted([1, 2, 32, 8, 17, 19, 42, 13, 0])
        self.assertFalse(binary_search([], 1))
        self.assertTrue(binary_search(test, 13))
        self.assertFalse(binary_search(test, 3))


if __name__ == '__main__':
    unittest.main()
