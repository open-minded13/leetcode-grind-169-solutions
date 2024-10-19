"""Check if a string of parentheses is valid.

This module provides a class `Solution` with a method `isValid` to determine
whether a given string containing parentheses is valid. The validation checks
for correct matching and order of '()', '{}', and '[]'.

Typical usage example:

    solution = Solution()
    assert solution.isValid("()[]{}") == True
    assert solution.isValid("(]") == False
    assert solution.isValid("([{}])") == True
    assert solution.isValid("{[()]}") == True
"""

# Date of Last Practice: Aug 31, 2023 -> Jan 25, 2024
#
# Time Complexity: O(N), where n is the length of the input string because
#                  the method iterates through each character in the input string.
#
# Space Complexity: O(N), where n is the maximum of the size of the stack,
#                   depending on the input string. This is because, in the worst case,
#                   the method keeps adding a new stack if it can't find the correct
#                   closing bracket.


class Solution:
    """Validates if a string of parentheses is balanced and properly matched."""

    def isValid(self, s: str) -> bool:
        """Checks if a string of parentheses is valid.

        Args:
            s: A string containing only '(', ')', '{', '}', '[' and ']'.

        Returns:
            A boolean indicating if the parentheses in the input string are valid.
        """
        # Step 1 - Define a stack to keep track of open parentheses.
        stack = []
        # Step 2 - Define a mapping of closing to opening brackets for validation.
        matching_parentheses = {")": "(", "]": "[", "}": "{"}

        # Step 3 - Iterate through each character in the string.
        for char in s:
            # If the character is a closing bracket
            if char in matching_parentheses:
                # Step 4 - Pop the top element from the stack if it's not empty,
                # otherwise assign a dummy value (e.g., '#').
                top_element = stack.pop() if stack else "#"
                # Step 5 - Check if the popped element matches the expected opening
                #          bracket.
                if matching_parentheses[char] != top_element:
                    return False
            else:
                # Step 6 - If it's an opening bracket, push it onto the stack.
                stack.append(char)

        # Step 7 - Return True if the stack is empty (all open brackets matched).
        return not stack


def main():
    """Runs test cases for the Solution class."""
    solution = Solution()
    # Test cases with assertions.
    assert solution.isValid("()") is True, "Test case 1 failed"
    assert solution.isValid("()[]{}") is True, "Test case 2 failed"
    assert solution.isValid("(]") is False, "Test case 3 failed"
    assert solution.isValid("([{}])") is True, "Test case 4 failed"
    assert solution.isValid("{[()]}") is True, "Test case 5 failed"
    assert solution.isValid("([)]") is False, "Test case 6 failed"
    assert solution.isValid("{[]}") is True, "Test case 7 failed"
    assert solution.isValid("[") is False, "Test case 8 failed"
    assert solution.isValid("]") is False, "Test case 9 failed"
    assert solution.isValid("") is True, "Test case 10 failed"

    print("All test cases passed!")


if __name__ == "__main__":
    main()
