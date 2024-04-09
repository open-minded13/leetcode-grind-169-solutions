# Date of Last Practice: Oct 17, 2023 -> Jan 29, 2024
#
# Time Complexity: O(log N), where N is the number of elements in the nums array.
#                            In each iteration of the while loop,
#                            you effectively halve the search space by updating the left or right pointer.
#                            This logarithmic behavior makes binary search an efficient algorithm
#                            for searching in sorted arrays.
# Space Complexity: O(1) because the space used by the variables left, right, and pivot is not dependent
#                   on the size of the input array.

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            pivot = (left + right) // 2
            if target == nums[pivot]:
                return pivot
            elif target > nums[pivot]:
                left = pivot + 1
            else:
                right = pivot - 1
        return -1


# Test cases
if __name__ == "__main__":
    solution = Solution()

    # Example test cases
    nums = [-1, 0, 3, 5, 9, 12]
    target = 9
    result = solution.search(nums, target)
    print(result)  # Output should be 4

    nums = [-1, 0, 3, 5, 9, 12]
    target = 2
    result = solution.search(nums, target)
    print(result)  # Output should be -1

    # Additional test cases
    nums = [1, 2, 3, 4, 5, 6, 7, 8]
    target = 5
    result = solution.search(nums, target)
    print(result)  # Output should be 4

    nums = [1, 2, 3, 4, 5, 6, 7, 8]
    target = 10
    result = solution.search(nums, target)
    print(result)  # Output should be -1
