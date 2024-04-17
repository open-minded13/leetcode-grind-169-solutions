from typing import List

# Date of Last Practice: Jan 25, 2024 -> Feb 29, 2024
#
# Time Complexity: O(N), where N is the length of the height list.
#                  The two-pointer technique helps us iterate each element once.
#
# Space Complexity: O(1). We use constant space to store variables.


class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        max_left = 0
        right = len(height) - 1
        max_right = 0
        trapped_water = 0

        while left < right:
            if height[left] < height[right]:
                max_left = max(max_left, height[left])
                trapped_water += max_left - height[left]
                left += 1
            else:
                max_right = max(max_right, height[right])
                trapped_water += max_right - height[right]
                right -= 1

        return trapped_water


class Second_Solution:
    def trap(self, height: List[int]) -> int:
        water_trapped = 0

        # left to right, including the [2, 0, 2] situation
        temp = 0
        left, right = 0, 0
        while left <= right < len(height):
            if height[right] < height[left]:
                temp += height[left] - height[right]
            else:
                water_trapped += temp
                temp = 0
                left = right
            right += 1

        # right to left
        temp = 0
        left, right = len(height) - 1, len(height) - 1
        while 0 <= left <= right:
            if height[left] <= height[right]:
                temp += height[right] - height[left]
                left -= 1
            else:
                water_trapped += temp
                temp = 0
                right = left

        return water_trapped


class First_Solution:
    # Time Complexity: O(N * log N), where N is the length of the height list.
    #                  The sorting step dominates the time complexity, which is O(N * log N).
    #                  The while loop (outer loop) iterates N times.
    #                  And inside the while loop, because each element is checked only once
    #                  and then assigned a big number to prevent checking again.
    #                  Therefore, O(N + N) = O(N).
    #
    # Space Complexity: O(N). We create a h_with_index list of length len(height).

    def trap(self, height: List[int]) -> int:
        max_h = 0
        h_with_index = []
        for index, h in enumerate(height):
            h_with_index.append((h, index))
        h_with_index = sorted(h_with_index)

        count = 0
        h1, index_1 = h_with_index.pop()
        left, right = len(height), -1
        while h_with_index:
            h2, index_2 = h_with_index.pop()

            if index_1 < index_2 and index_2 > right:
                for i in range(index_1 + 1, index_2):
                    if height[i] < h2:
                        count += h2 - height[i]
                        height[i] = 10**5 + 1
                right = index_2
            elif index_2 < left:
                for i in range(index_2 + 1, index_1):
                    if height[i] < h2:
                        count += h2 - height[i]
                        height[i] = 10**5 + 1
                left = index_2

        return count


# Test cases
sol = Solution()
assert sol.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6
assert sol.trap([4, 2, 0, 3, 2, 5]) == 9
assert sol.trap([]) == 0
assert sol.trap([0]) == 0
assert sol.trap([1]) == 0
assert sol.trap([2, 2, 2, 2, 2]) == 0
assert sol.trap([3, 0, 3]) == 3
assert sol.trap([1, 3, 2, 4, 1, 3, 1, 4, 5]) == 8
assert sol.trap([1, 2, 3, 4, 5]) == 0
assert sol.trap([5, 4, 3, 2, 1]) == 0
assert sol.trap([5, 1, 2, 3, 4, 1, 5]) == 14

print("All test cases passed!")
