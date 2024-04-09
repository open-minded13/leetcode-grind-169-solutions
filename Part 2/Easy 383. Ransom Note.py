from collections import Counter

# Date of Last Practice: Oct 30, 2023 -> Feb 2, 2024
#
# Time Complexity: O(N+M), where N and M are the length of the ransomNote and magazine strings respectively.
#
# Space Complexity: O(N). In the worst case, as the letter_counter dictionary can store
#                         at most all distinct letters from the magazine string.


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letter_counter = {}

        # Count the occurrences of each letter in the magazine.
        for letter in magazine:
            if letter in letter_counter:
                letter_counter[letter] += 1
            else:
                letter_counter[letter] = 1

        # Check if you can construct the ransomNote.
        for letter in ransomNote:
            if letter in letter_counter:
                letter_counter[letter] -= 1
                if letter_counter[letter] < 0:
                    return False
            else:
                return False

        return True


class AnotherSolution1:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letter_counter = [0] * 26
        for letter in magazine:
            letter_counter[ord(letter) - ord("a")] += 1
        for letter in ransomNote:
            letter_counter[ord(letter) - ord("a")] -= 1
            if letter_counter[ord(letter) - ord("a")] < 0:
                return False
        return True


class AnotherSolution2(object):
    def canConstruct(self, ransomNote, magazine):
        # The Counter class takes an iterable (in this case, strings) as input and
        # returns a dictionary-like object where keys are elements from the iterable,
        # and values are their respective counts.
        #
        # For example,
        #   st1 = Counter(ransomNote = "aaabbc")
        #   st1 = {'a': 3, 'b': 2, 'c': 1}
        st1, st2 = Counter(ransomNote), Counter(magazine)

        # The & operator between two Counter objects returns a new Counter object that
        # contains the intersection of the elements from both counters.
        # In this context, st1 & st2 represents the letters common to
        # both ransomNote and magazine, and st1 is the Counter for ransomNote.
        if st1 & st2 == st1:
            return True
        return False


# Test cases
sol = Solution()
print(sol.canConstruct("a", "b"))  # False
print(sol.canConstruct("aa", "ab"))  # False
print(sol.canConstruct("aa", "aab"))  # True

sol = AnotherSolution1()
print(sol.canConstruct("a", "b"))  # False
print(sol.canConstruct("aa", "ab"))  # False
print(sol.canConstruct("aa", "aab"))  # True
