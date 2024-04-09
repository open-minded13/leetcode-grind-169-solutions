from typing import List

# Date of Last Practice: Nov 6, 2023 -> Feb 3, 2024
#
# Time Complexity: O(N), where N is the number of intervals in the input list (i.e., intervals).
#
# Space Complexity: O(N), where N is the number of intervals in the input lists.
#                   The result list is used to store the merged intervals.
#                   In the worst case, if no merging occurs,
#                   the result list will contain the same number of intervals as
#                   the input lists (i.e., intervals and newInterval).
#                   Therefore, the space complexity for the result list is O(n).


class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        new_interval_inserted = False
        result = []
        for interval in intervals:
            # The new interval is after the range of the current interval.
            if newInterval[0] > interval[1]:
                result.append(interval)

            # The new interval is before the range of the current interval.
            elif newInterval[1] < interval[0]:
                if not new_interval_inserted:
                    result.append(newInterval)
                    new_interval_inserted = True
                result.append(interval)

            # The new internal completely or partially overlaps the range of the current internal.
            else:
                newInterval[0] = min(interval[0], newInterval[0])
                newInterval[1] = max(interval[1], newInterval[1])

        if not new_interval_inserted:
            result.append(newInterval)
        return result


# Test cases
solution = Solution()

intervals1 = [[1, 3], [6, 9]]
newInterval1 = [2, 5]
output1 = solution.insert(intervals1, newInterval1)
print(output1)  # Output: [[1, 5], [6, 9]]

intervals2 = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
newInterval2 = [4, 9]
output2 = solution.insert(intervals2, newInterval2)
print(output2)  # Output: [[1, 2], [3, 10], [12, 16]]

intervals3 = [[1, 3], [6, 9]]
newInterval3 = [4, 5]
output3 = solution.insert(intervals3, newInterval3)
print(output3)  # Output: [[1, 3], [4, 5], [6, 9]]
