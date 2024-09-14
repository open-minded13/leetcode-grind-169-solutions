"""
Solve the 'Product of Array Except Self' problem from LeetCode.

This module defines a class `Solution` that contains a method `productExceptSelf`
which, given an integer array `nums`, returns an array `answer` such that
`answer[i]` is equal to the product of all the elements of `nums` except `nums[i]`.

The method adheres to O(n) time complexity and uses O(1) space complexity (excluding
the space required for the output array).

Typical usage example:

sol = Solution()
result = sol.productExceptSelf([1, 2, 3, 4])  # Returns [24, 12, 8, 6]
"""

from typing import List

# Date of Last Practice: Dec 18, 2023 -> Feb 8, 2024 -> Sep 14, 2024
#
# Time Complexity: O(N), where N is the length of the input array.
#
# Space Complexity: O(1) if we don't count the output array (i.e., answers).
#                   The extra space used by the algorithm is the `product` variable,
#                   which is constant space.


class Solution:
    """
    A class used to solve the 'Product of Array Except Self' problem.

    Methods
    -------
    productExceptSelf(nums: List[int]) -> List[int]
        Returns an array such that each element at index `i` is the product of all
        elements in the input array `nums` except `nums[i]`.
    """

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Calculate the product of all elements except self in O(n) time and O(1) space.

        Args:
            nums (List[int]): The input array of integers.

        Returns:
            List[int]: The output array where each element is the product of all the
                       elements of `nums` except `nums[i]`.
        """

        # Step 1 - Check if the input array is empty or has only one element
        nums_length = len(nums)
        if nums_length < 2:
            return []

        # Step 2 - Initialize an array 'result' with ones to store left-side products
        result = [1] * nums_length

        # Step 2 - Traverse from left to right, calculating the product of all elements
        # to the left of the current index and storing it in the 'result' array
        product = 1
        for i in range(nums_length):
            result[i] = product  # Store the product of elements to the left
            product *= nums[i]  # Update product for the next element

        # Step 3 - Traverse from right to left, calculating the product of all elements
        # to the right of the current index and multiplying it with the current result
        product = 1
        for i in range(nums_length - 1, -1, -1):
            result[i] *= product  # Multiply the result by the product of right elements
            product *= nums[i]  # Update product for the next element

        # Step 4 - Return the final result array
        return result


# Test cases
def test_solution():
    """
    Test the 'productExceptSelf' method with various test cases.
    """
    sol = Solution()

    # Test case 1
    nums = [1, 2, 3, 4]
    expected_output = [24, 12, 8, 6]
    assert sol.productExceptSelf(nums) == expected_output, "Test case 1 failed"

    # Test case 2
    nums = [-1, 1, 0, -3, 3]
    expected_output = [0, 0, 9, 0, 0]
    assert sol.productExceptSelf(nums) == expected_output, "Test case 2 failed"

    # Test case 3: Single element array
    nums = [5]
    expected_output = []
    assert sol.productExceptSelf(nums) == expected_output, "Test case 3 failed"

    # Test case 4: Empty array
    nums = []
    expected_output = []
    assert sol.productExceptSelf(nums) == expected_output, "Test case 4 failed"

    print("All test cases passed!")


# Run the test cases
if __name__ == "__main__":
    test_solution()
