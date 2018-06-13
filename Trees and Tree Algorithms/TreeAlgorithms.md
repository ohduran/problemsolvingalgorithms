# Trees and Tree Algorithms
Trees are used in many areas of computer science, including operating systems, graphics, database systems, and networking.

A tree data structure has root, branches, and leaves. The root is considered to be at the top and its leaves at the bottom.

You can start at the top of the tree and follow a path. At each level, we might ask ourselves a question and then follow the path that agrees with our answer.

All of the children of one node are independent of the children of another node.

Each leaf node is unique; we can specify a path from the root of the tree to a leaf that uniquely identifies each leaf.

### Vocabulary

- Node: A node is a fundamental block of the tree. It can have a name, the 'key', and additional information called 'payload'.
- Edge: An edge connects two nodes to show that there is a relationship between them. Every node is connected by exactly one incoming edge, and may have several outgoing edges.
- Root: The only node with no incoming edges.
- Path: Ordered list of nodes that are connected by edges.
- Children: The set of nodes that have incoming edges from the same node.
- Parent: A node that connects with a set of nodes with outgoing edges.
- Subtree: A set of nodes and edges comprised of a parent and all the descendants of that parent.
- Leaf Node: A node that has no children.
- Level of Node n: The number of edges on the path from the root node to n.
- Height: Maximum level of any node in the tree.

### Definitions

1. A tree consists of a set of nodes and a set of edges that connect pairs of nodes. One node is designated as the root node; every node except root is connected by an edge from exactly one other node; a unique path traverses from root to each node.
2. A tree is either empty or consists of a root and zero or more subtrees, each of which is also a tree.

## Binary Heaps and Priority Queues

Earlier we have seen FIFO structures called queues, and in particular, the **priority queue**. In a priority queue,
the logical order of items inside a queue is determined by their priority. The highest priority items
are at the front of the queue and the lowest priority are at the back.

Thus, when you enqueue an item on a priority queue, the new item may move all the way to the front.

The classic way to implement a priority queue is using a binary heap, which will allow us both enqueue and dequeue items in *O(log n)*.

The binary heap diagram looks a lot like a tree, but when implemented, we use only a single list as an internal representation.
It has two common variations: the **min heap**, in which the smallest key is always at the front, and the **max heap**, in which the largest key
is always at the front.

### Binary Heap Implementation

#### The Structure Property
We are taking advantage of the logarithmic nature of the binary tree to represent our heap, but we must keep it balanced.
A **complete binary tree** is a tree in which each level has all of its nodes.

Another interesting property of a complete tree is that we can represent it using a single list. We do not need to use nodes
and references or even list of lists. Because the tree is complete, the left child of a parent (at position *p*) is the node found in the position *2p*.
To find the parent of any node in the tree, we can use Python's integer division. Given a node in position *n*, the parent is at position n/2.