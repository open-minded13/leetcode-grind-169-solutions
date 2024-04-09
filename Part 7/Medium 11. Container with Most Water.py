# Date of Last Practice: Jun 14, 2023 -> Feb 21, 2024
#
# Time Complexity: O(N), where N is the length of the input list (height).
#                  This is because the algorithm iterates over the list once in a loop.
#                  Each iteration performs constant time operations,
#                  such as comparisons and arithmetic calculations.
#
# Space Complexity: O(1). The algorithm only uses a constant amount of extra space
#                   to store variables (max_area, left, and right).
#                   Regardless of the size of the input list,
#                   the amount of memory used by the algorithm remains the same.


# Optimized Solution: Two-Pointer Technique
#
# In each iteration, we move the pointer with the smaller height towards the center.
# This is because moving the pointer with the larger height will only decrease the width
# and can never increase the area.


class Solution:
    def maxArea(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:
            area = min(height[left], height[right]) * (right - left)
            max_area = area if area > max_area else max_area
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area


class Brute_Force_Solution:
    def maxArea(self, height: list[int]) -> int:
        max_area = 0
        for start_x in range(len(height)):
            for end_x in range(start_x, len(height)):
                area = (end_x - start_x) * min(height[end_x], height[start_x])
                max_area = area if area > max_area else max_area
        return max_area


# Test Cases
solution = Solution()

# Example Case
height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
# The max area is min(1, 7) * 7 = 49
assert solution.maxArea(height) == 49

# Additional Cases
height = [4, 3, 2, 1, 4]
# The max area is min(4, 4) * 4 = 16
assert solution.maxArea(height) == 16

height = [1, 2, 1]
# The max area is min(1, 1) * 2 = 2
assert solution.maxArea(height) == 2

height = [1, 1]
# The max area is min(1, 1) * 1 = 1
assert solution.maxArea(height) == 1

height = [1, 2, 4, 3]
# The max area is min(2, 3) * 2 = 4
assert solution.maxArea(height) == 4

height = [2, 3, 10, 5, 7, 8, 9]
# The max area is min(10, 9) * 4 = 36
assert solution.maxArea(height) == 36

print("All test cases passed!")
