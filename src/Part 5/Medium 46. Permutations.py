# Date of Last Practice: Dec 23, 2023 -> Feb 12, 2024
#
# Time Complexity: O(N!), where N is the amount of the input nums.
#                  The recursion depth is N (since we are generating permutations of N elements),
#                  and at each level, we are iterating N times. However, due to the used_num constraint,
#                  the actual number of iterations decreases as the recursion depth increases:
#                  At the first level, there are N options.
#                  At the second level, there are N-1 options, and so on.
#                  This results in N * (N-1) * (N-2) * ... * 1, which is N!.
#
# Space Complexity: O(N), where N is the amount of the input nums.
#                   The maximum depth of the recursive call stack is N
#                   as we explore each element for permutations.
#                   The maximum size of the combination list is N.
#                   The size of used_num is always N.


class Solution:
    def permute(self, nums):
        def backtrack(combination):
            if len(combination) == len(nums):
                results.append(list(combination))
                return

            for i in range(len(nums)):
                if not used_num[nums[i]]:
                    used_num[nums[i]] = True
                    combination.append(nums[i])
                    backtrack(combination)
                    combination.pop()
                    used_num[nums[i]] = False

        used_num = {num: False for num in nums}
        results = []
        backtrack([])

        return results


# Test cases
sol = Solution()

# Test case 1
nums1 = [1, 2, 3]
print(
    "Test Case 1:", sol.permute(nums1)
)  # Expected Output: All permutations of [1, 2, 3]

# Test case 2
nums2 = [0, 1]
print("Test Case 2:", sol.permute(nums2))  # Expected Output: All permutations of [0, 1]

# Test case 3
nums3 = [1]
print("Test Case 3:", sol.permute(nums3))  # Expected Output: All permutations of [1]

# Test case with larger input
nums4 = [1, 2, 3, 4]
print(
    "Test Case 4:", sol.permute(nums4)
)  # Expected Output: All permutations of [1, 2, 3, 4]
