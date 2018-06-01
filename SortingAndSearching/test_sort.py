import unittest
import sort


unsorted_list = [3, 4, 1, 7, 2, 5, 9, 8, 6]
sorted_list = range(1, 10)


def verify_sort(self, sort_function):
    """Verification test for a sort function."""
    result = sort_function(unsorted_list)
    self.assertEqual(result, sorted_list)


class TestSort(unittest.TestCase):
    """Test Sort algorithms."""

    def test_all_sorts(self):
        """Iterate over all functions and assert that everything works."""
        list_of_functions = [
            sort.bubble_sort,
            sort.selection_sort,
        ]

        for sort_function in list_of_functions:
            verify_sort(self, sort_function)


if __name__ == '__main__':
    unittest.main()
