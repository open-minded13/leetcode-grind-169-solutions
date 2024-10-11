"""
Module for checking if an integer is a palindrome without converting it to a string.

This module defines a class `Solution` with a method to determine whether a given 
integer is a palindrome. The solution avoids converting the integer to a string and
operates with O(1) space complexity.
"""

# Date of Last Practice: Aug 24, 2024
#
# Time Complexity: O(log10(x)), where x is the input integer.
#                  We divide the input integer by 10 for each iteration.
#
# Space Complexity: O(1), as we only use a constant amount of extra space.


class Solution:
    """
    Provides a method to check if an integer is a palindrome.

    Methods:
        is_palindrome(x): Returns True if `x` is a palindrome, False otherwise.
    """

    def is_palindrome(self, x: int) -> bool:
        """
        Check if the given integer is a palindrome without converting it to a string.

        Args:
            x (int): The integer to check.

        Returns:
            bool: True if `x` is a palindrome, False otherwise.
        """

        # Step 1 - Handle edge cases where x is negative or ends in 0 (and is not 0).
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reversed_number = 0

        # Step 2 - Reverse the second half of the number.
        while x > reversed_number:
            reversed_number = reversed_number * 10 + x % 10
            x //= 10

        # Step 3 - Check if the number is a palindrome.
        # Compare the first half and the reversed second half.
        return x == reversed_number or x == reversed_number // 10


def main():
    """
    Main function to demonstrate the Solution class.
    """
    solution = Solution()

    # Step 4 - Test cases with assertions to validate the solution.
    assert solution.is_palindrome(121) is True, "Test Case 1 Failed"
    assert solution.is_palindrome(-121) is False, "Test Case 2 Failed"
    assert solution.is_palindrome(10) is False, "Test Case 3 Failed"
    assert solution.is_palindrome(0) is True, "Test Case 4 Failed"
    assert solution.is_palindrome(12321) is True, "Test Case 5 Failed"

    print("All test cases passed.")


if __name__ == "__main__":
    main()
