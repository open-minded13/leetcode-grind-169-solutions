"""Regular Expression Matching.

Given a string s and a string p, the function isMatch(s, p) determines if s matches p.
s is a string consisting of lowercase English letters.
p is a pattern string containing lowercase English letters, '.', and '*'.
'.' matches any single character.
'*' matches zero or more of the preceding element.

Example 1:
    Input: s = "aa", p = "a"
    Output: False
    Explanation: "a" does not match the entire string "aa".

Example 2:
    Input: s = "aa", p = "a*"
    Output: True
    Explanation: '*' means zero or more of the preceding element, 'a'. 
                 Therefore, by repeating 'a' once, it becomes "aa".

Example 3:
    Input: s = "abc", p = ".*"
    Output: True
    Explanation: ".*" means "zero or more (*) of any character (.)".
"""

# Date of Last Practice: Oct 8, 2024
#
# Time Compleixty: O(M * N), where M is the length of the string s and N is the length
#                  of the pattern p. The function dp(i, j) is called at most once for
#                  each pair of (i, j) indices. Since there are M * N possible pairs,
#                  the time complexity is O(M * N).
#
# Space Complexity: O(M * N), where M is the length of the string s and N is the length
#                   of the pattern p. The memoization cache can store at most M * N
#                   entries. Therefore, the space complexity is O(M * N).


class Solution:
    """Implements regular expression matching with support for '.' and '*'."""

    def isMatch(self, s: str, p: str) -> bool:
        """Returns True if the string s matches the pattern p.

        Args:
            s: The input string consisting of lowercase English letters.
            p: The pattern string containing lowercase English letters, '.', and '*'.

        Returns:
            True if s matches p according to the regular expression rules,
            False otherwise.
        """
        # Memoization cache to avoid redundant computations.
        memo = {}

        def dp(i: int, j: int) -> bool:
            """Recursively checks if s[i:] matches p[j:] using dynamic programming.

            Args:
                i: Current index in s.
                j: Current index in p.

            Returns:
                True if s[i:] matches p[j:], False otherwise.
            """
            # If the result for this state has already been computed, return it.
            if (i, j) in memo:
                return memo[(i, j)]

            # Base case: if we've reached the end of the pattern, check if we're
            # also at the end of the string.
            if j == len(p):
                return i == len(s)

            # Check if the current characters match.
            first_match = i < len(s) and p[j] in {s[i], "."}

            # Handle the '*' wildcard.
            if j + 1 < len(p) and p[j + 1] == "*":
                # Either skip the '*' and its preceding character, or use the '*' to
                # consume one matching character.
                memo[(i, j)] = dp(i, j + 2) or (first_match and dp(i + 1, j))
            else:
                # Regular case: proceed to the next character if there's a match.
                memo[(i, j)] = first_match and dp(i + 1, j + 1)

            return memo[(i, j)]

        # Start matching from the beginning of both strings.
        return dp(0, 0)


def main():
    """Runs sample test cases for the Solution class."""
    solution = Solution()

    # Test cases
    assert solution.isMatch("aa", "a") is False, "Test case 1 failed"
    assert solution.isMatch("aa", "a*") is True, "Test case 2 failed"
    assert solution.isMatch("ab", ".*") is True, "Test case 3 failed"
    assert solution.isMatch("aab", "c*a*b") is True, "Test case 4 failed"
    assert solution.isMatch("mississippi", "mis*is*p*.") is False, "Test case 5 failed"
    assert solution.isMatch("bbbba", ".*a*a") is True, "Test case 6 failed"
    assert solution.isMatch("ab", ".*c") is False, "Test case 7 failed"
    assert solution.isMatch("", "c*c*") is True, "Test case 8 failed"
    assert solution.isMatch("a", "ab*") is True, "Test case 9 failed"
    assert solution.isMatch("a", ".*..a*") is False, "Test case 10 failed"
    assert solution.isMatch("aaa", "a*a") is True, "Test case 11 failed"

    print("All test cases passed.")


if __name__ == "__main__":
    main()
