from typing import List

# Date of Last Practice: Dec 18, 2023 -> Feb 8, 2024
#
# Time Complexity: O(N), where N is the length of the input array.
#
# Space Complexity: O(1) if we don't count the output array (i.e., answers) as extra space.
#                   The extra space used by the algorithm is the right_product variable,
#                   which is constant space.


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # answers = [1 for _ in range(len(nums))]
        answers = [1] * len(nums)

        # First pass: Products to the left of each index.
        for i in range(1, len(nums)):
            answers[i] = nums[i - 1] * answers[i - 1]

        # Second pass: Products to the right of each index.
        right_product = 1
        # for i in range(len(nums)-1, -1, -1):
        for i in reversed(range(len(nums))):
            answers[i] *= right_product
            right_product *= nums[i]

        return answers


# Test cases
sol = Solution()

# Test case 1
print("Test Case 1:")
nums = [1, 2, 3, 4]
print(f"Input: {nums}")
print(f"Output: {sol.productExceptSelf(nums)}")  # Expected: [24, 12, 8, 6]

# Test case 2
print("\nTest Case 2:")
nums = [-1, 1, 0, -3, 3]
print(f"Input: {nums}")
print(f"Output: {sol.productExceptSelf(nums)}")  # Expected: [0, 0, 9, 0, 0]
