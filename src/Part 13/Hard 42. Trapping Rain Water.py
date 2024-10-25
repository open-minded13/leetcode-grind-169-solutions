"""Calculate the amount of trapped rainwater between elevation heights.

This module defines a class for solving the Trapping Rain Water problem using a 
two-pointer approach. It efficiently calculates the trapped rainwater for a given 
elevation map represented as a list of integers.
"""

from typing import List

# Date of Last Practice: Jan 25, 2024 -> Feb 29, 2024 -> Oct 25, 2024
#
# Time Complexity: O(N), where N is the length of the height list.
#                  The two-pointer technique helps us iterate each element once.
#
# Space Complexity: O(1). We use constant space to store variables.


class Solution:
    """Computes the trapped rainwater using the two-pointer technique."""

    def trap(self, height: List[int]) -> int:
        """Calculates the total trapped rainwater.

        Args:
            height: List of non-negative integers representing elevation heights.

        Returns:
            The total amount of trapped rainwater.
        """
        # Step 1 - Initialize pointers and variables for tracking max heights.
        left, right = 0, len(height) - 1
        max_left_h, max_right_h = 0, 0
        trapped_water = 0

        # Step 2 - Process elevation heights using two-pointer approach.
        while left < right:
            left_h, right_h = height[left], height[right]
            # Update max heights seen so far from both directions.
            max_left_h = max(max_left_h, left_h)
            max_right_h = max(max_right_h, right_h)

            # Step 3 - Calculate trapped water at the smaller height and move the
            #          pointer.
            if left_h <= right_h:
                # Water trapped is determined by the difference between max_left_h
                # and left_h.
                trapped_water += max_left_h - left_h
                left += 1
            else:
                # Water trapped is determined by the difference between max_right_h
                # and right_h.
                trapped_water += max_right_h - right_h
                right -= 1

        # Step 4 - Return the accumulated trapped water.
        return trapped_water


def main():
    """Demonstrates the usage of the Solution class with test cases."""
    sol = Solution()

    # Step 5 - Define test cases with expected results.
    assert sol.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6
    assert sol.trap([4, 2, 0, 3, 2, 5]) == 9
    assert sol.trap([1, 3, 2, 4, 1, 3, 1, 4, 5]) == 8
    assert sol.trap([5, 1, 2, 3, 4, 1, 5]) == 14
    assert sol.trap([]) == 0
    assert sol.trap([0]) == 0
    assert sol.trap([1]) == 0
    assert sol.trap([2, 2, 2, 2, 2]) == 0
    assert sol.trap([3, 0, 3]) == 3
    assert sol.trap([1, 2, 3, 4, 5]) == 0
    assert sol.trap([5, 4, 3, 2, 1]) == 0
    assert sol.trap([2, 0, 2, 0, 2, 0, 2]) == 6

    print("All test cases passed!")


if __name__ == "__main__":
    main()
