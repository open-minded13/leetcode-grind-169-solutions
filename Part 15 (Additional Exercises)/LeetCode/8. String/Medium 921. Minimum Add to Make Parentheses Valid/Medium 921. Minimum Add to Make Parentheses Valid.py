"""Solves the problem of making a parentheses string valid.

This module provides a solution class with a method to calculate the minimum
number of insertions required to make a given string of parentheses valid. The
approach used involves counting unbalanced parentheses throughout a single
pass of the string.

Typical usage example:

solution = Solution()
assert solution.minAddToMakeValid("())") == 1
assert solution.minAddToMakeValid("(((") == 3
assert solution.minAddToMakeValid("()))((") == 4
assert solution.minAddToMakeValid("()()") == 0
assert solution.minAddToMakeValid("") == 0
"""

# Date of Last Practice: Mar 17, 2024 -> Sep 14, 2024
#
# Time Complexity: O(N), where N is the length of the string.
#                  This is because the solution iterates through each character of
#                  the string exactly once.
#
# Space Complexity: O(1). The solution uses only a constant amount of extra space
#                   to store the variables left_parenthesis and right_parenthesis,
#                   regardless of the size of the input string.


class Solution:
    """Calculates the minimum insertions to validate a string.

    Attributes:
        None
    """

    def minAddToMakeValid(self, s: str) -> int:
        """Calculates the minimum number of parenthesis insertions needed.

        This method calculates the required number of insertions by tracking
        unbalanced opening and closing parentheses while iterating through
        the string. It uses two counters: one for unbalanced open parentheses
        and another for unbalanced closed parentheses.

        Args:
            s (str): The input string consisting of '(' and ')' characters.

        Returns:
            int: The minimum number of insertions required to make the string valid.

        Example:
            >>> solution = Solution()
            >>> solution.minAddToMakeValid("())")
            1
            >>> solution.minAddToMakeValid("(((")
            3
        """
        left_parenthesis, right_parenthesis = 0, 0

        for char in s:
            if char == "(":
                left_parenthesis += 1
            elif char == ")" and left_parenthesis > 0:
                left_parenthesis -= 1
            else:
                right_parenthesis += 1

        return left_parenthesis + right_parenthesis


def main():
    """Validate the minAddToMakeValid method of Solution class."""
    solution = Solution()
    assert solution.minAddToMakeValid("())") == 1, "Test case 1 failed"
    assert solution.minAddToMakeValid("(((") == 3, "Test case 2 failed"
    assert solution.minAddToMakeValid("()))((") == 4, "Test case 3 failed"
    assert solution.minAddToMakeValid("()()") == 0, "Test case 4 failed"
    assert solution.minAddToMakeValid("") == 0, "Test case 5 failed"
    print("All test cases passed successfully!")


if __name__ == "__main__":
    main()
