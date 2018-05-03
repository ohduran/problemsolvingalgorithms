import unittest
from what_is_recursion import list_sum, factorial, to_str, is_palindrome


class TestWhatIsRecursion(unittest.TestCase):
    """Test What is Recursion functions."""

    def test_list_sum(self):
        """Test list_sum function."""
        self.assertEqual(list_sum([1, 2, 3]), 6)
        self.assertEqual(list_sum([1, 3, 5, 7, 9]), 25)

    def test_factorial(self):
        """Test factorial function."""
        self.assertEqual(factorial(4), 24)
        self.assertEqual(factorial(3), 6)

    def test_to_str(self):
        """Test to_str function."""
        self.assertEqual(to_str(1453, 10), '1453')
        self.assertEqual(to_str(1453, 16), '5AD')

    def test_is_palindrome(self):
        """Test is_palindrome function."""
        self.assertFalse(is_palindrome('palindrome'))
        self.assertTrue(is_palindrome('madam'))
        self.assertTrue(is_palindrome(
                'Reviled did I live, said I, as evil I did deliver'))
        self.assertTrue(is_palindrome(
                'Able was I ere I saw Elba'))


class TestStackFrames(unittest.TestCase):
        """Test stackframes module."""

        def test_to_str(self):
            """Test to_str function."""
            self.assertEqual(to_str(1453, 10), '1453')
            self.assertEqual(to_str(1453, 16), '5AD')


if __name__ == '__main__':
    unittest.main()
