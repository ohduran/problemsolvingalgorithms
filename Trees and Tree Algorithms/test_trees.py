import unittest
import trees
import binaryheap


class TestTrees(unittest.TestCase):
    """Test Trees."""

    def test_binary_tree_root_methods(self):
        """Test the initial behaviour of the Binary Tree."""
        r = trees.BinaryTree('a')
        self.assertEqual(r.get_root_value(), 'a')

        r.set_root_value('hello')
        self.assertEqual(r.get_root_value(), 'hello')

    def test_binary_tree_left_methods(self):
        """Test left child functionality."""
        r = trees.BinaryTree('a')
        self.assertIsNone(r.get_left_child())

        r.insert_left('b')
        self.assertTrue(isinstance(r.get_left_child(), trees.BinaryTree))
        self.assertEqual(r.get_left_child().get_root_value(), 'b')

    def test_binary_tree_right_methods(self):
        """Test right child functionality."""
        r = trees.BinaryTree('a')
        self.assertIsNone(r.get_right_child())

        r.insert_right('c')
        self.assertTrue(isinstance(r.get_right_child(), trees.BinaryTree))
        self.assertEqual(r.get_right_child().get_root_value(), 'c')

    def test_minheap_isempty(self):
        """Test Binary Heap isempty() method"""
        bn = binaryheap.MinHeap()
        # minheap must be initialised empty
        self.assertTrue(bn.is_empty())

    def test_minheap_insert(self):
        bn = binaryheap.MinHeap()

        bn.insert(5)

    def test_minheap_size(self):
        pass


if __name__ == '__main__':
    unittest.main()
