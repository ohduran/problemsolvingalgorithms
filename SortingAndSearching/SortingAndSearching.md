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

One way to always have a perfect hash function with no collisions is to increase the size of the hash table so that each possible value in the item range can be accommodated. It is however not feasible when the number of possible items is large (1 billion slots for 9-digit SS numbers).

- Folding method:
Divides the item into equal-size pieces, and then they are added together to give the resulting hash value.
- Mid-square method:
Square the item, and then extract some portion of the resuting digits.

But this doesn't scale very well for inserting data into the hash table.

One method for resolving collisions looks into the hash table and tries to find another open slot to hold the item that caused the collision. A simple way to do this is to start at the original hash table and then move in a sequential manner through the slots until we encounter the first empty slot: this is open addressing, called linear probing.

Once we have a hashing table, it's crucial that we use the same method to search.  However, a disadvantage of linear probing is the tendency for clustering: if many collisions occur at the same hash table, a number of surrounding slots will be filled by the linear probing resolution. One way to deal with this is to extend the linear probing technique so that instead of looking sequentially for the next open slot, we skip slots, distributing the items more evenly. The general name for this is rehashing.

A variation of the linear probing idea is called quadrating probing. Instead of using a constant "skip" value, we use a rehash function that increments the hash value by 1,3,5,7,9, ..., using successive perfect squares.

An alternative method for handling the collision is to allow each slot to hold a reference to a collection of items. As more and more items hash to the same location, the difficulty to search for the item increases.

# Sorting

Sorting is the process of placing elements from a collection in some kind of order. We have already seen a number of algorithms that were able to benefit from having a sorted list.

For small collections, a complex sorting method may be more trouble than it is worth. For larger collections, we want to take advantage of as many improvements as possible.

In order to sort a collection, it will be necessary to have some systematic way to compare values to see if they are out of order. The total number of comparisons will be the most common way to measure a sort procedure; the exchange of positions is a costly operation and the total number of exchanges will also be important for evaluating the overall efficiency of the algorithm.

## Bubble Sort
The bubble sort makes multiple passes through a list. It compares adjacent items and exchanges those that are out of order.
