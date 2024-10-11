# Date of Last Practice: Dec 31, 2023 -> Feb 18, 2024
#
# Time Complexity: O(N), where N is the length of the string s.
#                  This is because we're iterating through the string at most once,
#                  performing constant-time checks and calculations at each step.
#
# Space Complexity: O(1), as we only use constant extra space, including
#                   index, s_length, max_int_32, min_int_32, and result.


class Solution:
    def myAtoi(self, s: str) -> int:
        # Step 1: Skip leading whitespaces
        index = 0
        s_length = len(s)
        while index < s_length and s[index] == " ":
            index += 1

        # Step 2: Check if the next character is '-' or '+'
        is_negative = False
        if index < s_length and (s[index] == "+" or s[index] == "-"):
            if s[index] == "-":
                is_negative = True
            index += 1

        # Step 3: Read in the next characters until a non-digit character
        max_int_32 = 2**31 - 1
        min_int_32 = -(2**31)
        result = 0
        while index < s_length and s[index].isdigit():
            digit = int(s[index])
            if result > max_int_32 // 10 or (
                result == max_int_32 // 10 and digit > max_int_32 % 10
            ):
                return min_int_32 if is_negative else max_int_32
            result = result * 10 + digit
            index += 1

        return -result if is_negative else result


class First_Solution:
    def myAtoi(self, s: str) -> int:
        if not s:
            return 0

        index = 0
        is_negative = False
        for i, char in enumerate(s):
            if char == " ":
                continue
            if char == "+" or char == "-":
                is_negative = True if char == "-" else False
                if i + 1 < len(s):
                    index = i + 1
                else:
                    return 0
                if not s[index].isdigit():
                    return 0
                break
            elif char.isdigit():
                index = i
                break
            else:
                return 0

        max_int_32 = 2**31 - 1
        min_int_32 = -(2**31)
        result = 0
        for i in range(index, len(s)):
            if not s[i].isdigit():
                break
            result = result * 10 + int(s[i])
            if is_negative:
                if -result < min_int_32:
                    return min_int_32
            else:
                if result > max_int_32:
                    return max_int_32

        return -result if is_negative else result


# Test cases
sol = Solution()
print(sol.myAtoi("42"))  # Expected output: 42
print(sol.myAtoi("   -42"))  # Expected output: -42
print(sol.myAtoi("4193 with words"))  # Expected output: 4193
print(
    sol.myAtoi("words and 987")
)  # Expected output: 0 (since it starts with non-whitespace characters that are non-digits)
print(sol.myAtoi("-91283472332"))  # Expected output: -2147483648 (clamped to INT_MIN)
print(sol.myAtoi("+-2"))  # Expected output: 0
