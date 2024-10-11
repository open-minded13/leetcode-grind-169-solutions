from typing import List

# Date of Last Practice: Dec 26, 2023 -> Feb 12, 2024
#
# Time Complexity: O(N * log N), where N is the number of intervals.
#                  This is due to the initial sort.
#                  The merging process itself is O(N) as it
#                  involves a single pass through the sorted intervals.
#
# Space Complexity: O(1), as we don't use any extra space
#                   apart from the input and output arrays.


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        intervals = sorted(intervals, key=lambda x: x[0])
        merged_intervals = []
        for interval in intervals:
            if not merged_intervals:
                merged_intervals.append(list(interval))
                continue
            if merged_intervals[-1][1] < interval[0]:
                merged_intervals.append(list(interval))
            else:
                merged_intervals[-1][1] = max(merged_intervals[-1][1], interval[1])

        return merged_intervals


# Test cases
sol = Solution()

# Test case 1
print(
    sol.merge([[1, 3], [2, 6], [8, 10], [15, 18]])
)  # Expected output: [[1,6],[8,10],[15,18]]

# Test case 2
print(sol.merge([[1, 4], [4, 5]]))  # Expected output: [[1,5]]
