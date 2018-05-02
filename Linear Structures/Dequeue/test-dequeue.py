from dequeue import Dequeue
from palindromechecker import palindrome_checker
import unittest


class TestDequeue(unittest.TestCase):
    """Dequeue class tests."""

    def test_add_front(self):
        """Test add front method."""
        d = Dequeue()
        self.assertTrue(d._items == [])

        d.add_front(1)
        d.add_front(2)

        self.assertEqual(d._items, [2, 1])

    def test_add_rear(self):
        """Test add rear method."""
        d = Dequeue()
        self.assertTrue(d._items == [])

        d.add_rear(1)
        d.add_rear(2)
        self.assertEqual(d._items, [1, 2])

    def test_remove_rear(self):
        """Test remove rear method."""
        d = Dequeue()
        d.add_rear(1)
        d.add_rear(2)
        d.add_rear(3)
        self.assertEqual(d._items, [1, 2, 3])

        rear = d.remove_rear()

        self.assertEqual(rear, 3)
        self.assertEqual(d._items, [1, 2])

    def test_remove_front(self):
        """Test remove front method."""
        d = Dequeue()
        d.add_rear(1)
        d.add_rear(2)
        d.add_rear(3)
        self.assertEqual(d._items, [1, 2, 3])

        front = d.remove_front()

        self.assertEqual(front, 1)
        self.assertEqual(d._items, [2, 3])

    def test_is_empty(self):
        """Test is empty method."""
        d = Dequeue()
        self.assertTrue(d.is_empty())
        d.add_front(1)
        self.assertFalse(d.is_empty())

    def test_size(self):
        """Test size method."""
        d = Dequeue()
        self.assertEqual(d.size(), 0)

        n = 10
        for number in range(1, n):
                d.add_rear(1)
                self.assertEqual(d.size(), number)


class TestPalindromeChecker(unittest.TestCase):
        """Palindrome Checker tests."""

        def test_1(self):
                """Test 1."""
                self.assertTrue(palindrome_checker('radar'))
                self.assertTrue(palindrome_checker('toot'))
                self.assertTrue(palindrome_checker('madam'))
                self.assertFalse(palindrome_checker('palindrome'))


if __name__ == '__main__':
    unittest.main()
