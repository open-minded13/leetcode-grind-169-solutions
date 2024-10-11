"""
Find the missing number in an array containing distinct numbers.

This module defines a class `Solution` with a method `missingNumber` that
identifies the missing number from a sequence of distinct integers in the range
[0, n], where n is the length of the list.

Typical usage example:

    nums = [3, 0, 1]
    solution = Solution()
    result = solution.missingNumber(nums)
    print(result)  # Output: 2
"""

from typing import List

# Date of Last Practice: Aug 28, 2024
#
# Time Complexity: O(N), where N is the number of elements in the input list nums.
#
# Space Complexity: O(1), as the function uses a constant amount of extra space.


class Solution:
    """
    Represent the solution for finding the missing number.
    """

    def missingNumber(self, nums: List[int]) -> int:
        """
        Find the missing number from a list of distinct integers.

        This method uses the formula for the sum of the first n natural numbers
        to compute the expected sum and subtracts the sum of the given numbers
        to identify the missing one.

        Args:
            nums (List[int]): A list of distinct integers.

        Returns:
            int: The missing integer in the range [0, n].
        """
        # Step 1 - Determine the length of the list.
        length = len(nums)

        # Step 2 - Calculate the expected sum of numbers from 0 to n.
        expected_sum = (1 + length) * length // 2

        # Step 3 - Subtract the sum of elements in the nums list from the expected sum.
        for num in nums:
            expected_sum -= num

        # Step 4 - The result is the missing number.
        return expected_sum

    def missingNumberXOR(self, nums: List[int]) -> int:
        """
        Find the missing number from a list of distinct integers using the XOR method.

        This method leverages the properties of XOR where a number XORed with itself
        results in 0, and a number XORed with 0 remains unchanged. By XORing all the
        indices and the numbers in the list, the missing number can be identified.

        Since XOR is commutative and associative, the order of XOR operations does not
        matter, and the result after all XOR operations is the missing number. Therefore,
        the following two-pass XOR operation can be simplified to a single pass.

        ```python
        missing = 0
        for i in range(0, len(nums)+1):
            missing ^= i ^ nums
        for num in nums:
            missing ^= num
        return missing
        ```

        Args:
            nums (List[int]): A list of distinct integers.

        Returns:
            int: The missing integer in the range [0, n].
        """
        # Step 1 - Initialize result with the last index (length).
        missing = len(nums)

        # Step 2 - XOR all indices and numbers in the list.
        for i, num in enumerate(nums):
            missing ^= i ^ num

        # Step 3 - The result after all XOR operations is the missing number.
        return missing


def main():
    """
    Demonstrate the usage of the Solution class with test cases.
    """
    solution = Solution()

    # Test case 1
    nums = [3, 0, 1]
    assert solution.missingNumber(nums) == 2, "Test case 1 failed."
    assert solution.missingNumberXOR(nums) == 2, "Test case 1 XOR failed."

    # Test case 2
    nums = [0, 1]
    assert solution.missingNumber(nums) == 2, "Test case 2 failed."
    assert solution.missingNumberXOR(nums) == 2, "Test case 2 XOR failed."

    # Test case 3
    nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
    assert solution.missingNumber(nums) == 8, "Test case 3 failed."
    assert solution.missingNumberXOR(nums) == 8, "Test case 3 XOR failed."

    # Test case 4
    nums = [0]
    assert solution.missingNumber(nums) == 1, "Test case 4 failed."
    assert solution.missingNumberXOR(nums) == 1, "Test case 4 XOR failed."

    # Test case 5
    nums = [0, 2, 3]
    assert solution.missingNumber(nums) == 1, "Test case 5 failed."
    assert solution.missingNumberXOR(nums) == 1, "Test case 5 XOR failed."

    print("All test cases passed.")


if __name__ == "__main__":
    main()
