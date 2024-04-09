# Date of Last Practice: Dec 30, 2023 -> Feb 18, 2024
#
# Time Complexity: O(N^2), where N is the length of the string.
#                  First, we iterate each character in the string, which is O(N).
#                  Second, for each character, we potentially expand in both directions.
#                  In the worst case, this expansion can be N/2 times or O(N).
#                  Therefore, O(N * N / 2) = O(N^2).
#
#                  The Manacher's algorithm can reduce the time to O(N) (yet space is O(N)).
#                  However, for most practical purposes, especially in coding interviews or
#                  unless dealing with extremely long strings, the "expand around center" method
#                  is often sufficient due to its simpler implementation and decent efficiency.
#
# Space Complexity: O(1), as we only use constant extra space.


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        def expand_around_center(left, right):
            while left >= 0 and right <= len(s) - 1 and s[left] == s[right]:
                left -= 1
                right += 1
            return right - left - 1

        start, end = 0, 0
        for index in range(len(s)):
            len_1 = expand_around_center(index, index)
            len_2 = expand_around_center(index, index + 1)
            max_len = max(len_1, len_2)
            if max_len > (end - start):
                start = index - (max_len - 1) // 2
                end = index + max_len // 2

        return s[start : end + 1]


# Test cases
sol = Solution()
print(sol.longestPalindrome("babad"))  # Output: "bab" or "aba"
print(sol.longestPalindrome("cbbd"))  # Output: "bb"
