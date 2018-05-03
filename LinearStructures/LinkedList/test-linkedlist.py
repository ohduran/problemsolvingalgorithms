import unittest
from linkedlist import Node, UnorderedList, OrderedList


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


class TestUnorderedList(unittest.TestCase):
    """Test UnorderedList class."""

    def test_initially_points_to_empty(self):
        """An immediately instantiated UL must point to None."""
        ul = UnorderedList()

        self.assertIsNone(ul.head)

    def test_is_empty(self):
        """Test is_empty method."""
        ul = UnorderedList()
        self.assertTrue(ul.is_empty())
        ul.head = Node(1)
        self.assertFalse(ul.is_empty())

    def test_add(self):
        """Test add method."""
        ul = UnorderedList()
        ul.add(1)
        self.assertFalse(ul.is_empty())
        self.assertTrue(isinstance(ul.head, Node))
        self.assertEqual(ul.head.get_data(), 1)

    def test_size(self):
        """Test size method."""
        ul = UnorderedList()
        ul.add(3)
        ul.add(2)
        ul.add(1)
        self.assertEqual(ul.size(), 3)

    def test_search(self):
        """Test search method."""
        ul = UnorderedList()
        ul.add(3)
        ul.add(2)
        ul.add(1)

        self.assertTrue(ul.search(3))
        self.assertTrue(ul.search(2))
        self.assertTrue(ul.search(1))
        self.assertFalse(ul.search(0))

    def test_remove(self):
        """Test remove method."""
        ul = UnorderedList()
        ul.add(3)
        ul.add(2)
        ul.add(1)

        self.assertTrue(ul.search(2))

        ul.remove(2)

        self.assertFalse(ul.search(2))


class TestOrderedList(unittest.TestCase):
    """Test Ordered List class."""

    def test_search(self):
        """Test search method."""
        ol = OrderedList()
        ol.head = Node(1)

        self.assertTrue(ol.search(1))
        self.assertFalse(ol.search(2))

    def test_add(self):
        """Test add method."""
        ol = OrderedList()
        self.assertTrue(ol.is_empty())

        ol.add(1)
        self.assertFalse(ol.is_empty())
        self.assertTrue(ol.search(1))



if __name__ == '__main__':
    unittest.main()
