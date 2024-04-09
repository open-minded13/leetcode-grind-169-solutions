# Date of Last Practice: Jan 5, 2024 -> Feb 21, 2024
#
# Time Complexity: O(N*S), where N is the number of elements in the array.
#                  We iterate over each element to calculate the sum of the array, O(N).
#                  The core of the algorithm is the dynamic programming part.
#                  We iterate over each element in the array O(N), and for each element,
#                  we potentially iterate over a range up to the half_sum O(S/2).
#                  Therefore, O(N) + O(N*S/2) = O(N*S).
#
# Space Complexity: O(S), where S is the sum of the array.
#                   The space complexity is primarily dictated by the size of
#                   the dynamic programming array, which is of size S/2 + 1.


class Solution:
    def canPartition(self, nums):
        total_sum = sum(nums)

        # If total sum is odd, partition is not possible
        if total_sum % 2 != 0:
            return False

        half_sum = total_sum // 2

        dp = [False] * (half_sum + 1)
        dp[0] = True

        for num in nums:
            for i in range(half_sum, num - 1, -1):
                dp[i] = dp[i] or dp[i - num]

        return dp[half_sum]


# Test cases
solution = Solution()

# Test case 1
nums1 = [1, 5, 11, 5]
assert solution.canPartition(nums1) == True

# Test case 2
nums2 = [1, 2, 3, 5]
assert solution.canPartition(nums2) == False

# Additional test cases
assert solution.canPartition([1, 1, 3, 4, 7]) == True
assert solution.canPartition([2, 3, 4, 6]) == False

print("All test cases passed!")
