# Date of Last Practice: Aug 31, 2023 -> Jan 25, 2024
#
# Time Complexity: O(N), where n is the length of the input string because
#                  the method iterates through each character in the input string.
#
# Space Complexity: O(N), where n is the maximum of the size of the stack,
#                   depending on the input string. This is because, in the worst case,
#                   the method keeps adding a new stack if it can't find the correct closing bracket.


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char == "(" or char == "{" or char == "[":
                stack.append(char)
            else:
                # Using `if not stack` is critical, or `the stack[-1] == "("` judgement will generate an error.
                # IndexError: list index out of range
                if not stack:
                    return False
                if char == ")" and stack[-1] == "(":
                    stack.pop()
                elif char == "]" and stack[-1] == "[":
                    stack.pop()
                elif char == "}" and stack[-1] == "{":
                    stack.pop()
                else:
                    stack.append(char)
        if len(stack) == 0:
            return True
        else:
            return False


# Test Cases
test_cases = [
    "()",
    "()[]{}",
    "(]",
    "([)]",
    "{[]}",
    "((())",
    "",
    "[[[]]]",
    "{{{}}}]",
]

solution = Solution()

for test_case in test_cases:
    is_valid = solution.isValid(test_case)
    print(f"Input: {test_case}\nOutput: {is_valid}\n")
