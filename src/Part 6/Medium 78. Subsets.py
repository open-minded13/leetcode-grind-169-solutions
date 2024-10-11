from typing import List

# Date of Last Practice: Dec 31, 2023 -> Feb 20, 2024
#
# Time Complexity: O(2^N), where N is the length of the input nums array.
#                  Each element in the array has two choices —
#                  either to be included in the current subset or not.
#                  This leads to 2^N different combinations.
#
# Space Complexity: O(N), where N is the length of the input nums array.
#                   The maximum depth of the recursive call stack is O(N).
#                   The combination list also takes up space, but since it is reused and
#                   never holds more than N elements at a time,
#                   it contributes O(N) to the space complexity.
#
#                   We are storing all 2^N subsets, and each subset can be
#                   up to N elements in size. However, this is usually not considered in
#                   space complexity analysis as it is required for the output.


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = []

        def find_subset(index, combination):
            if index == len(nums):
                output.append(list(combination))
                return
            find_subset(index + 1, combination)
            combination.append(nums[index])
            find_subset(index + 1, combination)
            combination.pop()

        find_subset(0, [])
        return output


# Test cases
sol = Solution()

# Test case 1
nums1 = [1, 2, 3]
expected1 = [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
assert sorted(sol.subsets(nums1)) == sorted(
    expected1
), f"Test Case 1 Failed: {sol.subsets(nums1)}"

# Test case 2
nums2 = [0]
expected2 = [[], [0]]
assert sorted(sol.subsets(nums2)) == sorted(
    expected2
), f"Test Case 2 Failed: {sol.subsets(nums2)}"

# Test case 3
nums3 = [1, 2, 3, 4]
expected3 = [
    [],
    [1],
    [2],
    [1, 2],
    [3],
    [1, 3],
    [2, 3],
    [1, 2, 3],
    [4],
    [1, 4],
    [2, 4],
    [1, 2, 4],
    [3, 4],
    [1, 3, 4],
    [2, 3, 4],
    [1, 2, 3, 4],
]
assert sorted(sol.subsets(nums3)) == sorted(
    expected3
), f"Test Case 3 Failed: {sol.subsets(nums3)}"

# Test case 4
nums4 = [-1, 0, 1]
expected4 = [[], [-1], [0], [-1, 0], [1], [-1, 1], [0, 1], [-1, 0, 1]]
assert sorted(sol.subsets(nums4)) == sorted(
    expected4
), f"Test Case 4 Failed: {sol.subsets(nums4)}"

# Test case 5
nums5 = []
expected5 = [[]]
assert sorted(sol.subsets(nums5)) == sorted(
    expected5
), f"Test Case 5 Failed: {sol.subsets(nums5)}"

print("All test cases passed!")
