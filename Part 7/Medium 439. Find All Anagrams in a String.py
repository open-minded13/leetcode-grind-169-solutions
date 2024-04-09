from typing import List

# Date of Last Practice: Jan 14, 2024 -> Feb 26, 2024
#
# Time Complexity: O(N), where N is the length of s.
#                  We use a fixed-sized sliding window and hash tables.
#                  When we slide the window over s, we update one character enters,
#                  and another character leaves to s_count.
#                  This method allows us to visit each element of s in constant time (at most 2).
#
# Space Complexity: O(1), as the size of these arrays does not depend on the input size
#                   but rather on a constant (the number of lowercase letters in the alphabet = 26).


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []

        s_count, p_count = [0] * 26, [0] * 26
        for char in p:
            p_count[ord(char) - ord("a")] += 1

        left = 0
        result = []
        for right in range(len(s)):
            s_count[ord(s[right]) - ord("a")] += 1

            if right - left + 1 == len(p):
                if s_count == p_count:
                    result.append(left)
                s_count[ord(s[left]) - ord("a")] -= 1
                left += 1

        return result


class First_Solution:
    # Time Complexity: O(N*M), where N is the length of s and M is the length of p.
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []
        if len(s) == 1:
            if s[0] == p[0]:
                return [0]
            else:
                return []
        output = []
        if len(p) == 1:
            for index, char in enumerate(s):
                if char == p[0]:
                    output.append(index)
            return output

        p_dict, back_up = {}, {}
        for char in p:
            p_dict.setdefault(char, 0)
            p_dict[char] += 1
            back_up.setdefault(char, 0)
            back_up[char] += 1

        left = 0
        left_is_checked = False
        right = 1

        while right < len(s) and left < len(s):
            if not left_is_checked:
                if s[left] in p_dict:
                    if p_dict[s[left]] == 1:
                        del p_dict[s[left]]
                    else:
                        p_dict[s[left]] -= 1
                    left_is_checked = True
                else:
                    left += 1
                    continue
                right = left + 1
                if right >= len(s):
                    continue

            if s[right] in p_dict:
                if p_dict[s[right]] == 1:
                    del p_dict[s[right]]
                else:
                    p_dict[s[right]] -= 1
                if not p_dict:
                    output.append(left)
                if right - left < len(p) - 1:
                    right += 1
                else:
                    p_dict.setdefault(s[left], 0)
                    p_dict[s[left]] += 1
                    left += 1
                    right += 1
            else:
                left += 1
                left_is_checked = False
                p_dict = back_up.copy()

        return output


# Test Cases
sol = Solution()
assert sol.findAnagrams("cbaebabacd", "abc") == [0, 6]
assert sol.findAnagrams("abab", "ab") == [0, 1, 2]
assert sol.findAnagrams("a", "b") == []
assert sol.findAnagrams("baa", "aa") == [1]

print("All test cases passed!")
