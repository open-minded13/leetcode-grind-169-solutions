# Date of Last Practice: Mar 7, 2024
#
# Time Complexity: O(N+M), where N is the length of word and M is the length of abbr.
#
# Space Complexity: O(1). The solution uses constant extra space, i.e.,
#                   variables for pointers and counters (word_ptr, abbr_ptr, counter),
#                   regardless of the input size.


class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        word_ptr = 0
        abbr_ptr = 0

        while word_ptr < len(word) and abbr_ptr < len(abbr):
            if abbr[abbr_ptr].isdigit():
                if abbr[abbr_ptr] == "0":
                    return False

                counter = 0
                while abbr_ptr < len(abbr) and abbr[abbr_ptr].isdigit():
                    counter *= 10
                    counter += int(abbr[abbr_ptr])
                    if counter > len(word):
                        return False
                    abbr_ptr += 1

                while counter > 0:
                    word_ptr += 1
                    counter -= 1
            else:
                if abbr[abbr_ptr] != word[word_ptr]:
                    return False
                abbr_ptr += 1
                word_ptr += 1

        if word_ptr == len(word) and abbr_ptr == len(abbr):
            return True
        return False


# Test cases
sol = Solution()

assert sol.validWordAbbreviation("internationalization", "i12iz4n") == True
assert sol.validWordAbbreviation("apple", "a2e") == False
assert sol.validWordAbbreviation("substitution", "s10n") == True
assert (
    sol.validWordAbbreviation("substitution", "s55n") == False
)  # Invalid because of adjacent substrings
assert (
    sol.validWordAbbreviation("substitution", "s010n") == False
)  # Invalid because of leading zero
assert sol.validWordAbbreviation("substitution", "12") == True

# Print a message to indicate all tests passed
print("All tests passed!")
