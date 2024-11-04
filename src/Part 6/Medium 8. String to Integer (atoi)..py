"""
Converts a string to a 32-bit signed integer, simulating the C/C++ atoi function.

This module defines a class Solution that contains a method for converting a
string into a 32-bit signed integer, handling leading whitespace, signs, and
non-digit characters as specified. The method also ensures that the output is
clamped within the 32-bit integer range.
"""

# Date of Last Practice: Dec 31, 2023 -> Feb 18, 2024 -> Nov 3, 2024
#
# Time Complexity: O(N), where N is the length of the string s.
#                  This is because we're iterating through the string at most once,
#                  performing constant-time checks and calculations at each step.
#
# Space Complexity: O(1), as we only use constant extra space, including index,
#                   s_length, max_int_32, min_int_32, and result.


class Solution:
    """Implements the myAtoi method for string-to-integer conversion."""

    def myAtoi(self, s: str) -> int:
        """
        Convert a string to a 32-bit signed integer.

        Args:
            s (str): Input string representing the number to be converted.

        Returns:
            int: Converted integer clamped to 32-bit signed integer range.
        """
        int_max = 2**31 - 1
        int_min = -(2**31)

        # Step 1: Initialize variables
        index = 0
        s_length = len(s)
        result = 0
        is_negative = False

        # Step 2: Skip leading whitespaces
        while index < s_length and s[index] == " ":
            index += 1

        # Step 3: Check if the next character is a sign
        if index < s_length and (s[index] == "-" or s[index] == "+"):
            is_negative = s[index] == "-"
            index += 1

        # Step 4: Convert subsequent digits to an integer
        while index < s_length and s[index].isdigit():
            digit = int(s[index])

            # Step 5: Handle potential overflow by checking result bounds
            if (result > int_max // 10) or (
                result == int_max // 10 and digit > int_max % 10
            ):
                return int_min if is_negative else int_max

            result = result * 10 + digit
            index += 1

        return -result if is_negative else result


def main():
    """
    Demonstrate the usage of the Solution class.

    This function initializes an instance of the Solution class and runs
    test cases to verify the correctness of the myAtoi method.
    """
    solution = Solution()

    # Test cases with assertions
    assert solution.myAtoi("42") == 42
    assert solution.myAtoi("   -42") == -42
    assert solution.myAtoi("4193 with words") == 4193
    assert solution.myAtoi("words and 987") == 0  # Starts with non-digit characters
    assert solution.myAtoi("-91283472332") == -2147483648  # Clamped to int_min
    assert solution.myAtoi("21474836460") == 2147483647  # Clamped to int_max
    assert solution.myAtoi("+1") == 1  # Positive number with sign

    print("All test cases passed!")


if __name__ == "__main__":
    main()
