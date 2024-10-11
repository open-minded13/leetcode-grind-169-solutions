import sys

# Date of Last Practice: Jun 11, 2023 -> Feb 2, 2024
#
# Time Complexity: O(N), where N is the length of the input (nums).
#
# Space Complexity: O(1) because we use a constant amount of extra space to store extra variables.


class Solution:
    def maxSubArray(self, nums):
        sub_max_sum = -sys.maxsize - 1
        cur_sum = 0
        for num in nums:
            cur_sum = max(cur_sum + num, num)
            sub_max_sum = max(sub_max_sum, cur_sum)
        return sub_max_sum


# Test cases
def test_maxSubArray():
    solution = Solution()

    # Test case 1: [-2,1,-3,4,-1,2,1,-5,4]
    nums1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    assert solution.maxSubArray(nums1) == 6

    # Test case 2: [1]
    nums2 = [1]
    assert solution.maxSubArray(nums2) == 1

    # Test case 3: [5,4,-1,7,8]
    nums3 = [5, 4, -1, 7, 8]
    assert solution.maxSubArray(nums3) == 23

    # Test case 4: Empty array
    nums4 = []
    assert solution.maxSubArray(nums4) == -sys.maxsize - 1

    # Test case 5: All negative numbers
    nums5 = [-5, -3, -2, -8]
    assert solution.maxSubArray(nums5) == -2

    print("All test cases passed!")


if __name__ == "__main__":
    test_maxSubArray()
