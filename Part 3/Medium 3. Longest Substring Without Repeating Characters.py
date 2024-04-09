# Date of Last Practice: Nov 6, 2023 -> Feb 3, 2024
#
# Time Complexity: O(N), where N is the length of the input string s.
#
# Space Complexity: O(min(N, M)), where n is the length of the input string s,
#                   and m is the size of the character set (number of distinct characters in the string).
#                   In the worst case, when all characters are distinct,
#                   the space complexity is O(n) because we store all characters in the recent_char_index.
#                   However, when the string contains a limited character set, the space complexity is limited to O(m).


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        recent_char_index = {}
        longest_substring = 0
        start = 0

        # Consider using enumerate instead of iterating with range and len.
        # for end in range(len(s)):
        #     if s[end] in recent_char_index and recent_char_index[s[end]] >= start:
        #         start = recent_char_index[s[end]]+1
        #     recent_char_index[s[end]] = end
        #     longest_substring = max(longest_substring, end-start+1)
        for end, char in enumerate(s):
            if char in recent_char_index and recent_char_index[char] >= start:
                start = recent_char_index[char] + 1
            recent_char_index[char] = end
            longest_substring = max(longest_substring, end - start + 1)

        return longest_substring


class First_Solution:
    # Time Complexity: O(N), where N is the length of the input string s.
    #                  We traverse the string once from left to right; however,
    #                  each character is processed at most TWICE (first insertion and then removal).
    #
    # Space Complexity: O(min(N, M)), where n is the length of the input string s,
    #                   and m is the size of the character set (number of distinct characters in the string).

    def lengthOfLongestSubstring(self, s: str) -> int:
        substring_length = 0
        max_substring_length = 0
        substring_dict = {}
        i = 0

        while i < len(s):
            if s[i] in substring_dict:
                max_substring_length = max(max_substring_length, substring_length)
                substring_length = 0
                i = substring_dict[s[i]] + 1
                substring_dict.clear()
            substring_dict[s[i]] = i
            substring_length += 1
            i += 1

        max_substring_length = max(max_substring_length, substring_length)
        return max_substring_length


# Test cases
solution = Solution()
print(solution.lengthOfLongestSubstring("abcabcbb"))  # Expected output: 3
print(solution.lengthOfLongestSubstring("bbbbb"))  # Expected output: 1
print(solution.lengthOfLongestSubstring("pwwkew"))  # Expected output: 3
print(solution.lengthOfLongestSubstring("dvdj"))  # Expected output: 3
