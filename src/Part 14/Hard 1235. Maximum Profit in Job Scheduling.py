"""Calculate the maximum profit from non-overlapping job schedules.

Visualizing the dynamic programming table:

#      V
# srt  1 |   2 |   4 |   6 |   3 |
#      v
# end  3 |   5 |   6 |   9 |  10 |
# pro 20 |  20 |  70 |  60 | 100 |
#
# dp  <3 | <=3 | <=5 | <=6 | <=9 | <=10 |
#      0 |   0 |   0 |   0 |   0 |    0 |
#            ^

Note: srt = start time, end = end time, pro = profit, dp = dynamic programming table.
      V = vertical arrow showing the current job being processed.
      v = vertical arrow showing the binary search result for the current job,
          indicating the last job that ends before the current job starts.
      ^ = horizontal arrow showing the current position in the DP table.

The final DP table helps compute the maximum possible profit by comparing the 
options of including or excluding each job based on their end and start times.
"""

from typing import List
from bisect import bisect_right

# Date of Last Practice: Apr 14, 2024 -> Oct 22, 2024
#
# Time Complexity: O(N * log N), where N is the total number of jobs.
#
#                  Sorting the Jobs: The first step in the solution involves sorting the
#                  list of jobs based on their end times. Sorting a list of size N
#                  typically uses an O(N log N) algorithm (like Timsort in Python).
#
#                  Binary Search: For each of the N jobs, the solution performs a binary
#                  search to find the index of the last job that ends before the current
#                  job starts.
#
#                  So, the total time complexity for all binary searches is O(N log N).
#
# Space Complexity: O(N), where N is the total number of jobs.
#
#                   Storage for Jobs and Times: We store the jobs in a sorted list,
#                   and also separately maintains lists for start times, end times,
#                   and profits. This triples the storage required for job data,
#                   resulting in a space complexity of O(3N), which simplifies to O(N).
#
#                   DP Array: An array dp of size N + 1 is used to
#                   store the cumulative maximum profit up to each job.
#                   This adds an additional O(N) space requirement.


class Solution:
    """Computes maximum profit from a set of jobs without overlap."""

    def jobScheduling(
        self, startTime: List[int], endTime: List[int], profit: List[int]
    ) -> int:
        """Returns the maximum profit from non-overlapping jobs.

        Args:
            startTime: List of integers representing start times of jobs.
            endTime: List of integers representing end times of jobs.
            profit: List of integers representing profits of jobs.

        Returns:
            The maximum profit achievable without job time conflicts.
        """
        # Step 1: Combine job data into tuples and sort them by end time.
        jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])

        # Step 2: Extract the sorted start and end times for binary search.
        start_times = [job[0] for job in jobs]
        end_times = [job[1] for job in jobs]
        profits = [job[2] for job in jobs]

        total_jobs = len(jobs)
        dp = [0] * (total_jobs + 1)  # Step 3: DP table to store max profits

        # Step 4: Compute the maximum profit using DP and binary search.
        for i in range(1, total_jobs + 1):
            current_profit = profits[i - 1]
            # Use bisect_right to find the latest job that ends before the
            # current job starts.
            previous_index = bisect_right(end_times, start_times[i - 1])
            # Step 5: DP recurrence relation to find max profit by including or
            #         excluding the job.
            dp[i] = max(dp[i - 1], dp[previous_index] + current_profit)

        # Step 6: Return the result which is stored in the last DP entry.
        return dp[total_jobs]


def main():
    """Demonstrates usage of the Solution class and validates with test cases."""
    sol = Solution()

    # Example test cases and assertions
    assert sol.jobScheduling([1, 2, 3, 3], [3, 4, 5, 6], [50, 10, 40, 70]) == 120
    assert (
        sol.jobScheduling([1, 2, 3, 4, 6], [3, 5, 10, 6, 9], [20, 20, 100, 70, 60])
        == 150
    )
    assert sol.jobScheduling([1, 1, 1], [2, 3, 4], [5, 6, 4]) == 6

    # Additional test cases
    assert sol.jobScheduling([1, 3, 6], [2, 5, 8], [20, 20, 20]) == 60
    assert (
        sol.jobScheduling([1, 2, 3, 3, 5], [2, 3, 4, 6, 8], [50, 10, 40, 100, 200])
        == 250
    )

    print("All test cases passed!")


if __name__ == "__main__":
    main()
