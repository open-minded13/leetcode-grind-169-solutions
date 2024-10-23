"""Finds the area of the largest rectangle in a histogram.

This module contains a class `Solution` with a method to determine the area
of the largest rectangle that can be formed within a histogram.
"""

from typing import List

# Date of Last Practice: Jan 30, 2024 -> Mar 3, 2024 -> Oct 23, 2024
#
# Time Complexity: O(N), where N is the number of bars in the histogram.
#                  This efficiency is achieved because each bar is pushed onto the
#                  stack once and popped once.
#
# Space Complexity: O(N), where N is the number of bars in the histogram.
#                   We use an additional stack to store indices of the bars.


class Solution:
    """Solves the largest rectangle area problem for a given histogram."""

    def largestRectangleArea(self, heights: List[int]) -> int:
        """Finds the maximum area of a rectangle in a histogram.

        Uses a stack-based approach to calculate the maximum rectangular area
        possible in the histogram represented by the input list of heights.

        Args:
            heights: A list of integers representing bar heights in the histogram.

        Returns:
            The maximum area of a rectangle that can be formed in the histogram.
        """
        # Step 1 - Initialize the stack and variable to store the max area.
        stack = []  # Holds (height, index)
        max_area = 0

        # Step 2 - Traverse each bar in the histogram.
        for i, cur_height in enumerate(heights):
            # Step 3 - Process bars in the stack taller than the current bar.
            while stack and stack[-1][0] > cur_height:
                height, _ = stack.pop()
                # Calculate the width of the rectangle using the current index.
                width = i if not stack else i - stack[-1][1] - 1
                max_area = max(max_area, height * width)
            # Step 4 - Push the current bar and its index onto the stack.
            stack.append((cur_height, i))

        # Step 5 - Process any remaining bars in the stack.
        while stack:
            height, _ = stack.pop()
            # Calculate the width as if the right end extends beyond the histogram.
            width = len(heights) if not stack else len(heights) - stack[-1][1] - 1
            max_area = max(max_area, height * width)

        # Step 6 - Return the maximum area found.
        return max_area


def main():
    """Demonstrates the usage of the `Solution` class with test cases."""
    solution = Solution()

    # Test cases
    assert solution.largestRectangleArea([2, 1, 5, 6, 2, 3]) == 10, "Test Case 1 Failed"
    assert solution.largestRectangleArea([2, 4]) == 4, "Test Case 2 Failed"
    assert solution.largestRectangleArea([2, 0, 2]) == 2, "Edge Case 1 Failed"
    assert solution.largestRectangleArea([5, 4, 1, 2]) == 8, "Edge Case 2 Failed"
    assert solution.largestRectangleArea([9, 0]) == 9, "Edge Case 3 Failed"

    print("All test cases passed!")


if __name__ == "__main__":
    main()
