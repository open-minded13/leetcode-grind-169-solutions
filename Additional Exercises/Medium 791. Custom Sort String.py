from collections import Counter

# Date of Last Practice: Mar 13, 2024
#
# Time Complexity: O(N+M), where N is the length of the input string s, and M is the length of order.
#                  The first loop iterates over each character in s, which is O(N).
#                  The second loop iterates over each character in order, which is O(m).
#                  Since these steps are sequential and not nested,
#                  the overall time complexity is O(N+M).
#
# Space Complexity: O(1) (or O(N) if considering the final result list).
#                   This uses additional space proportional to
#                   the number of unique characters in s,
#                   which is at most O(26) if all characters are unique.


class Solution:
    def customSortString(self, order: str, s: str) -> str:
        # Step 1: Count occurrences of each character in s
        letter_count = Counter(s)

        result = []

        # Step 2: Append characters in the order of 'order'
        for char in order:
            result.append(char * letter_count[char])
            del letter_count[char]

        # Step 3: Append characters not in 'order'
        for char in letter_count.keys():
            result.append(char * letter_count[char])

        return "".join(result)


# Test cases
sol = Solution()
assert sol.customSortString("cba", "abcd") == "cbad"
assert sol.customSortString("bcafg", "abcd") == "bcad"
# Testing with characters not in 'order'
assert sol.customSortString("xyz", "abcabc") == "aabbcc"
# Testing with repeating characters in 's'
assert sol.customSortString("cba", "aabbccdd") == "ccbbaadd"

print("All tests passed!")
