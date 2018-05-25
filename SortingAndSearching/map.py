"""
Implementing the Map Abstract Data Type.

One of the most useful Python collections is the dictionary,
an associative data type where you can store key-data pairs.

The keys in a map are all unique so that there is a one-to-one relationship
between a key and a value. The key is used to look up the associated value,
an idea often referred to as map.
"""


class Map():
    """Map Abstract Data Type."""

    def __init__(self):
        """Instantiate the object."""
        pass

    def put(self, key, val):
        """
        Add a new key-value pair to the map.
        If the key is already in the map, override.
        """
        pass

    def get(self, key):
        """Get the value associated with the key."""
        pass

    def delete(self, key):
        """Delete the key-value pair."""
        pass

    def __len__(self):
        """Return the number of key-value pairs."""
        pass

    def __in__(self, key):
        """Return True for a statement of the form key in map."""
        pass
