"""
Find the minimum substring of a string containing all characters of another string.

This module defines a class `Solution` with a method to find the minimum window 
substring of a string `s` that contains all characters (including duplicates) 
of a string `t`. If no such substring exists, it returns an empty string.

Typical usage example:

    solution = Solution()
    result = solution.minWindow(s, t)
"""

from collections import defaultdict
import sys

# Date of Last Practice: Jan 28, 2024 -> Mar 3, 2024 -> Oct 8, 2024
#
# Time Complexity: O(N), where N is the length of s.
#                  The `right` pointer traverses the string s once.
#                  The `left` pointer can also traverse the string s once.
#                  Therefore, the time complexity is O(N) + O(N) = O(N).
#
# Space Complexity: O(M), where M is the number of unique characters in t.
#                   The space complexity is O(M) because the dictionary t_dict
#                   can contain at most M unique characters from the string t.


class Solution:
    """
    Finds the minimum window substring in `s` that contains all characters of `t`.
    """

    def minWindow(self, s: str, t: str) -> str:
        """
        Returns the minimum window substring of `s` that contains all characters in `t`.

        Args:
            s: The input string where we need to find the substring.
            t: The string containing the characters to be found in the substring.

        Returns:
            The smallest substring of `s` containing all characters from `t`,
            or an empty string if no such substring exists.
        """
        if not t or not s or len(t) > len(s):
            return ""

        # Step 1: Initialize character count dictionary for `t`
        t_dict = defaultdict(int)
        for char in t:
            t_dict[char] += 1

        # Step 2: Initialize sliding window pointers and variables
        min_length = sys.maxsize
        min_left, min_right = 0, 0
        substring_dict = defaultdict(int)
        left = 0
        counter = 0  # Tracks how many characters have been matched

        # Step 3: Slide the `right` pointer through the string `s`
        for right, char in enumerate(s):
            # Step 4: Expand the window by including character at `right`
            if char in t_dict:
                substring_dict[char] += 1
                if substring_dict[char] == t_dict[char]:
                    counter += 1

            # Step 5: Contract the window if all characters from `t` are matched
            while counter == len(t_dict):
                # Step 6: Update the minimum window if current window is smaller
                if (right - left + 1) < min_length:
                    min_left, min_right = left, right
                    min_length = right - left + 1

                # Step 7: Shrink the window by moving the `left` pointer
                if s[left] in t_dict:
                    substring_dict[s[left]] -= 1
                    if substring_dict[s[left]] < t_dict[s[left]]:
                        counter -= 1
                left += 1

        # Step 8: Return the result based on the smallest window found
        return s[min_left : min_right + 1] if min_length != sys.maxsize else ""


# Test cases
sol = Solution()

assert sol.minWindow("ADOBECODEBANC", "ABC") == "BANC"
assert sol.minWindow("a", "a") == "a"
assert sol.minWindow("a", "aa") == ""
assert sol.minWindow("aa", "aa") == "aa"
assert sol.minWindow("this is a test string", "tist") == "t stri"
assert sol.minWindow("geeksforgeeks", "ork") == "ksfor"
assert sol.minWindow("ab", "b") == "b"
assert sol.minWindow("bba", "ab") == "ba"
assert sol.minWindow("abbaac", "aba") == "baa"
assert sol.minWindow("abbaac", "abc") == "baac"
assert sol.minWindow("abbaac", "aac") == "aac"
assert sol.minWindow("a", "b") == ""
assert sol.minWindow("", "a") == ""
assert sol.minWindow("abcdef", "z") == ""
assert sol.minWindow("abcdef", "") == ""
assert sol.minWindow("abdecfbdbebbcabbedcabfaadbefa", "abbc") == "bbca"

print("All test cases passed!")
