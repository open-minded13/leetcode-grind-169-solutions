"""
Find the smallest nonnegative integer missing from the array.

This module defines a class `Solution` with a method to find the smallest 
nonnegative integer that is NOT present in a given array of unique nonnegative 
integers. The method rearranges the array elements to place each integer in its 
corresponding index if possible, then scans to find the first missing integer.

Discussion: The difference between `arr[arr[i]], arr[i] = arr[i], arr[arr[i]]` 
and `arr[i], arr[arr[i]] = arr[arr[i]], arr[i]` is crucial. In Python, tuple 
assignment is evaluated from left to right, so the first form of assignment 
(`arr[arr[i]], arr[i] = arr[i], arr[arr[i]]`) swaps values correctly. The second 
form leads to incorrect behavior as it evaluates `arr[i]` before `arr[arr[i]]`, 
causing unintended overwriting of values. Careful attention is required when 
performing such assignments in-place.
"""

from typing import List

# Date of Last Practice: Oct 7, 2024
#
# Time Complexity: O(N), where N is the length of the input array.
#                  The algorithm performs two passes over the array, each taking
#                  O(N) time. The first pass rearranges the array elements. Although
#                  it contains a while loop, the total number of swaps is bounded by
#                  the length of the array. The second pass scans the array to find
#                  the first missing integer, which also takes O(N) time.
#
# Space Complexity: O(1), since the algorithm uses only a constant amount of
#                   extra space.


class Solution:
    """Find the smallest positive integer missing from the array."""

    def firstMissingPositive(self, nums: List[int]) -> int:
        """
        Rearranges elements in nums to find the smallest missing positive integer.

        Args:
            nums (List[int]): Array of unique nonnegative integers.

        Returns:
            int: The smallest positive integer not present in nums.
        """
        n = len(nums)

        # Step 1 - Rearrange the array by placing each integer in its corresponding
        #          index if it's in the range 1 to n.
        for i in range(n):
            # While the current number is within the valid range and not at its
            # correct position
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                correct_position = (
                    nums[i] - 1
                )  # The correct position for the current value
                # Swap the current value with the value at its correct position
                nums[correct_position], nums[i] = nums[i], nums[correct_position]

        # Step 2 - Scan the array to find the first index where index + 1 != value
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        # Step 3 - If all indices match, return the next available integer (n + 1)
        return n + 1


def main():
    """Test the firstMissingPositive function with various test cases."""
    solution = Solution()

    # Test cases
    assert solution.firstMissingPositive([0]) == 1
    assert solution.firstMissingPositive([0, 1, 2]) == 3
    assert solution.firstMissingPositive([1, 3, 0, 2]) == 4
    assert solution.firstMissingPositive([100000]) == 1
    assert solution.firstMissingPositive([1, 0, 3, 4, 5]) == 2
    assert solution.firstMissingPositive([0, 100000]) == 1
    assert solution.firstMissingPositive([0, 99999, 100000]) == 1
    assert solution.firstMissingPositive([0, 5, 4, 1, 3, 6, 2]) == 7

    print("All test cases passed!")


if __name__ == "__main__":
    main()
