"""
Calculate the minimal sales path cost in a tree of car distributors.

The sales path is a path from the factory (root node) to a dealership (leaf node). 
Each node represents a distributor or dealership, and each node holds a cost 
for shipping a car to it. The goal is to find the minimum cost of shipping 
a car from the root to a dealership.

Attributes:
    Node: Class to represent a node in the distribution tree.
    Solution: Class to calculate the minimal sales path cost.
"""

from typing import List

# Date of Last Practice: Oct 10, 2024
#
# Time Complexity: O(N), where N is the number of nodes in the tree.
#                  We visit each node once.
#
# Space Complexity: O(H), where H is the height of the tree.
#                   The space complexity is the height of the tree because we use
#                   recursion to traverse the tree. The maximum depth of the
#                   recursion is the height of the tree. In the worst case, the
#                   tree is skewed, and the height is equal to the number of nodes.


class Node:
    """Represents a distributor or dealership node in the sales path tree."""

    def __init__(self, cost: int):
        """Initializes a node with a given cost."""
        self.cost = cost
        self.children: List["Node"] = []


class Solution:
    """Finds the minimal sales path cost in the tree."""

    def get_cheapest_cost(self, rootNode: Node) -> int:
        """
        Find the minimum cost path from root node to any leaf node.

        Uses DFS to traverse the tree and calculate the cost.

        Args:
            rootNode: The root node of the tree (Honda's factory).

        Returns:
            The minimum cost from the root to any leaf node.
        """

        def dfs(node: Node) -> int:
            # If it's a leaf node, return its cost
            if not node.children:
                return node.cost

            # Find the minimum cost among all children
            min_cost = float("inf")
            for child in node.children:
                min_cost = min(min_cost, dfs(child))

            # Return the node cost plus the minimum cost of its children
            return node.cost + min_cost

        return dfs(rootNode)


# Test cases
def main():
    """Main function to run test cases."""

    # Test case 1: Empty tree, no cost
    root1 = Node(0)
    sol = Solution()
    assert (
        sol.get_cheapest_cost(root1) == 0
    ), f"Expected 0, but got {sol.get_cheapest_cost(root1)}"

    # Test case 2: Tree with minimal path cost 7
    root2 = Node(0)
    child21 = Node(5)
    child211 = Node(4)

    child22 = Node(3)
    child221 = Node(2)
    child2211 = Node(1)
    child22111 = Node(1)
    child222 = Node(0)
    child2221 = Node(10)

    child23 = Node(6)
    child231 = Node(1)
    child232 = Node(5)

    child21.children = [child211]
    child22.children = [child221, child222]
    child221.children = [child2211]
    child2211.children = [child22111]
    child222.children = [child2221]
    child23.children = [child231, child232]
    root2.children = [child21, child22, child23]
    assert (
        sol.get_cheapest_cost(root2) == 7
    ), f"Expected 7, but got {sol.get_cheapest_cost(root2)}"

    print("All test cases passed.")


if __name__ == "__main__":
    main()
