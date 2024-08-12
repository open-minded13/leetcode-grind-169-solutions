# Date of Last Practice: Mar 8, 2024
#
# Time Complexity: O(N), where N is the length of the input string.
#
# Space Complexity: O(N), where N is the length of the input string.


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:

        stack = []
        valid_list = list(s)
        for index, char in enumerate(s):
            if char == "(":
                stack.append(index)
            if char == ")":
                if stack:
                    stack.pop()
                else:
                    valid_list[index] = ""

        while stack:
            valid_list[stack.pop()] = ""

        return "".join(valid_list)


class AnotherSolution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # Step 1: Remove invalid ')' from left to right
        left_parentheses = 0
        left_valid_string = ""
        for char in s:
            if char == "(":
                left_parentheses += 1
            elif char == ")":
                if left_parentheses == 0:
                    continue  # Skip this char as it's an invalid ')'
                left_parentheses -= 1
            left_valid_string += char

        # Step 2: Remove invalid '(' from right to left
        right_parentheses = 0
        valid_string = ""
        for char in reversed(left_valid_string):
            if char == ")":
                right_parentheses += 1
            elif char == "(":
                if right_parentheses == 0:
                    continue  # Skip this char as it's an invalid '('
                right_parentheses -= 1
            valid_string = char + valid_string

        return valid_string


# Test cases
sol = Solution()
assert sol.minRemoveToMakeValid("lee(t(c)o)de)") == "lee(t(c)o)de"
assert sol.minRemoveToMakeValid("a)b(c)d") == "ab(c)d"
assert sol.minRemoveToMakeValid("))((") == ""
assert sol.minRemoveToMakeValid("(a(b(c)d)") == "a(b(c)d)"

# Print "All tests passed" if no assertion fails
print("All tests passed.")
