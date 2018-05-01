import unittest
from queue import Queue
from hotpotato import hot_potato


class TestQueue(unittest.TestCase):
    """Test Queue class."""

    def test_enqueue(self):
        """Enqueue must add a new item at the end of the queue."""
        q = Queue()
        self.assertEqual(len(q._items), 0)
        q.enqueue('hello')
        self.assertEqual(q._items, ['hello'])

    def test_is_empty(self):
        """Test is_empty method."""
        q = Queue()
        self.assertTrue(q.is_empty())
        q._items.append('hello')
        self.assertFalse(q.is_empty())

    def test_dequeue(self):
        """
        dequeue must return the first item on the list.
        And remove it from the list.
        """
        q = Queue()
        q._items.append('hello')
        q._items.append('world')
        q._items.append('hello')
        q.dequeue()
        self.assertEqual(q._items, ['world', 'hello'])

    def test_size(self):
        """Size must return length of the queue."""
        q = Queue()
        q._items.append('hello')
        q._items.append('world')
        q._items.append('hello')
        q._items.append('world')
        self.assertEqual(q.size(), 4)


class TestHotPotato(unittest.TestCase):
        """Test Hot Potato."""

        def test_1(self):
                """Test 1."""
                self.assertEqual(
                        hot_potato(
                                ['Bill',
                                 'David',
                                 'Susan',
                                 'Jane',
                                 'Kent',
                                 'Brad'],
                                7),
                        'Susan'
                )


if __name__ == '__main__':
    unittest.main()
