# Trees and Tree Algorithms
Trees are used in many areas of computer science, including operating systems, graphics, database systems, and networking.

A tree data structure has root, branches, and leaves. The root is considered to be at the top and its leaves at the bottom.

You can start at the top of the tree and follow a path. At each level, we might ask ourselves a question and then follow the path that agrees with our answer.

All of the children of one node are independent of the children of another node.

Each leaf node is unique; we can specify a path from the root of the tree to a leaf that uniquely identifies each leaf.

## Vocabulary

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

## Definitions

1. A tree consists of a set of nodes and a set of edges that connect pairs of nodes. One node is designated as the root node; every node except root is connected by an edge from exactly one other node; a unique path traverses from root to each node.
2. A tree is either empty or consists of a root and zero or more subtrees, each of which is also a tree.
