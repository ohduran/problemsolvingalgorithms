"""Queue Data Structure - FIFO."""


class Queue():
    """Queue data structure - FIFO."""

    def __init__(self):
        """Define queue - FIFO."""
        self._items = []

    def is_empty(self):
        """Return True if the queue is empty."""
        return len(self._items) == 0

    def enqueue(self, item):
        """Add a new item to the end of the queue."""
        self._items.append(item)

    def dequeue(self):
        """Remove the first item of the queue and return it."""
        first = self._items[0]
        self._items.remove(first)
        return first

    def size(self):
        """Return the size of the queue."""
        return len(self._items)
