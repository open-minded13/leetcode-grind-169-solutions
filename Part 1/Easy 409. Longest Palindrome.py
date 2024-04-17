from collections import Counter

# Date of Last Practice: Oct 29, 2023 -> Feb 2, 2024
#
# Time Complexity: O(N), where N is the length of the s string.
#
# Space Complexity: O(1). For the Counter object, the solution uses 54 additional spaces
#                         (to create a Counter's dictionary-like object)
#                         because the number of distinct lowercase and uppercase letters.
#                         Other variables like single_letter_exists and
#                         longest_palindrome_length require 2 space.
#                         Overall, O(26) + O(2) can be considered as O(1).


class Solution:
    def longestPalindrome(self, s: str) -> int:
        letter_counter = Counter(s)
        single_letter_exists = 0
        longest_palindrome_length = 0
        # for key, value in letter_counter.items():
        for value in letter_counter.values():
            if value % 2 == 1:
                single_letter_exists = 1
            longest_palindrome_length += (value // 2) * 2
        return longest_palindrome_length + single_letter_exists


# Test cases
def test_longestPalindrome():
    solution = Solution()
    assert (
        solution.longestPalindrome("abccccdd") == 7
    )  # "dccaccd" is the longest palindrome
    assert solution.longestPalindrome("aabb") == 4  # "abba" is the longest palindrome
    assert (
        solution.longestPalindrome("abc") == 1
    )  # "a", "b", and "c" are all palindromes of length 1
    assert solution.longestPalindrome("ccc") == 3  # "ccc" is the longest palindrome
    assert solution.longestPalindrome("bb") == 2  # "bb" is the longest palindrome
    print("All test cases passed.")


if __name__ == "__main__":
    test_longestPalindrome()
