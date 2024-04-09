import sys
from typing import List

# Date of Last Practice: Jan 14, 2024 -> Feb 23, 2024
#
# Time Complexity: O(N), where N is the number of nodes in the tree.
#                  Each node is removed once, and their edge reductions can be done in O(1).
# Space Complexity: O(N), where N is the number of nodes in the tree.
#                   The adj_list and leaves are dominant issues for storage.
#
# Centroid Decomposition: The concept of finding centroids in a tree is central to this problem.
#                         In a tree, a centroid is a node that, if removed,
#                         would split the tree into subtrees none of which
#                         is larger than half the size of the original tree.
#                         For the minimum height trees, the centroids will be the roots.
#                         NOTE: "A tree can have at most 2 centroids."
#
# Pruning the Tree: The algorithm starts by identifying all leaf nodes
#                   (nodes with only one neighbor).
#                   These leaves are then pruned from the tree, and the process is repeated.
#                   As leaves are pruned, the new leaf nodes are identified in the reduced tree.
#                   This process continues until only one or two nodes remain,
#                   which are the centroids of the tree.
#
# Adjacency List: This is used to represent the tree.
#                 Each node in the list maintains a set of its adjacent nodes (neighbors).
#                 NOTE: The use of a set for each node's neighbors makes it easy and fast to
#                 add or remove edges in O(1), which is crucial for this problem.
#                 Compared to list.remove(), it takes O(N) to remove the item.


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        if n == 2:
            return [0, 1]

        # Build the adjacency list.
        adj_list = [set() for _ in range(n)]
        for edge in edges:
            adj_list[edge[0]].add(edge[1])
            adj_list[edge[1]].add(edge[0])

        # Initialize the first layer of leaves.
        leaves = [i for i in range(n) if len(adj_list[i]) == 1]

        # Trim the leaves until reaching the centroids (at most 2 in a tree).
        remaining_nodes = n
        while remaining_nodes > 2:
            remaining_nodes -= len(leaves)

            new_leaves = []
            for leaf in leaves:
                neighbor = adj_list[leaf].pop()
                adj_list[neighbor].remove(leaf)
                if len(adj_list[neighbor]) == 1:
                    new_leaves.append(neighbor)

            leaves = new_leaves

        return leaves


class First_Solution:
    # For each node, we are running a DFS to find the maximum depth.
    # The DFS itself is O(N) in the worst case (since it might visit all nodes).
    # Since we are doing this for every node, it becomes O(N^2).
    # Therefore, this solution will encounter a 'Time Limit Exceeded' error.
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        adjcent_list = {i: [] for i in range(n)}
        for edge in edges:
            adjcent_list[edge[0]].append(edge[1])
            adjcent_list[edge[1]].append(edge[0])

        def dfs(root, node, level):
            depth = level
            for child in adjcent_list[node]:
                if child == root:
                    if len(adjcent_list[node]) == 1:
                        return level
                    continue
                depth = max(dfs(node, child, level + 1), depth)
            return depth

        result = []
        min_depth = sys.maxsize
        for root in range(n):
            depth = 1
            for node in adjcent_list[root]:
                depth = max(dfs(root, node, 1), depth)
            if depth <= min_depth:
                if depth == min_depth:
                    result.append(root)
                else:
                    result.clear()
                    result.append(root)
                    min_depth = depth

        return result


sol = Solution()

# Test case 1: Tree with only two nodes
assert sol.findMinHeightTrees(2, [[0, 1]]) == [0, 1] or sol.findMinHeightTrees(
    2, [[0, 1]]
) == [1, 0]

# Test case 2: Star-shaped tree (one central node with multiple leaves)
assert sol.findMinHeightTrees(5, [[0, 1], [0, 2], [0, 3], [0, 4]]) == [0]

# Test case 3: Linear tree (nodes in a straight line)
assert sol.findMinHeightTrees(5, [[0, 1], [1, 2], [2, 3], [3, 4]]) == [2]

# Test case 4: Large tree with multiple branches
assert sol.findMinHeightTrees(7, [[0, 1], [1, 2], [1, 3], [2, 4], [2, 5], [5, 6]]) == [
    2
]

# Test case 5: Single node tree
assert sol.findMinHeightTrees(1, []) == [0]

print("All test cases passed!")
