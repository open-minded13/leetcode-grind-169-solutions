import sys
from collections import Counter, defaultdict
from typing import List
from functools import lru_cache

# Date of Last Practice: Mar 18, 2024
#
# Time Complexity: O(N⋅2^T), where N is the number of stickers and
#                  T is the length of the target string.
#
#   1) Preprocessing Stickers: The algorithm preprocesses the list of stickers
#       by filtering out those not sharing any characters with the target and
#       converting the remaining ones into Counter objects.
#       This operation has a time complexity of O(N*M),
#       where N is the number of stickers and M is the maximum length of a sticker,
#       due to the iteration and set intersection operations.
#
#   2) DFS Calls: The DFS function is memoized, which means each unique state of
#       the remaining target string will be computed exactly once.
#       The number of unique states can be up to 2^T in the worst case,
#       where T is the length of the target string,
#       representing different combinations of characters remaining.
#
#   3) Within Each DFS Call: For each call, the algorithm iterates over each preprocessed sticker,
#       and for each sticker, it may construct a new target state by subtracting
#       the Counter of the sticker from the Counter of the remaining target.
#       The subtraction and construction of the new target state are linear in
#       the size of the target, leading to O(T) complexity for this operation.
#
#   4) Considering the recursion and the operations within each call,
#       the time complexity can be difficult to directly quantify due to the combinatorial nature of
#       the problem and the impact of memoization. However, it can be broadly described as O(N⋅2^T)
#       under the assumption that each DFS call could potentially iterate over all stickers
#       and perform operations linear in the size of the target.
#
# Space Complexity: O(2^T+T+N*M), where N is the number of stickers,
#                   T is the length of the target string, and
#                   M is the maximum length of a sticker.
#
#   1) Memoization Cache: The space complexity is primarily determined by the size of the
#       memoization cache, which stores results for different states of the remaining target string.
#       In the worst case, this could be up to 2^T unique states.
#
#   2) Call Stack: The depth of the DFS call stack can go up to T in the worst case.
#
#   3) Preprocessed Stickers: Storing the preprocessed stickers as Counter objects need O(N*M).


class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:

        # Preprocess stickers: Keep only those stickers that have characters
        # in common with the target and convert them to Counter objects for easy manipulation
        preprocessed_stickers = [
            Counter(sticker) for sticker in stickers if set(sticker) & set(target)
        ]

        # Memoized DFS to minimize the number of stickers required
        @lru_cache(None)
        def dfs(remaining_target):
            # Base case: if no characters are left in the target, no stickers are needed
            if not remaining_target:
                return 0

            # Count characters in the remaining target
            remaining_count = Counter(remaining_target)

            # Find the character that is least frequent in the remaining target
            # This helps prioritize stickers that contain this character
            min_char = min(remaining_count, key=lambda char: remaining_count[char])

            # Initialize the result as infinity to find the minimum number of stickers
            min_stickers_needed = float("inf")

            # Iterate over each preprocessed sticker counter
            for sticker_count in preprocessed_stickers:
                # Skip this sticker if it doesn't contain the minimum required character
                if sticker_count[min_char] == 0:
                    continue

                # Construct the next target by removing characters covered by the current sticker
                next_target = "".join((remaining_count - sticker_count).elements())

                # Recurse with the new target, update the result if a new minimum is found
                next_result = dfs(next_target)

                if next_result != -1:
                    min_stickers_needed = min(min_stickers_needed, 1 + next_result)

            # If no solution was found, return -1, otherwise return the minimum stickers needed
            return -1 if min_stickers_needed == float("inf") else min_stickers_needed

        # Solve the problem
        return dfs(target)


class TimeLimitedExceededSolution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        sticker_to_letter_count = {}
        for sticker in stickers:
            sticker_to_letter_count[sticker] = Counter(sticker)

        target_letter_count = defaultdict(int)
        for char in target:
            target_letter_count[char] += 1

        letter_to_stickers = defaultdict(list)
        for char in target_letter_count.keys():
            for sticker, sticker_dict in sticker_to_letter_count.items():
                if char in sticker_dict:
                    letter_to_stickers[char].append(sticker)

            if char not in letter_to_stickers:
                return -1

        self.min_stickers = sys.maxsize
        cur_letter_counter = defaultdict(int)

        def _is_A_greater_or_equal_than_B(A, B):
            for key, value in B.items():
                if key not in A or A[key] < value:
                    return False
            return True

        def _backtracking(index, stickers):
            if _is_A_greater_or_equal_than_B(cur_letter_counter, target_letter_count):
                self.min_stickers = min(stickers, self.min_stickers)
                return

            if index > len(target) - 1:
                return

            char = target[index]
            if cur_letter_counter[char] >= target_letter_count[char]:
                _backtracking(index + 1, stickers)
                return

            for sticker in letter_to_stickers[char]:
                for letter, count in sticker_to_letter_count[sticker].items():
                    if letter in target_letter_count:
                        cur_letter_counter[letter] += count
                _backtracking(index + 1, stickers + 1)
                for letter, count in sticker_to_letter_count[sticker].items():
                    if letter in target_letter_count:
                        cur_letter_counter[letter] -= count

        _backtracking(0, 0)
        return self.min_stickers if self.min_stickers != sys.maxsize else -1


# Create an instance of the solution
solution = Solution()

# Test cases
# Example 1: Basic scenario with a direct solution
stickers = ["with", "example", "science"]
target = "thehat"
assert solution.minStickers(stickers, target) == 3, "Test case 1 failed"

# Example 2: Scenario where it's impossible to form the target
stickers = ["notice", "possible"]
target = "basicbasic"
assert solution.minStickers(stickers, target) == -1, "Test case 2 failed"

# Additional Test Case: Requires optimal selection of stickers
stickers = ["these", "guess", "about", "garden", "him"]
target = "atomher"
assert solution.minStickers(stickers, target) == 3, "Test case 3 failed"

print("All test cases passed successfully.")
