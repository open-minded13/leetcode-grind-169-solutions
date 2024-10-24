"""
Evaluates a basic mathematical expression in a string.

This module defines a class `Solution` that provides a method to evaluate a basic 
mathematical expression with addition, subtraction, and parentheses.

Example usage:
    sol = Solution()
    result = sol.calculate("1 + (2 - 3)")
"""

# Date of Last Practice: Mar 5, 2024 -> Oct 24, 2024
#
# Time Complexity: O(N), where N is the length of the input string. Each character
#                  in the string s is visited once.
#
# Space Complexity: O(N), where N is the length of the input string.
#                   In the worst case, the recursion depth can be proportional to the
#                   length of the string if there are nested parentheses.


class Solution:
    """Calculates the result of a basic mathematical expression."""

    def calculate(self, s: str) -> int:
        """Evaluates the given string representing a mathematical expression.

        Args:
            s: A string representing a valid mathematical expression.

        Returns:
            An integer that is the result of evaluating the expression.
        """

        def new_bracket(index):
            """Helper function to handle expressions recursively."""
            total = 0
            is_plus_sign = True  # Tracks if the current operator is '+' or '-'.

            # Step 1 - Iterate through the string.
            while index < len(s):
                char = s[index]

                if char == "+" or char == "-":
                    # Step 2 - Update the current operator.
                    is_plus_sign = char == "+"

                elif char == ")":
                    # Step 3 - End of current sub-expression, return result.
                    return total, index

                elif char == "(":
                    # Step 4 - Recursive call for nested expressions inside parentheses.
                    sub_total, index = new_bracket(index + 1)
                    # Add or subtract based on the operator.
                    total += sub_total if is_plus_sign else -sub_total

                elif char.isdigit():
                    # Step 5 - Parse multi-digit numbers.
                    value = int(char)
                    while index + 1 < len(s) and s[index + 1].isdigit():
                        value = value * 10 + int(s[index + 1])
                        index += 1
                    total += value if is_plus_sign else -value

                # Step 6 - Move to the next character.
                index += 1

            return total, index

        # Step 7 - Call the recursive function starting from index 0.
        return new_bracket(0)[0]


# Test cases
if __name__ == "__main__":
    sol = Solution()

    # Basic arithmetic tests
    assert sol.calculate("1 + 1") == 2  # Step 1: Basic addition
    assert sol.calculate(" 2-1 + 2 ") == 3  # Step 2: Mixed operators

    # Parentheses tests
    assert sol.calculate("(1+(4+5+2)-3)+(6+8)") == 23  # Step 3: Nested parentheses
    assert sol.calculate("-(2 + 3)") == -5  # Step 4: Unary minus

    # Large number tests
    assert sol.calculate("2147483647") == 2147483647  # Step 5: Large number

    print("All test cases passed.")
