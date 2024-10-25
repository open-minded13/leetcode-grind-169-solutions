import math

# Date of Last Practice: Mar 11, 2024 -> Oct 25, 2024
#
# Time Complexity: O(N), where N is the length of the string s.
#                  We iterate over each character of the string exactly once, O(N).
#                  Finally, we add up all the elements in the stack, which in the
#                  worst case (when the expression consists entirely of addition and
#                  subtraction operations) can be proportional to the length of the
#                  string. This also results in a time complexity of O(N).
#
# Space Complexity: O(N), where N is the length of the string s.
#                   In the worst-case scenario, if the expression consists entirely
#                   of addition and subtraction operations, the stack might store a
#                   number for nearly every operands in the input string. Since the
#                   number of operands is proportional to the length of the string,
#                   this results in O(N).


class Solution:
    """Evaluates an arithmetic expression represented as a string."""

    def calculate(self, s: str) -> int:
        """Evaluates the given arithmetic expression and returns the result.

        Args:
            s (str): The arithmetic expression containing non-negative integers
                and operators ('+', '-', '*', '/') separated by spaces.

        Returns:
            int: The result of evaluating the arithmetic expression.
        """
        stack = []
        index = 0
        operator = "+"  # Default operator is '+'

        while index < len(s):
            char = s[index]

            # Step 1 - Update the operator when encountering '+', '-', '*', or '/'.
            if char in "+-*/":
                operator = char
            # Step 2 - Parse digits to form a number.
            elif char.isdigit():
                value = int(char)
                while index + 1 < len(s) and s[index + 1].isdigit():
                    value = value * 10 + int(s[index + 1])
                    index += 1

                # Step 3 - Apply the parsed value based on the current operator.
                if operator == "+":
                    stack.append(value)
                elif operator == "-":
                    stack.append(-value)
                elif operator == "*":
                    stack[-1] *= value
                elif operator == "/":
                    stack[-1] = math.trunc(stack[-1] / value)

                # Reset the operator to handle subsequent numbers.
                operator = "+"
            index += 1

        # Step 4 - Sum all elements in the stack to compute the final result.
        return sum(stack)


def main():
    """Runs test cases for the Solution class's calculate function."""
    solution = Solution()

    # Test cases to validate the solution.
    assert solution.calculate("3+2*2") == 7, "Test case 1 failed"
    assert solution.calculate(" 3/2 ") == 1, "Test case 2 failed"
    assert solution.calculate(" 3+5 / 2 ") == 5, "Test case 3 failed"
    assert solution.calculate("1*2-3/4+5*6-7*8+9/10") == -24, "Test case 4 failed"

    print("All test cases passed successfully.")


if __name__ == "__main__":
    main()
