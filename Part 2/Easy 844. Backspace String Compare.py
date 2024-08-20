"""
A module to compare two strings considering backspace characters.

This module contains a Solution class with a method to compare two strings
when '#' is used as a backspace. The comparison is done in O(n) time
and O(1) space complexity.

Typical usage example:

    solution = Solution()
    assert solution.backspaceCompare("ab#c", "ad#c") == True
"""

# Date of Last Practice: Aug 20, 2024
#
# Time Complexity: O(N + M), where N and M are the lengths of the input strings.
#                  The reason is that we process each string once to remove backspaces.
#
# Space Complexity: O(1), since we use only a constant amount of extra space.


class Solution:
    """A class to solve the backspace string comparison problem."""

    def backspaceCompare(self, s: str, t: str) -> bool:
        """
        Compare two strings considering '#' as a backspace character.

        This function compares two input strings after processing all
        backspace characters. The comparison is done using a two-pointer
        technique, ensuring O(n) time complexity and O(1) space complexity.

        Args:
            s (str): The first string to compare.
            t (str): The second string to compare.

        Returns:
            bool: True if the processed strings are equal, otherwise False.
        """

        def next_valid_char(index: int, string: str) -> int:
            """
            Find the next valid character index after considering backspaces.

            This helper function processes the string backwards, skipping
            over characters that should be removed due to preceding '#'
            characters.

            Args:
                index (int): The current index in the string.
                string (str): The string being processed.

            Returns:
                int: The index of the next valid character, or -1 if none exist.
            """
            skip = 0
            while index >= 0:
                if string[index] == "#":
                    skip += 1
                elif skip > 0:
                    skip -= 1
                else:
                    return index
                index -= 1
            return -1

        # Initialize pointers to the end of both strings
        s_index, t_index = len(s) - 1, len(t) - 1

        # Compare the strings from the end to the beginning
        while s_index >= 0 or t_index >= 0:
            s_index = next_valid_char(s_index, s)
            t_index = next_valid_char(t_index, t)

            # Compare the characters at the current valid indices
            if s_index >= 0 and t_index >= 0 and s[s_index] != t[t_index]:
                return False

            # If one string is exhausted before the other
            if (s_index < 0) != (t_index < 0):
                return False

            # Move to the previous character in both strings
            s_index -= 1
            t_index -= 1

        return True


def main():
    """Main function to run test cases for the Solution class."""
    solution = Solution()

    # Test case 1: Both strings become "ac"
    assert solution.backspaceCompare("ab#c", "ad#c") is True, "Test case 1 failed"

    # Test case 2: Both strings become empty
    assert solution.backspaceCompare("ab##", "c#d#") is True, "Test case 2 failed"

    # Test case 3: One string becomes "c", the other "b"
    assert solution.backspaceCompare("a#c", "b") is False, "Test case 3 failed"

    # Additional test cases can be added here
    print("All test cases passed!")


if __name__ == "__main__":
    main()
