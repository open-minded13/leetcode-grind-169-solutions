# Date of Last Practice: Sep 2, 2023 -> Jan 27, 2024
#
# Time Complexity: O(N), where N is the length of the string.
#                  Overall, the time complexity is O(N) due to the linear operations for
#                  removing non-alphanumeric characters O(N), converting to lowercase O(N),
#                  and the loop O(N/2).
# Space Complexity: O(N), where N is the length of the string.
#                   This is due to the creation of the letters string.


import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Remove non-alphanumeric characters and convert to lowercase
        letters = re.sub(r"[^A-Za-z0-9]", "", s)
        letters = letters.lower()
        length = len(letters)

        # Check if the string is empty or consists of a single character (palindrome by definition)
        if length <= 1:
            return True

        # Define left and right ranges based on string length (odd or even)
        if length % 2 == 0:
            left_range = range(length // 2 - 1, -1, -1)
            right_range = range(length // 2, length)
        else:
            left_range = range(length // 2 - 1, -1, -1)
            right_range = range(length // 2 + 1, length)

        # Compare characters at corresponding positions in the ranges
        for left, right in zip(left_range, right_range):
            if letters[right] != letters[left]:
                return False

        return True


class AnotherSolution:
    def isPalindrome(self, s: str) -> bool:
        # This line of code first creates a list comprehension.
        # It iterates over each character c in the input string s.
        # For each character c, it checks if it is alphanumeric using the c.isalnum() method.
        # If c is alphanumeric, it converts it to lowercase using c.lower().
        # This line essentially creates a list s containing only alphanumeric characters
        # from the input string s, with all characters converted to lowercase.
        s = [c.lower() for c in s if c.isalnum()]

        # This line checks if the string s is a palindrome.
        # It uses a generator expression within the all() function.
        # range(len(s)//2) generates a sequence of indices from 0 to
        # half the length of the cleaned string s.
        #
        # For each index i, it checks if s[i] (the character at index i) is equal to
        # s[~i] (the character at the corresponding position from the end of the string).
        # The ~i notation represents the index from the end of the string.
        # So, s[~i] refers to the character at the same position
        # from the end as s[i] from the beginning.
        #
        # The all() function checks if all these character comparisons are True.
        # If all characters match in a pairwise manner from the beginning and
        # end of the string towards the middle, the string is considered a palindrome,
        # and the function returns True. Otherwise, it returns False.
        return all(s[i] == s[~i] for i in range(len(s) // 2))


# Test cases
solution = Solution()
print(solution.isPalindrome("A man, a plan, a canal: Panama"))  # True
print(solution.isPalindrome("race a car"))  # False
print(solution.isPalindrome("abcba"))  # True
print(solution.isPalindrome("12321"))  # True
print(solution.isPalindrome("Able was I, ere I saw Elba"))  # True
print(solution.isPalindrome("Palindrome"))  # False
