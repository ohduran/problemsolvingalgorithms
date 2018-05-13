# Searching
The algorithmic process of finding a particular item in a collection of items.
## Sequential Search
Go one by one: if it's there, then yes, else false.
## Binary Search
Divide and conquer! O(log n)
## Hashing
Build a data structure that can be searched in O(1) time, called hashing.
A hash table is a collection of items stored so that each position (slot), can hold an item and is named by an integer value starting at 0.
The mapping between an item and the slot where that item belongs is called hash function. It will take any item in the collection and return an integer in the range of slot names, between 0 and m-1, for m being the size of the hash table.
Once the hash values have been computed, we can insert each item into the hash table at the designated position - hash value.
How many values have been occupied against the total size is called load factor.
hash function == h(item) = item % size (in the case below, 11)
item      Hash value
54          10
26          4
93          5
17          6
77          0
31          9

Now when we want to search for an item, we simply use the hash function to compute the slot name for the item and then check the hash table to see if it is present.
This search operation is O(1), since a constant amount of time is required to compute the hash value and then index the hash table at location.

BUT -- what if the hash function is not giving me a list of unique values?
Say we include 44 in the list above, with hash value 0 as well (44%11 = 0). This is a collision.
