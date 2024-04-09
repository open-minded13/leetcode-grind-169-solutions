# Date of Last Practice: Jan 30, 2024 -> Mar 3, 2024
#
# Time Complexity: O(N), where N is the number of bars in the histogram.
#                  This efficiency is achieved because each bar is
#                  pushed onto the stack once and popped once.
#
# Space Complexity: O(N), where N is the number of bars in the histogram.
#                   We use an additional stack to store indices of the bars.

import sys
from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = -sys.maxsize - 1
        for i in range(len(heights)):
            # Remove bars from the stack while the current bar is shorter.
            while stack and heights[stack[-1]] > heights[i]:
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, height * width)
            stack.append(i)

        # Handle the remaining bars in the stack.
        while stack:
            height = heights[stack.pop()]
            width = len(heights) if not stack else len(heights) - stack[-1] - 1
            max_area = max(max_area, height * width)

        return max_area


# Test cases
solution = Solution()

# Test Case 1
assert solution.largestRectangleArea([2, 1, 5, 6, 2, 3]) == 10

# Test Case 2
assert solution.largestRectangleArea([2, 4]) == 4

print("Test cases passed!")
