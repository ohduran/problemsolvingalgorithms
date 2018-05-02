import unittest
from linkedlist import Node


class TestNode(unittest.TestCase):
    """Node class tests."""

    def test_get_data(self):
        """Test get_data method."""
        n = Node(93)
        self.assertEqual(n.get_data(), 93)

    def set_next(self):
        """Test set_next method."""
        n1 = Node(1)
        n2 = Node(2)

        # by default, next is None
        self.assertIsNone(n1.next)

        n1.set_next(n2)

        # data from next is data from node 2
        self.assertEqual(n1.get_next().get_data(), 2)

    def get_next(self):
        """Test get_next method."""
        n1 = Node(1)
        n2 = Node(2)

        # by default, next is None
        self.assertIsNone(n1.next)

        n1.set_next(n2)
        self.assertEqual(n1.get_next(), n2)


if __name__ == '__main__':
    unittest.main()
