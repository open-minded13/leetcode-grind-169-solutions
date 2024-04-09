from typing import List
import random

# Date of Last Practice: Mar 7, 2024
#
# Time Complexity: O(N), where N is the length of the input list.
#                  We iterate through the list once to create the prefix sum array.
#                  The binary search in the prefix sum array is O(log N).
#
# Space Complexity: O(N), where N is the length of the input list.
#                   The prefix sum array effectively divides the range from 1 to
#                   the total sum of the weights into several segments,
#                   where the length of each segment is proportional to
#                   the weight of the corresponding index.


class Solution:

    def __init__(self, w: List[int]):
        self.prefix_sums = []
        prefix_sum = 0
        for weight in w:
            prefix_sum += weight
            self.prefix_sums.append(prefix_sum)

    def pickIndex(self) -> int:
        random_int = random.randrange(1, self.prefix_sums[-1] + 1)
        left, right = 0, len(self.prefix_sums) - 1

        while left <= right:
            pivot = (left + right) // 2
            if random_int == self.prefix_sums[pivot]:
                return pivot
            if random_int > self.prefix_sums[pivot]:
                left = pivot + 1
            else:
                right = pivot - 1

        return left


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()

# Test cases
solution = Solution([1, 3])
print(solution.pickIndex())  # This will print an index, 0 or 1, based on the weight.
