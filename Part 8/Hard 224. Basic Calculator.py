# Date of Last Practice: Mar 5, 2024
#
# Time Complexity: O(N), where N is the length of the input string.
#                  Each character in the string s is visited once.
#
# Space Complexity:O(N), where N is the length of the input string.
#                  In the worst case, the recursion depth can be proportional to
#                  the length of the string if there are nested parentheses.


class Solution:
    def calculate(self, s: str) -> int:

        def _calculator(index):
            cur_level_result = 0
            cur_operator = True

            while index < len(s):
                if s[index] == " ":
                    index += 1
                    continue
                elif s[index] == "+":
                    cur_operator = True
                elif s[index] == "-":
                    cur_operator = False
                elif s[index] == "(":
                    next_level_result, index = _calculator(index + 1)
                    if cur_operator:
                        cur_level_result += next_level_result
                    else:
                        cur_level_result -= next_level_result
                elif s[index] == ")":
                    return cur_level_result, index
                else:
                    operand = int(s[index])
                    while index + 1 < len(s) and s[index + 1].isdigit():
                        operand *= 10
                        operand += int(s[index + 1])
                        index += 1
                    if cur_operator:
                        cur_level_result += operand
                    else:
                        cur_level_result -= operand

                index += 1

            return cur_level_result, index

        result, _ = _calculator(0)

        return result


# Test cases
sol = Solution()
assert sol.calculate("1 + 1") == 2
assert sol.calculate(" 2-1 + 2 ") == 3
assert sol.calculate("(1+(4+5+2)-3)+(6+8)") == 23
assert sol.calculate("-2+ 1") == -1
assert sol.calculate("-(2+3)") == -5
assert sol.calculate("2147483647") == 2147483647

print("All test cases passed successfully.")
