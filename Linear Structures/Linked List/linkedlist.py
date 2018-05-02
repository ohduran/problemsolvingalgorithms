class Node:
    """A collection of nodes make up a linked list."""

    def __init__(self, data):
        """Define constructor."""
        self._data = data
        self.next = None

    def set_next(self, new_next):
        """
        By default, the node is the last one in the list.
        Change that using set_next.
        """
        self.next = new_next

    def get_data(self):
        """Return data stored in node."""
        return self._data

    def get_next(self):
        """Get the next Node."""
        return self.next
