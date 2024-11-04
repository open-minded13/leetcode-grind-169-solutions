"""Find the longest palindromic substring in a given string.

This module defines two approaches to identify the longest palindromic 
substring within a provided string. The primary approach uses explicit tracking
variables to minimize errors and make the logic more straightforward.

Typical usage example:

    sol = Solution()
    assert sol.longestPalindrome("babad") in {"bab", "aba"}
"""

# Date of Last Practice: Dec 30, 2023 -> Feb 18, 2024 -> Nov 3, 2024
#
# Time Complexity: O(N^2), where N is the length of the string.
#                  - We iterate each character in the string, which is O(N).
#                  - For each character, we potentially expand in both directions.
#                  - In the worst case, this expansion can be N/2 times or O(N).
#                  - Therefore, O(N * N / 2) = O(N^2).
#
#                  The Manacher's algorithm can reduce the time to O(N) (yet space
#                  is O(N)). However, for most practical purposes, especially in coding
#                  interviews or unless dealing with extremely long strings, the "expand
#                  around center" method is often sufficient due to its simpler
#                  implementation and decent efficiency.
#
# Space Complexity: O(1), as we only use constant extra space.


class Solution:
    """A solution to find the longest palindromic substring in a string."""

    def longestPalindrome(self, s: str) -> str:
        """Finds and returns the longest palindromic substring.

        This method uses explicit tracking variables (`max_length`, `final_left`,
        and `final_right`) to make index updates clear and reduce the risk of
        off-by-one errors. Expands around each character and each pair of
        characters as the center of a potential palindrome.

        Args:
            s (str): The input string to find the longest palindromic substring.

        Returns:
            str: The longest palindromic substring in `s`.
        """
        if not s:
            return ""

        max_length, final_left, final_right = 0, -1, -1

        def find_palindrome(left: int, right: int):
            """Expands around center to check palindrome length and update."""
            nonlocal max_length, final_left, final_right
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > max_length:
                    max_length = right - left + 1
                    final_left, final_right = left, right
                left -= 1
                right += 1

        for i in range(len(s)):
            # Step 1 - Expand around single character (odd length palindromes)
            find_palindrome(i, i)
            # Step 2 - Expand around two characters (even length palindromes)
            if i + 1 < len(s):
                find_palindrome(i, i + 1)

        # Step 3 - Return the longest palindrome substring found
        return s[final_left : final_right + 1]

    def longestPalindromeSimplified(self, s: str) -> str:
        """Alternative method for finding the longest palindromic substring.

        This method uses simpler start and end variables to track the longest
        palindromic substring, reducing the number of variables but potentially
        increasing the chance of index errors.

        Args:
            s (str): The input string to find the longest palindromic substring.

        Returns:
            str: The longest palindromic substring in `s`.
        """
        if not s:
            return ""

        def expand_around_center(left: int, right: int) -> int:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return right - left - 1

        start, end = 0, 0
        for index in range(len(s)):
            # Expand around single character (odd length palindromes)
            len_1 = expand_around_center(index, index)
            # Expand around two characters (even length palindromes)
            len_2 = expand_around_center(index, index + 1)
            max_len = max(len_1, len_2)
            if max_len > (end - start):
                start = index - (max_len - 1) // 2
                end = index + max_len // 2

        return s[start : end + 1]


# Test cases
def main():
    """Main function for running test cases."""
    sol = Solution()
    # Test primary method with assertions
    assert sol.longestPalindrome("babad") in {"bab", "aba"}, "Primary case 1 failed"
    assert sol.longestPalindrome("cbbd") == "bb", "Primary case 2 failed"
    assert sol.longestPalindrome("a") == "a", "Primary case 3 failed"
    assert sol.longestPalindrome("racecar") == "racecar", "Primary case 4 failed"
    assert sol.longestPalindrome("abcdefg") in {
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
    }, "Primary case 5 failed"

    # Test alternative simplified method
    assert sol.longestPalindromeSimplified("babad") in {
        "bab",
        "aba",
    }, "Simplified case 1 failed"
    assert sol.longestPalindromeSimplified("cbbd") == "bb", "Simplified case 2 failed"
    assert sol.longestPalindromeSimplified("a") == "a", "Simplified case 3 failed"
    assert (
        sol.longestPalindromeSimplified("racecar") == "racecar"
    ), "Simplified case 4 failed"
    assert sol.longestPalindromeSimplified("abcdefg") in {
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
    }, "Simplified case 5 failed"

    print("All test cases passed.")


if __name__ == "__main__":
    main()
