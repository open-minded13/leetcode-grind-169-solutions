import math

# Date of Last Practice: Mar 11, 2024
#
# Time Complexity: O(N), where N is the length of the string s.
#                  We iterate over each character of the string exactly once,
#                  which is O(N). Finally, we add up all the elements in the stack,
#                  which in the worst case (when the expression consists entirely of addition
#                  and subtraction operations) can be proportional to the length of the string.
#                  This also results in a time complexity of O(N).
#
# Space Complexity: O(N), where N is the length of the string s.
#                   In the worst-case scenario, if the expression consists
#                   entirely of addition and subtraction operations,
#                   the stack might store a number for nearly every operands
#                   in the input string. Since the number of operands is
#                   proportional to the length of the string, this results in O(N).


class Solution:
    def calculate(self, s: str) -> int:
        operand, prev_sign, stack = 0, "+", []
        for char in s + "+":
            if char.isdigit():
                operand = operand * 10 + int(char)
            elif char in "+-*/":
                if prev_sign == "+":
                    stack.append(operand)
                elif prev_sign == "-":
                    stack.append(-operand)
                elif prev_sign == "*":
                    stack.append(stack.pop() * operand)
                else:
                    stack.append(math.trunc(stack.pop() / operand))
                operand, prev_sign = 0, char
        return sum(stack)


# Initialize Solution object
solution = Solution()

# Test case 1: Simple addition and multiplication
assert solution.calculate("3+2*2") == 7, "Test case 1 failed"

# Test case 2: Simple division
assert solution.calculate(" 3/2 ") == 1, "Test case 2 failed"

# Test case 3: Combination of operations
assert solution.calculate(" 3+5 / 2 ") == 5, "Test case 3 failed"

# Test case 4: More complex expression with multiple types of operations
assert solution.calculate("1*2-3/4+5*6-7*8+9/10") == -24, "Test case 4 failed"

print("All test cases passed successfully.")
