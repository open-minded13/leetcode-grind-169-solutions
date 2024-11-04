"""Check if an integer array can be partitioned into two equal-sum subsets.

This module defines a solution for the "Partition Equal Subset Sum" problem,
using dynamic programming to determine if a subset with a specified sum
exists. If such a subset exists, then the remaining elements also sum
to the same value, indicating an equal partition is possible.

Typical usage example:

    solution = Solution()
    result = solution.canPartition([1, 5, 11, 5])  # True
"""

from typing import List

# Date of Last Practice: Jan 5, 2024 -> Feb 21, 2024 -> Nov 3, 2024
#
# Time Complexity: O(N*S), where N is the number of elements in the array.
#                  - We iterate over each element to calculate the sum of the array, O(N).
#                  - The core of the algorithm is the dynamic programming part.
#                    1) We iterate over each element in the array O(N), and for each element,
#                    2) we potentially iterate over a range up to the half_sum O(S/2).
#                  - Therefore, O(N) + O(N*S/2) = O(N*S).
#
# Space Complexity: O(S), where S is the sum of the array.
#                   The space complexity is primarily dictated by the size of the dynamic
#                   programming array, which is of size S/2 + 1.


class Solution:
    """Determine if an array can be partitioned into two equal-sum subsets."""

    def canPartition(self, nums: List[int]) -> bool:
        """Check if the array can be partitioned into two equal-sum subsets.

        This function uses dynamic programming to find if a subset sum of half
        the total sum exists. If found, such a subset implies the other subset
        also has the same sum, achieving equal partitioning.

        Args:
            nums: List of integers representing the array.

        Returns:
            True if the array can be partitioned into two equal-sum subsets,
            False otherwise.
        """
        # Step 1 - Calculate the total sum of the array.
        total_sum = sum(nums)

        # Step 2 - If the sum is odd, partitioning into equal subsets is impossible.
        if total_sum % 2 != 0:
            return False

        # Step 3 - Define the target subset sum as half of the total sum.
        target_sum = total_sum // 2

        # Step 4 - Initialize the DP array, where dp[i] represents whether a
        #          subset with sum i is achievable.
        dp = [False] * (target_sum + 1)
        dp[0] = True  # A sum of zero is always achievable with an empty subset.

        # Step 5 - Update the DP array for each number in nums.
        for num in nums:
            for i in range(target_sum, num - 1, -1):
                dp[i] = dp[i] or dp[i - num]

        # Step 6 - The value at dp[target_sum] indicates if an equal partition is
        #          possible.
        return dp[target_sum]


def main():
    """Execute test cases to validate the Solution class."""
    solution = Solution()

    # Test cases
    nums1 = [1, 5, 11, 5]
    nums2 = [1, 2, 3, 5]
    nums3 = [1, 1, 3, 4, 7]
    nums4 = [2, 3, 4, 6]

    assert solution.canPartition(nums1) is True, "Test case 1 failed"
    assert solution.canPartition(nums2) is False, "Test case 2 failed"
    assert solution.canPartition(nums3) is True, "Test case 3 failed"
    assert solution.canPartition(nums4) is False, "Test case 4 failed"

    print("All test cases passed!")


if __name__ == "__main__":
    main()
