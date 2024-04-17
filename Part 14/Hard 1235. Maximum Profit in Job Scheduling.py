from typing import List
from bisect import bisect_right

# Date of Last Practice: Apr 14, 2024
#
# Time Complexity: O(N * log N), where N is the total number of jobs.
#
#                  Sorting the Jobs: The first step in the solution involves
#                  sorting the list of jobs based on their end times.
#                  Sorting a list of size N typically uses
#                  an O(N log N) algorithm (like Timsort in Python).
#
#                  Binary Search using bisect_right: For each of the N jobs,
#                  the solution performs a binary search to find the index of
#                  the last job that ends before the current job starts.
#                  Since binary search on a sorted list of size N has a time complexity of
#                  O(log N), and this operation is done for each job,
#                  the total time complexity for all binary searches is O(N log N).
#
#                  Dynamic Programming Calculation: The solution iterates through each job
#                  to calculate the maximum profit. For each job, it accesses the DP array
#                  at specific indices (constant time operations),
#                  thus this part of the algorithm runs in O(N).
#
#                  Combining these components, the overall time complexity of the algorithm is
#                  O(N log N) + O(N log N) + O(N), which simplifies to O(N log N).
#
# Space Complexity: O(N), where N is the total number of jobs.
#
#                   Storage for Jobs and Times: The solution stores the jobs in a sorted list (jobs),
#                   and also separately maintains lists for startTimes and endTimes.
#                   This triples the storage required for job data,
#                   resulting in a space complexity of O(3N), which simplifies to O(N).
#
#                   DP Array: An array dp of size N + 1 is used to
#                   store the cumulative maximum profit up to each job.
#                   This adds an additional O(N) space requirement.


class Solution:
    def jobScheduling(
        self, startTime: List[int], endTime: List[int], profit: List[int]
    ) -> int:
        # Step 1: Sort jobs by end time
        jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])
        n = len(jobs)

        # Extract sorted start and end times for binary search
        endTimes = [job[1] for job in jobs]
        startTimes = [job[0] for job in jobs]

        # Step 2: Initialize DP array
        dp = [0] * (n + 1)

        # Step 3: Compute maximum profit using DP
        for i in range(1, n + 1):
            # Include current job's profit and find best previous non-conflicting job
            current_profit = jobs[i - 1][2]
            previous_index = bisect_right(
                endTimes, startTimes[i - 1]
            )  # Get index of last job that ends before this one starts
            # Max profit including this job
            dp[i] = max(dp[i - 1], dp[previous_index] + current_profit)

        # Final DP entry contains the answer
        return dp[n]


# Example test cases and assertions
sol = Solution()

# Test case 1
assert sol.jobScheduling([1, 2, 3, 3], [3, 4, 5, 6], [50, 10, 40, 70]) == 120
# Test case 2
assert (
    sol.jobScheduling([1, 2, 3, 4, 6], [3, 5, 10, 6, 9], [20, 20, 100, 70, 60]) == 150
)
# Test case 3
assert sol.jobScheduling([1, 1, 1], [2, 3, 4], [5, 6, 4]) == 6

# Additional test case
assert sol.jobScheduling([1, 3, 6], [2, 5, 8], [20, 20, 20]) == 60

print("All test cases passed!")

# Test Case 2 Visualization

# [1,2,4,6,3]
# [3,5,6,9,10]
#           ^
# cur_pro = 20
# pre_index = 0
# dp[1] = max dp[0] or dp[0]+20 = 20

# cur_pro = 20
# pre_index = 0
# dp[2] = max dp[1] or dp[0]+20 = 20

# cur_pro = 70
# pre_index = 1
# dp[3] = max dp[2] or dp[1]+70 = 90

# cur_pro = 60
# pre_index = 3
# dp[4] = max dp[3] or dp[3]+60 = 150

# dp[5] = max dp[4] or dp[0]+100 = max 150 or 20+100 = 150
