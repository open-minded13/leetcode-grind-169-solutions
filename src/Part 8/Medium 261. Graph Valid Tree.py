"""
Determines if a given graph forms a valid tree.

The `Solution` class provides a method `validTree` that checks whether a graph 
represented by nodes and edges forms a valid tree. The function ensures the 
graph is acyclic and fully connected.
"""

from collections import defaultdict

# Date of Last Practice: Sep 10, 2024 -> Oct 29, 2024
#
# Time Complexity (Union-Find):
#                 O(E * α(V)), where E is the number of edges and V is the number
#                 of vertices. The Union-Find operations (Find and Union) are
#                 almost constant time due to path compression and union by rank.
#                 The α(V) is the inverse Ackermann function, which is a very slow
#                 growing function. In practice, α(V) is almost constant for typical
#                 values of V. Therefore, the time complexity is similar to O(E).
#
# Time Complexity (DFS):
#                 O(V + E), where V is the number of vertices and E is the number of
#                 edges. We visit each vertex once and for each vertex, we visit all
#                 its edges once.
#
#                 When to consider E into the time complexity?
#
#                 Graph A:
#
#                 0 - 1 - 2 - 3 - 4
#
#                 The O(V + E) time complexity is O(2V - 1) because the number of edges
#                 is V - 1, which can be simplified to O(V).
#
#                 Graph B:
#
#                   0
#                  / \
#                 1---2
#                 |   |
#                 3---4
#
#                 We should consider E in the time complexity because each vertex
#                 visits all its edges. In complete graphs, the number of edges is
#                 V * (V - 1) / 2.
#
# Space Complexity (Union-Find): O(V), due to storing the parent and rank arrays.
#
# Space Complexity (DFS): O(V + E), as the graph is represented using an adjacency list.


class UnionFind:
    """
    Union-Find data structure to manage connected components in a graph.
    """

    def __init__(self, size):
        # Initialize the parent of each node to be itself
        self.parent = list(range(size))
        # Rank is used to keep the tree flat
        self.rank = [1] * size

    def find(self, node):
        """
        Find the representative (root) of the node's set, with path compression.

        Args:
            node (int): The node to find the root for.

        Returns:
            int: The root of the node.
        """
        if self.parent[node] != node:
            # Path compression: make node point directly to the root
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, node1, node2):
        """
        Union the sets of two nodes.

        Args:
            node1 (int): The first node.
            node2 (int): The second node.

        Returns:
            bool: True if the union was successful (nodes were not in the same set),
                  False if a cycle was detected (nodes were already connected).
        """
        root1 = self.find(node1)
        root2 = self.find(node2)

        if root1 == root2:
            return False  # Cycle detected, since both nodes have the same root

        # Union by rank to keep tree flat
        if self.rank[root1] > self.rank[root2]:
            self.parent[root2] = root1
        elif self.rank[root1] < self.rank[root2]:
            self.parent[root1] = root2
        else:
            self.parent[root2] = root1
            self.rank[root1] += 1

        return True


class Solution:
    """
    Determines whether a graph represented by nodes and edges forms a valid tree.

    Union-Find is a way to group items together, where each item points to a leader
    that represents its group. If we try to connect two items already in the same group,
    it means there’s a loop or cycle, which shows that the graph isn’t a proper tree.
    """

    def validTree(self, n: int, edges: list[list[int]]) -> bool:
        """
        Checks if the given graph is a valid tree.

        Args:
            n (int): The number of nodes in the graph.
            edges (list[list[int]]): The edges of the graph.

        Returns:
            bool: True if the graph is a valid tree, otherwise False.
        """

        # Pick one of the following methods to check if the graph is a valid tree
        return self.unionFindValidTree(n, edges)
        # return self.validTreeDFS(n, edges)

    # Method 1: Union-Find (Disjoint Set), which is generally faster than DFS
    def unionFindValidTree(self, n: int, edges: list[list[int]]) -> bool:
        """
        Checks if the given graph is a valid tree using Union-Find.

        Args:
            n (int): The number of nodes in the graph.
            edges (list[list[int]]): The edges of the graph.

        Returns:
            bool: True if the graph is a valid tree, otherwise False.
        """
        if len(edges) != n - 1:
            return False  # A valid tree needs exactly n - 1 edges

        uf = UnionFind(n)
        for u, v in edges:
            if not uf.union(u, v):
                return False  # Cycle detected

        return True

    # Method 2: DFS
    def validTreeDFS(self, n: int, edges: list[list[int]]) -> bool:
        """
        Checks if the given graph is a valid tree using DFS.

        Args:
            n (int): The number of nodes in the graph.
            edges (list[list[int]]): The edges of the graph.

        Returns:
            bool: True if the graph is a valid tree, otherwise False.
        """
        # Handle the trivial case where there is only one node.
        if n == 1:
            return True

        # Handle cases where no edges are provided or an empty edge is given.
        if not edges or not edges[0]:
            return False

        # Initialize sets for tracking visited and safe nodes.
        is_visited = set()
        is_safe_node = set()

        # Build the graph using an adjacency list.
        graph = defaultdict(list)
        for node1, node2 in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)

        def has_cycle(prev, node):
            """
            Detects cycles using DFS.

            Args:
                prev (int or None): The previous node in the DFS traversal.
                node (int): The current node being visited.

            Returns:
                bool: True if a cycle is detected, otherwise False.
            """
            if node in is_safe_node:
                return False
            if node in is_visited:
                return True

            is_visited.add(node)
            for next_node in graph[node]:
                if next_node == prev:
                    continue
                if has_cycle(node, next_node):
                    return True

            is_visited.remove(node)
            is_safe_node.add(node)
            return False

        node = edges[0][0]
        if has_cycle(None, node):
            return False

        if len(is_safe_node) != n:
            return False

        return True


def main():
    """
    Runs test cases for the Solution class.
    """
    solution = Solution()

    # Test cases
    assert solution.validTree(5, [[0, 1], [0, 2], [0, 3], [1, 4]]), "Test case 1 failed"
    assert (
        solution.validTree(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]) is False
    ), "Test case 2 failed"
    assert solution.validTree(4, [[0, 1], [2, 3]]) is False, "Test case 3 failed"
    assert solution.validTree(2, []) is False, "Test case 4 failed"
    assert solution.validTree(1, []) is True, "Test case 5 failed"
    assert solution.validTree(3, [[1, 0]]) is False, "Test case 6 failed"

    print("All test cases passed!")


if __name__ == "__main__":
    main()
