from typing import List

# Date of Last Practice: Nov 19, 2023 -> Feb 4, 2024
#
# Time Complexity: O(N), where N is the number of tokens in the input list.
#                  This is because we iterate through each token once.
#
# Space Complexity: O(N), where N is the number of nodes in the graph.
#                   This is because the number of stacks we use is proportional to the number of tokens.
#                   In the worst case, when all operators are put at the end of the tokens list,
#                   we will use almost N stacks to store operands.


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])

        operators = set(["+", "-", "*", "/"])
        stack = []

        for char in tokens:
            if char in operators:
                operand_2 = stack.pop()
                operand_1 = stack.pop()
                if char == "+":
                    stack.append(operand_1 + operand_2)
                elif char == "-":
                    stack.append(operand_1 - operand_2)
                elif char == "*":
                    stack.append(operand_1 * operand_2)
                elif char == "/":
                    # Note: The int() conversion ensures the result is an integer in Python 3.
                    # If the division result is not a whole number,
                    # it will be truncated to the nearest integer towards zero.
                    # `int(-7 / 2) = -3` vs `-7 // 2 = -4`
                    stack.append(int(operand_1 / operand_2))
            else:
                stack.append(int(char))

        return stack.pop()


# Test cases
solution = Solution()
print(solution.evalRPN(["2", "1", "+", "3", "*"]))  # Output: 9
print(solution.evalRPN(["4", "13", "5", "/", "+"]))  # Output: 6
print(
    solution.evalRPN(["10", "6", "9", "3", "/", "-11", "*", "+", "*", "17", "+"])
)  # Output: -253
