"""Tree Data Structures."""


class BinaryTree():
    """A Binary Tree is a Tree with a maximum of two children per node."""

    def __init__(self, key):
        """Instantiate a Binary Tree."""
        self.key = key
        self.left_child = None
        self.right_child = None

    def get_left_child(self):
        """Return the binary tree corresponding to the left child of node."""
        return self.left_child

    def get_right_child(self):
        """Return the binary tree corresponding to the right child of node."""
        return self.right_child

    def set_root_value(self, value):
        """Store the object value in root."""
        self.key = value

    def get_root_value(self):
        """Return the object stored in node."""
        return self.key

    def insert_left(self, node):
        """
        Create a new Binary Tree and install as the left child of node.
        If a left child already exists,
        it will become the left child of the new node.
        """
        if self.left_child is None:
            self.left_child = BinaryTree(node)
        else:
            bt = BinaryTree(node)
            bt.left_child = self.left_child
            self.left_child = bt

    def insert_right(self, node):
        """
        Create a new Binary Tree and install as the right child of node.
        If a right child already exists,
        it will become the right child of the new node.
        """
        if self.right_child is None:
            self.right_child = BinaryTree(node)
        else:
            bt = BinaryTree(node)
            bt.right_child = self.right_child
            self.right_child = bt
