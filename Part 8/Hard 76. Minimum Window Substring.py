# Date of Last Practice: Jan 28, 2024 -> Mar 3, 2024
#
# Time Complexity: O(M+N), where M is the length of s, and N is the length of t.
#                  Creating t_dict from string t using Counter(t) takes O(N) time.
#                  The sliding window approach checks each element in s at most twice.
#                  Therefore O(2*M+N) = O(M+N).
#
# Space Complexity: O(N), where N is the length of t.
#                   The storage of t_dict and char_counter,
#                   which contain at most all unique characters of t.

from collections import Counter, defaultdict
import sys


class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if not t:
            return ""

        s_counter = defaultdict(int)
        t_counter = defaultdict(int)
        num_of_char = len(t)
        counter = 0

        for char in t:
            t_counter[char] += 1

        left, right = 0, 0
        min_substring_len = sys.maxsize
        output = ""
        while left <= right < len(s):
            if s[right] in t_counter:
                s_counter[s[right]] += 1
                if s_counter[s[right]] <= t_counter[s[right]]:
                    counter += 1

            if counter == num_of_char:
                while counter == num_of_char:
                    if s[left] in t_counter:
                        s_counter[s[left]] -= 1
                        if s_counter[s[left]] < t_counter[s[left]]:
                            counter -= 1
                    left += 1

                len_of_substring = right - (left - 1) + 1
                if len_of_substring < min_substring_len:
                    min_substring_len = len_of_substring
                    output = s[left - 1 : right + 1]

            right += 1

        return output


class SecondSolution:
    """This solution has the same time and space complexity."""

    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        t_dict = Counter(t)
        left = 0
        right = 0
        min_window_length = sys.maxsize
        ans = [0, len(s)]
        char_counter = {char: 0 for char in set(t)}
        formed = 0

        while right < len(s):
            if s[right] in t_dict:
                char_counter[s[right]] += 1
                if char_counter[s[right]] == t_dict[s[right]]:
                    formed += 1

                while left < len(s) and formed == len(t_dict):
                    if right - left < ans[1] - ans[0]:
                        ans[0] = left
                        ans[1] = right
                        min_window_length = right - left
                    if s[left] in t_dict:
                        char_counter[s[left]] -= 1
                        if char_counter[s[left]] < t_dict[s[left]]:
                            formed -= 1
                    left += 1
            right += 1

        return s[ans[0] : ans[1] + 1] if min_window_length != sys.maxsize else ""


class FirstSolution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        if len(t) == 1:
            if t[0] in s:
                return t

        t_dict = {}
        for char in t:
            t_dict.setdefault(char, 0)
            t_dict[char] += 1

        left = 0
        for i in range(len(s)):
            if s[i] in t_dict:
                left = i
                break
            elif i == len(s) - 1:
                return ""
        right = left + 1
        cur_min_left = left
        cur_min_right = right
        cur_min_window = sys.maxsize
        checking_dict = {}
        checking_dict[s[left]] = 1
        prev_right = -1

        def helper():
            for key, value in t_dict.items():
                if key not in checking_dict or checking_dict[key] < value:
                    return False
            return True

        while left < right < len(s):
            if s[right] in t_dict:
                checking_dict.setdefault(s[right], 0)
                checking_dict[s[right]] += 1

                if helper():
                    if (right - left) < cur_min_window:
                        cur_min_left = left
                        cur_min_right = right
                        cur_min_window = right - left
                    checking_dict[s[left]] -= 1

                    while left < len(s) - 1:
                        left += 1
                        if s[left] in t_dict:
                            if helper():
                                checking_dict[s[left]] -= 1
                                if (right - left) < cur_min_window:
                                    cur_min_left = left
                                    cur_min_right = right
                                    cur_min_window = right - left
                                continue
                            break
                    right = max(left + 1, right + 1)
                    continue
            right += 1

        if cur_min_window == sys.maxsize:
            return ""
        return s[cur_min_left : cur_min_right + 1]


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
