# Date of Last Practice: Oct 15, 2023 -> Jan 29, 2024
#
# Time Complexity: O(N), where n is the length of the input strings s and t.
#                  The solution iterates over both strings once to count the frequency of characters and
#                  then checks if the character frequencies match.
# Space Complexity: O(1) because the s_letter_count list always has a fixed size of 26,
#                   representing the lowercase English letters.


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        # Tips:
        # (1) [0] * 26 = [0, 0, ..., 0].
        # (2) [[0] for _ in range(26)] = [[0], [0], ..., [0]]
        s_letter_count = [0] * 26

        # In Python, we should use ord("a") to get its Unicode number instead of int("a").
        for char in s:
            s_letter_count[ord(char) - ord("a")] += 1
        for char in t:
            s_letter_count[ord(char) - ord("a")] -= 1
            if s_letter_count[ord(char) - ord("a")] < 0:
                return False
        return True


class First_Solution:
    # Time Complexity: O(N * log N), where n is the length of the input strings s and t.
    #                  The dominant factor is the sorting of both strings,
    #                  which typically has a time complexity of O(n log n).
    # Space Complexity: O(N) because the sorted versions of the input strings s and t
    #                   are stored in separate variables, and each can potentially have a length of n.

    def isAnagram(self, s: str, t: str) -> bool:
        # Sort the input strings and compare them.
        # `sorted_s = sorted(s)` is equal to `sorted_s = ''.join(sorted(s))` here.
        sorted_s = "".join(sorted(s))
        sorted_t = "".join(sorted(t))

        return sorted_s == sorted_t


# Test cases
if __name__ == "__main__":
    solution = Solution()
    assert solution.isAnagram("anagram", "nagaram") == True
    assert solution.isAnagram("rat", "car") == False
    assert solution.isAnagram("hello", "world") == False
    assert solution.isAnagram("listen", "silent") == True
    assert solution.isAnagram("abcdef", "fedcba") == True
    assert solution.isAnagram("abc", "abcd") == False
    print("All test cases passed!")
