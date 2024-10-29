"""Task Scheduler with cooldown period between repeating tasks.

This module provides a solution to the "Task Scheduler II" problem on LeetCode.
It determines the minimum number of days needed to complete all tasks in a 
given sequence, while adhering to a mandatory cooldown period between 
repeating tasks.

Example usage:
    solution = Solution()
    result = solution.taskSchedulerII([1, 2, 1, 2, 3, 1], 3)
    assert result == 9
"""

from typing import List

# Date of Last Practice: Oct 29, 2024
#
# Time Complexity: O(N), where N is the number of tasks in the input list.
#
# Space Complexity: O(M), where M is the number of unique tasks in the input list.


class Solution:
    """Determines minimum days needed to complete tasks with a cooldown period.

    Methods:
        taskSchedulerII(tasks, space): Calculates the minimum days required to
        complete all tasks based on cooldown requirements.
    """

    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        """Calculates minimum days to complete all tasks with cooldown period.

        Args:
            tasks (List[int]): List of tasks represented by integers.
            space (int): Minimum days required between repeating the same task.

        Returns:
            int: Minimum number of days to complete all tasks.
        """
        last_time = {}  # Tracks the last completion day for each task type
        cur_time = 0  # Current day count

        for task in tasks:
            cur_time += 1  # Move to the next day
            if task in last_time:
                # Enforce the cooldown by moving the day forward if needed
                cur_time = max(cur_time, last_time[task] + space + 1)
            last_time[task] = cur_time  # Update the last completion day for task

        return cur_time


# Testing the Solution class with sample test cases
def main():
    """Runs example test cases to validate the Solution class."""
    solution = Solution()

    # Test case 1
    assert solution.taskSchedulerII([1, 2, 1, 2, 3, 1], 3) == 9, "Test case 1 failed"
    # Test case 2
    assert solution.taskSchedulerII([5, 8, 8, 5], 2) == 6, "Test case 2 failed"
    # Additional test case
    assert solution.taskSchedulerII([1, 1, 1], 2) == 7, "Test case 3 failed"

    print("All test cases passed.")


if __name__ == "__main__":
    main()
