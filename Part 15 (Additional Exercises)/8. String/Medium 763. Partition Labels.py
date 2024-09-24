from typing import List

# Date of Last Practice: Mar 11, 2024
#
# Time Complexity: O(N), where N is the length of the input string s.
#                  The reason is that it iterates over the string twice—once to
#                  build the letter_dict and once to determine the partitions.
#                  Each of these operations takes O(N) time.
#
# Space Complexity: O(1), from a theoretical perspective,
#                   because the letter_dict map will contain at most 26 entries
#                   (for each letter of the English alphabet).
#                   Given the problem's nature, the maximum number of partitions
#                   (and hence, the maximum size of the result list) cannot exceed 26.


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # Step 1 - Create a mapping of each character to its last occurrence
        letter_dict = {}
        for index, char in enumerate(s):
            letter_dict[char] = index

        left, right = 0, 0
        result = []
        # Step 2 - Determine partitions based on the mapping
        for index, char in enumerate(s):
            cur_left = index
            cur_right = letter_dict[char]

            # Update the current partition's boundaries
            if left <= cur_left <= right or left <= cur_right <= right:
                left = min(left, cur_left)
                right = max(right, cur_right)
            else:
                # Step 3 - Finalize the current partition and start a new one
                result.append(right - left + 1)
                left, right = cur_left, cur_right

        # Step 4 - Add the last partition to the result
        result.append(right - left + 1)
        return result


# Test cases
sol = Solution()
assert sol.partitionLabels("ababcbacadefegdehijhklij") == [9, 7, 8]
assert sol.partitionLabels("eccbbbbdec") == [10]
assert sol.partitionLabels("abcdefghijk") == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
assert sol.partitionLabels("abcdahijkli") == [5, 1, 5]
assert sol.partitionLabels("abcdahabcda") == [11]

print("All test cases passed!")
