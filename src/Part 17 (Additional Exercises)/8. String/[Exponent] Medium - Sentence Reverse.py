"""
Reverse words in an array of characters.

The solution reverses the order of words in the input array
in place, with space characters separating the words.

Typical usage example:
    arr = ['p', 'e', 'r', 'f', 'e', 'c', 't', ' ',
           'm', 'a', 'k', 'e', 's', ' ',
           'p', 'r', 'a', 'c', 't', 'i', 'c', 'e']
    solution = Solution()
    reversed_arr = solution.reverse_words(arr)
"""

from typing import List

# Date of Last Practice: Oct 1, 2024
#
# Time Complexity: O(N), where N is the number of characters in the input array.
#                  The solution iterates over the array twice, once to reverse the
#                  entire array and once to reverse each word.
#
# Space Complexity: O(1), since the solution performs the operation in place without
#                   using any additional data structures.


class Solution:
    """Reverses words in a list of characters, separated by spaces."""

    def reverse_words(self, s: List[str]) -> List[str]:
        """
        Reverses the order of words in the given character array in place.

        Args:
            s: List of characters representing words separated by spaces.

        Returns:
            List of characters with words in reversed order.
        """

        def reverse_string(start: int, end: int) -> None:
            """Reverses a substring in place between the given indices."""
            while start < end:
                s[start], s[end] = s[end], s[start]  # Swap characters
                start += 1
                end -= 1

        n = len(s)

        # Step 1 - Reverse the entire character array
        reverse_string(0, n - 1)

        # Step 2 - Reverse each word in the reversed array
        start = 0
        while start < n:
            # Skip spaces to find the start of a word
            while start < n and s[start] == " ":
                start += 1
            end = start
            # Find the end of the current word
            while end < n and s[end] != " ":
                end += 1
            # Reverse the current word
            reverse_string(start, end - 1)
            start = end

        return s


def main():
    """Demonstrates the usage of the Solution class."""

    # Example 1
    arr = [
        "p",
        "e",
        "r",
        "f",
        "e",
        "c",
        "t",
        " ",
        "m",
        "a",
        "k",
        "e",
        "s",
        " ",
        "p",
        "r",
        "a",
        "c",
        "t",
        "i",
        "c",
        "e",
    ]
    solution = Solution()
    assert solution.reverse_words(arr) == [
        "p",
        "r",
        "a",
        "c",
        "t",
        "i",
        "c",
        "e",
        " ",
        "m",
        "a",
        "k",
        "e",
        "s",
        " ",
        "p",
        "e",
        "r",
        "f",
        "e",
        "c",
        "t",
    ]

    # Example 2 - Array with only one word
    arr = ["h", "e", "l", "l", "o"]
    assert solution.reverse_words(arr) == ["h", "e", "l", "l", "o"]

    # Example 3 - Array with spaces only
    arr = [" ", " ", " "]
    assert solution.reverse_words(arr) == [" ", " ", " "]

    # Example 4 - Empty array
    arr = []
    assert solution.reverse_words(arr) == []

    print("All test cases passed!")


if __name__ == "__main__":
    main()
