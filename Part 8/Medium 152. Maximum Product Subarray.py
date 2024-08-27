"""
A module to find the subarray with the largest product in an integer array.

This module defines a class `Solution` that provides two methods `maxProduct`
to find the subarray with the largest product in an integer array. The first
method demonstrates a good two-pass approach, while the second method offers
an optimized single-pass solution. Test cases are included to validate the
correctness of both implementations.
"""

import sys
from typing import List

# Date of Last Practice: Aug 26, 2024
#
# Time Complexity: O(N), where N is the number of elements in the given list.
#                  The time complexity is due to the single pass through the list.
#
# Space Complexity: O(1), as the algorithm uses a constant amount of extra space.
#                   The space complexity is independent of the input size.


class Solution:
    """
    Find the subarray with the largest product in an integer array.
    """

    def maxProduct_two_pass(self, nums: List[int]) -> int:
        """
        Find the subarray with the largest product using a two-pass approach.

        This function iterates through the array twice (left-to-right and
        right-to-left) while tracking the maximum product at each step. The
        current product is reset to 1 whenever a zero is encountered.

        Args:
            nums (List[int]): A list of integers representing the array.

        Returns:
            int: The largest product of any contiguous subarray.
        """
        current_value = 1
        max_value = -sys.maxsize - 1

        # First pass: left-to-right
        for num in nums:
            current_value *= num
            max_value = max(current_value, max_value)
            if current_value == 0:
                current_value = 1

        current_value = 1

        # Second pass: right-to-left
        for num in nums[::-1]:
            current_value *= num
            max_value = max(current_value, max_value)
            if current_value == 0:
                current_value = 1

        return max_value

    def maxProduct(self, nums: List[int]) -> int:
        """
        Find the subarray with the largest product using an optimized approach.

        This function iterates through the array once, tracking both the maximum
        and minimum products at each step to account for the effect of negative
        numbers. This avoids the need for a second pass.

        Args:
            nums (List[int]): A list of integers representing the array.

        Returns:
            int: The largest product of any contiguous subarray.
        """
        max_value = nums[0]
        current_max = nums[0]
        current_min = nums[0]

        for num in nums[1:]:
            candidates = (num, current_max * num, current_min * num)
            current_max = max(candidates)
            current_min = min(candidates)
            max_value = max(max_value, current_max)

        return max_value


def main():
    """
    Main function to run test cases for the maxProduct functions.

    This function runs several assert statements to ensure the correctness of
    both the maxProduct_two_pass and maxProduct functions.
    """
    # Create an instance of the Solution class
    solution = Solution()

    # Test case 1: Basic case with positive and negative numbers
    assert solution.maxProduct_two_pass([2, 3, -2, 4]) == 6
    assert solution.maxProduct([2, 3, -2, 4]) == 6

    # Test case 2: Contains zero, where product becomes zero
    assert solution.maxProduct_two_pass([-2, 0, -1]) == 0
    assert solution.maxProduct([-2, 0, -1]) == 0

    # Test case 3: All negative numbers
    assert solution.maxProduct_two_pass([-2, -3, -4]) == 12
    assert solution.maxProduct([-2, -3, -4]) == 12

    # Test case 4: Single positive number
    assert solution.maxProduct_two_pass([3]) == 3
    assert solution.maxProduct([3]) == 3

    # Test case 5: Single negative number
    assert solution.maxProduct_two_pass([-3]) == -3
    assert solution.maxProduct([-3]) == -3

    # Test case 6: Large array with mixed values
    assert solution.maxProduct_two_pass([2, 3, -2, 4, -1, 2, -5, 6, 0, 3, -1, 2]) == 240
    assert solution.maxProduct([2, 3, -2, 4, -1, 2, -5, 6, 0, 3, -1, 2]) == 240

    print("All test cases passed!")


if __name__ == "__main__":
    main()
