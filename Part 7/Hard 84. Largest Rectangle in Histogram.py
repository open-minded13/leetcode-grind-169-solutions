# Time Complexity: O(N), where N is the length of the input list (heights).
#                  This efficiency is achieved because each bar is pushed onto
#                  the stack once and popped once.
#
# Space Complexity: O(N), where N is the length of the input list (heights).
#                   We use an additional stack to store indices of the bars.

from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []
        for i, h in enumerate(heights):
            while stack and h < heights[stack[-1]]:
                index = stack.pop()
                height = heights[index]
                width = i - stack[-1] - 1 if stack else i
                max_area = max(height * width, max_area)
            stack.append(i)

        n = len(heights)
        while stack:
            index = stack.pop()
            height = heights[index]
            width = n - stack[-1] - 1 if stack else n
            max_area = max(height * width, max_area)

        return max_area


# Test cases
solution = Solution()

# Test Case 1
assert solution.largestRectangleArea([2, 1, 5, 6, 2, 3]) == 10

# Test Case 2
assert solution.largestRectangleArea([2, 4]) == 4

print("Test cases passed!")
