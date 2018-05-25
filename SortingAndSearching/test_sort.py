import unittest
import sort


unsorted_list = [3, 4, 1, 7, 2, 5, 9, 8, 6]
sorted_list = range(10)


class TestSort(unittest.TestCase):
    """Test Sort algorithms."""

    def test_bubble_sort(self):
        """Test bubble_sort."""
        result = sort.bubble_sort(unsorted_list)

        self.assertEqual(result, sorted_list)
