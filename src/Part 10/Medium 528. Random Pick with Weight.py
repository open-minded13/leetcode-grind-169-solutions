"""Randomly pick an index based on weighted probabilities.

This module defines a class to initialize an array of weights and allows for
random index selection with probability proportional to the weight of each index.

Typical usage example:
    solution = Solution([1, 3, 4])
    index = solution.pickIndex()
"""

from typing import List
from bisect import bisect_left
from random import randrange

# Date of Last Practice: Mar 7, 2024 -> Oct 27, 2024
#
# Time Complexity: O(N), where N is the length of the input list. We iterate through
#                  the list once to create the prefix sum array. The binary search in
#                  the prefix sum array is O(log N).
#
# Space Complexity: O(N), where N is the length of the input list. The prefix sum array
#                   effectively divides the range from 1 to the total sum of the weights
#                   into several segments, where the length of each segment is
#                   proportional to the weight of the corresponding index.


class Solution:
    """Initializes weight array and allows weighted random index selection.

    Attributes:
        prefix_sums (List[int]): Cumulative weight sums for efficient range selection.
        total_sum (int): Total of all weights in the array.
    """

    def __init__(self, w: List[int]):
        """Initializes Solution with a list of weights.

        Creates a prefix sum array from weights, allowing binary search for
        random weighted index selection.

        Args:
            w: List of positive integer weights.
        """
        self.prefix_sums = []
        cumulative_sum = 0
        for weight in w:
            cumulative_sum += weight
            self.prefix_sums.append(cumulative_sum)
        self.total_sum = cumulative_sum

    def pickIndex(self) -> int:
        """Selects a random index based on weight distribution.

        A random integer is generated in the range [1, total_sum], and the index
        corresponding to this cumulative range is returned using binary search.

        Returns:
            int: An index selected based on the weight distribution.
        """
        random_num = randrange(1, self.total_sum + 1)
        return self._binary_search(random_num)

    def _binary_search(self, target: int) -> int:
        """Binary search to find the smallest index with a cumulative sum >= target.

        Args:
            target: Randomly generated integer within cumulative weight range.

        Returns:
            int: The index where the target fits within the cumulative sums.
        """
        left, right = 0, len(self.prefix_sums) - 1
        while left < right:
            mid = (left + right) // 2
            if self.prefix_sums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left

    def _bisect_search(self, target: int) -> int:
        """Uses Python's bisect_left to achieve the same result as `_binary_search`.

        Uses Python's bisect_left to find the smallest index with a cumulative
        sum >= target.

        Args:
            target: Randomly generated integer within cumulative weight range.

        Returns:
            int: The index where the target fits within the cumulative sums.
        """
        return bisect_left(self.prefix_sums, target)


# Test cases with assertions
def main():
    """Tests the Solution class to ensure correct weighted index selection."""
    # Test case with single weight
    solution_single = Solution([1])
    assert solution_single.pickIndex() == 0, "Failed on single weight test"

    # Test case with multiple weights
    solution_multiple = Solution([1, 3, 4])
    index_counts = {0: 0, 1: 0, 2: 0}
    for _ in range(1000):
        index = solution_multiple.pickIndex()
        index_counts[index] += 1

    # Probability distribution roughly matches weights [1, 3, 4]
    assert index_counts[0] > 0, "Index 0 should be picked occasionally"
    assert (
        index_counts[1] > index_counts[0]
    ), "Index 1 should be picked more frequently than index 0"
    assert index_counts[2] > index_counts[1], "Index 2 should be picked most frequently"

    # Testing consistency between binary search methods
    random_num = randrange(1, solution_multiple.total_sum + 1)
    assert solution_multiple._binary_search(
        random_num
    ) == solution_multiple._bisect_search(
        random_num
    ), "Custom binary search and bisect_left do not match"

    print("All test cases passed!")


if __name__ == "__main__":
    main()
