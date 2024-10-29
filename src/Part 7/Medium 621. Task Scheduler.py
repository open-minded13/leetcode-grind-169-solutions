"""Solution to the Task Scheduler problem.

This module defines a class `Solution` to solve the Task Scheduler problem,
where tasks are scheduled with a cooldown period between identical tasks.
It calculates the minimum time required to complete all tasks with the given
constraints.

Typical usage example:
    sol = Solution()
    result = sol.leastInterval(["A", "A", "A", "B", "B", "B"], 2)
    print(result)  # Expected output: 8
"""

from typing import List
from collections import Counter

# Date of Last Practice: Jan 17, 2024 -> Feb 26, 2024 -> Oct 29, 2024
#
# Time Complexity: O(N), where N is the number of tasks.
#
# Space Complexity: O(1). We need space to store the count of each task.
#                   In the worst case, this can be as large as the number of distinct
#                   tasks. However, since the task identifiers are uppercase English
#                   letters, there's a fixed maximum of 26 possible tasks. Therefore,
#                   this space requirement is O(1) — constant space.
#
# Step 1 - The Most Frequent Tasks Set the Minimum Timeframe: The tasks that occurs
#          the most frequently sets a minimum bound for the time needed. This is because
#          it will require the most cooldown periods.
#
#          NOTE: We may have multiple tasks occur the most frequently to initialize.
#                Let's consider tasks = "AAAA BBBB C D E FFF".
#                If you only initialize one of the most frequent tasks,
#                such as "A___A___A___A", you will get a result "ABCDABEFABF_BF",
#                which is not the most efficient as "ABFCABFDABFEAB".
#
# Step 2 - Idle Slots: After placing the most frequent tasks with its necessary cooldown
#          periods, we get a series of slots that can be filled with other tasks.
#
# Step 3 - Filling the Slots: If we can fill all these slots with other tasks, we don't
#          need any idle time. If there aren't enough tasks to fill the slots, the
#          remaining slots become idle time.
#
# Step 4 - After Filling All Slots: Once all slots are filled, we can start another
#          cycle of the most frequent task "without needing idle time," as the cooldown
#          period for the most frequent task has been met.
#
# Why No More Idle After Filling Slots:
#
# 1. Cooldown Period is Respected: Once you've filled the cooldown slots for the most
#    frequent task, you've ensured this task won't appear again until after n slots.
#
# 2. Other Tasks Don't Need as Much Cooldown: Other tasks are less frequent, meaning
#    they naturally fit into the gaps without needing extra idle time.
#
# 3. Efficient Use of Time Slots: By the time you need to place the most frequent task
#    again, you've used up other tasks in the cooldown slots, making room for the most
#    frequent task without additional idle time.


class Solution:
    """Calculates the minimum units of time required to finish all tasks.

    Attributes:
        tasks (List[str]): A list of tasks represented by uppercase English letters.
        n (int): Non-negative integer representing the cooldown period between
                 identical tasks.
    """

    def leastInterval(self, tasks: List[str], n: int) -> int:
        """Returns the least number of time units required to complete all tasks.

        Args:
            tasks (List[str]): A list of uppercase English letter tasks.
            n (int): The cooldown period between two identical tasks.

        Returns:
            int: Minimum number of units of time to complete all tasks.
        """
        # Step 1 - Count the frequency of each task
        task_counts = Counter(tasks)

        # Step 2 - Find the maximum frequency and the number of tasks with that
        #          frequency
        max_count = max(task_counts.values())
        max_count_tasks = sum(1 for count in task_counts.values() if count == max_count)

        # Step 3 - Calculate the base required slots considering the most frequent tasks
        gap_count = max_count - 1
        gap_length = n - (max_count_tasks - 1)
        empty_slots = gap_count * gap_length

        # Step 4 - Calculate remaining tasks to fill empty slots, if possible
        available_tasks = len(tasks) - (max_count * max_count_tasks)
        idles = max(0, empty_slots - available_tasks)

        # Step 5 - Return the total length of tasks and required idle slots
        return len(tasks) + idles


# Test cases
def main():
    """Runs test cases to verify the correctness of the `leastInterval` method."""
    sol = Solution()

    # Test Case 1
    assert sol.leastInterval(["A", "A", "A", "B", "B", "B"], 2) == 8

    # Test Case 2
    assert sol.leastInterval(["A", "A", "A", "B", "B", "B"], 0) == 6

    # Test Case 3
    assert (
        sol.leastInterval(
            ["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"], 2
        )
        == 16
    )

    # Custom Complex Test Case
    tasks = [
        "F",
        "J",
        "J",
        "A",
        "J",
        "F",
        "C",
        "H",
        "J",
        "B",
        "E",
        "G",
        "G",
        "F",
        "A",
        "C",
        "I",
        "F",
        "J",
        "C",
        "J",
        "C",
        "H",
        "C",
        "A",
        "D",
        "G",
        "H",
        "B",
        "F",
        "G",
        "C",
        "C",
        "A",
        "E",
        "B",
        "H",
        "J",
        "E",
        "I",
        "F",
        "D",
        "E",
        "A",
        "C",
        "D",
        "B",
        "D",
        "J",
        "J",
        "C",
        "F",
        "D",
        "D",
        "J",
        "H",
        "A",
        "E",
        "C",
        "D",
        "J",
        "D",
        "G",
        "G",
        "B",
        "C",
        "E",
        "G",
        "H",
        "I",
        "D",
        "H",
        "F",
        "E",
        "I",
        "B",
        "D",
        "E",
        "I",
        "E",
        "C",
        "J",
        "G",
        "I",
        "D",
        "E",
        "D",
        "J",
        "C",
        "A",
        "C",
        "C",
        "D",
        "I",
        "J",
        "B",
        "D",
        "H",
        "H",
        "J",
        "G",
        "B",
        "G",
        "A",
        "H",
        "E",
        "H",
        "E",
        "D",
        "E",
        "J",
        "E",
        "J",
        "C",
        "F",
        "C",
        "J",
        "G",
        "B",
        "C",
        "I",
        "I",
        "H",
        "F",
        "A",
        "D",
        "G",
        "F",
        "C",
        "C",
        "F",
        "G",
        "C",
        "J",
        "B",
        "B",
        "I",
        "C",
        "J",
        "J",
        "E",
        "G",
        "H",
        "C",
        "I",
        "G",
        "J",
        "I",
        "G",
        "G",
        "J",
        "G",
        "G",
        "E",
        "G",
        "B",
        "I",
        "J",
        "B",
        "H",
        "D",
        "H",
        "G",
        "F",
        "C",
        "H",
        "C",
        "D",
        "A",
        "G",
        "B",
        "H",
        "H",
        "B",
        "J",
        "C",
        "A",
        "F",
        "J",
        "G",
        "F",
        "E",
        "B",
        "F",
        "E",
        "B",
        "B",
        "A",
        "E",
        "F",
        "E",
        "H",
        "I",
        "I",
        "C",
        "G",
        "J",
        "D",
        "H",
        "E",
        "F",
        "G",
        "G",
        "D",
        "E",
        "B",
        "F",
        "J",
        "J",
        "J",
        "D",
        "H",
        "E",
        "B",
        "D",
        "J",
        "I",
        "F",
        "C",
        "I",
        "E",
        "H",
        "F",
        "E",
        "G",
        "D",
        "E",
        "C",
        "F",
        "E",
        "D",
        "E",
        "A",
        "I",
        "E",
        "A",
        "D",
        "H",
        "G",
        "C",
        "I",
        "E",
        "G",
        "A",
        "H",
        "I",
        "G",
        "G",
        "A",
        "G",
        "F",
        "H",
        "J",
        "D",
        "F",
        "A",
        "G",
        "H",
        "B",
        "J",
        "A",
        "H",
        "B",
        "H",
        "C",
        "G",
        "F",
        "A",
        "C",
        "C",
        "B",
        "I",
        "G",
        "G",
        "B",
        "C",
        "J",
        "J",
        "I",
        "E",
        "G",
        "D",
        "I",
        "J",
        "I",
        "C",
        "G",
        "A",
        "J",
        "G",
        "F",
        "J",
        "F",
        "C",
        "F",
        "G",
        "J",
        "I",
        "E",
        "B",
        "G",
        "F",
        "A",
        "D",
        "A",
        "I",
        "A",
        "E",
        "H",
        "F",
        "D",
        "D",
        "C",
        "B",
        "J",
        "I",
        "J",
        "H",
        "I",
        "C",
        "D",
        "A",
        "G",
        "F",
        "I",
        "B",
        "E",
        "D",
        "C",
        "J",
        "G",
        "I",
        "H",
        "E",
        "C",
        "E",
        "I",
        "I",
        "B",
        "B",
        "H",
        "J",
        "C",
        "F",
        "I",
        "D",
        "B",
        "F",
        "H",
        "F",
        "A",
        "C",
        "A",
        "A",
        "B",
        "D",
        "C",
        "A",
        "G",
        "B",
        "G",
        "F",
        "E",
        "G",
        "A",
        "A",
        "A",
        "C",
        "J",
        "H",
        "H",
        "G",
        "C",
        "C",
        "B",
        "C",
        "E",
        "B",
        "E",
        "F",
        "I",
        "E",
        "E",
        "D",
        "I",
        "H",
        "G",
        "F",
        "A",
        "H",
        "B",
        "J",
        "B",
        "G",
        "H",
        "C",
        "C",
        "B",
        "G",
        "C",
        "B",
        "A",
        "E",
        "G",
        "A",
        "J",
        "G",
        "D",
        "C",
        "I",
        "G",
        "F",
        "G",
        "G",
        "A",
        "J",
        "E",
        "I",
        "D",
        "E",
        "A",
        "F",
        "A",
        "H",
        "C",
        "E",
        "D",
        "D",
        "D",
        "H",
        "I",
        "F",
        "F",
        "A",
        "F",
        "A",
        "A",
        "C",
        "J",
        "D",
        "J",
        "H",
        "I",
        "F",
        "A",
        "C",
        "B",
        "C",
        "A",
        "C",
        "C",
        "H",
        "A",
        "J",
        "I",
        "B",
        "A",
        "I",
        "F",
        "J",
        "C",
        "I",
        "B",
        "C",
        "E",
        "E",
        "E",
        "J",
        "G",
        "F",
        "E",
        "I",
        "A",
        "A",
        "E",
        "B",
        "J",
        "H",
        "H",
        "H",
        "A",
        "H",
        "J",
        "E",
        "F",
        "E",
        "F",
        "G",
        "J",
        "D",
        "I",
        "D",
        "I",
        "F",
        "B",
        "J",
        "D",
        "A",
        "A",
        "D",
        "F",
        "G",
        "B",
        "J",
        "H",
        "F",
        "A",
        "D",
        "H",
        "C",
        "B",
        "A",
        "J",
        "H",
        "I",
        "F",
        "H",
        "E",
        "G",
        "B",
        "A",
        "F",
        "F",
        "A",
        "C",
        "D",
        "G",
        "I",
        "I",
        "J",
        "H",
        "H",
        "C",
        "J",
        "G",
        "B",
        "A",
        "D",
        "B",
        "F",
        "J",
        "D",
        "I",
        "A",
        "F",
        "F",
        "F",
        "F",
        "A",
        "E",
        "B",
        "C",
        "G",
        "H",
        "E",
        "B",
        "B",
        "A",
        "G",
        "D",
        "C",
        "C",
        "E",
        "A",
        "C",
        "F",
        "G",
        "A",
        "I",
        "F",
        "B",
        "H",
        "J",
        "G",
        "C",
        "B",
        "H",
        "D",
        "A",
        "H",
        "B",
        "H",
        "H",
        "C",
        "A",
        "F",
        "I",
        "C",
        "F",
        "A",
        "C",
        "J",
        "I",
        "H",
        "H",
        "F",
        "B",
        "B",
        "D",
        "E",
        "C",
        "J",
        "F",
        "C",
        "E",
        "A",
        "J",
        "E",
        "C",
        "A",
        "E",
        "B",
        "A",
        "J",
        "F",
        "J",
        "J",
        "J",
        "H",
        "H",
        "C",
        "I",
        "E",
        "G",
        "G",
        "H",
        "J",
        "J",
        "H",
        "H",
        "H",
        "J",
        "H",
        "A",
        "G",
        "I",
        "C",
        "E",
        "C",
        "D",
        "G",
        "G",
        "F",
        "H",
        "D",
        "G",
        "H",
        "A",
        "E",
        "I",
        "D",
        "A",
        "H",
        "G",
        "E",
        "A",
        "B",
        "F",
        "I",
        "C",
        "A",
        "F",
        "B",
        "A",
        "I",
        "F",
        "G",
        "I",
        "F",
        "D",
        "A",
        "B",
        "J",
        "B",
        "D",
        "F",
        "G",
        "J",
        "J",
        "A",
        "A",
        "C",
        "H",
        "G",
        "F",
        "B",
        "I",
        "I",
        "J",
        "A",
        "H",
        "D",
        "F",
        "E",
        "F",
        "J",
        "B",
        "F",
        "C",
        "G",
        "E",
        "A",
        "G",
        "H",
        "E",
        "H",
        "H",
        "F",
        "I",
        "G",
        "C",
        "C",
        "G",
        "J",
        "B",
        "H",
        "F",
        "H",
        "D",
        "I",
        "B",
        "D",
        "I",
        "F",
        "H",
        "I",
        "D",
        "F",
        "G",
        "G",
        "E",
        "A",
        "C",
        "A",
        "G",
        "H",
        "G",
        "H",
        "J",
        "F",
        "D",
        "F",
        "G",
        "D",
        "D",
        "C",
        "J",
        "C",
        "J",
        "G",
        "G",
        "G",
        "G",
        "H",
        "H",
        "G",
        "D",
        "E",
        "H",
        "G",
        "C",
        "B",
        "F",
        "I",
        "F",
        "C",
        "H",
        "J",
        "I",
        "A",
        "F",
        "D",
        "C",
        "F",
        "C",
        "E",
        "E",
        "D",
        "D",
        "C",
        "G",
        "B",
        "F",
        "E",
        "J",
        "C",
        "I",
        "E",
        "D",
        "B",
        "B",
        "I",
        "I",
        "I",
        "H",
        "C",
        "E",
        "C",
        "J",
        "F",
        "G",
        "A",
        "I",
        "J",
        "D",
        "I",
        "C",
        "G",
        "F",
        "I",
        "E",
        "I",
        "E",
        "F",
        "A",
        "G",
        "E",
        "J",
        "A",
        "I",
        "A",
        "D",
        "A",
        "G",
        "J",
        "F",
        "E",
        "D",
        "I",
        "A",
        "E",
        "J",
        "I",
        "C",
        "J",
        "B",
        "F",
        "B",
        "E",
        "C",
        "E",
        "F",
        "G",
        "E",
        "J",
        "J",
        "I",
        "E",
        "D",
        "F",
        "C",
        "H",
        "H",
        "B",
        "G",
        "D",
        "I",
        "I",
        "F",
        "B",
        "G",
        "C",
        "F",
        "J",
        "B",
        "G",
        "J",
        "H",
        "D",
        "G",
        "C",
        "C",
        "I",
        "I",
        "E",
        "I",
        "B",
        "H",
        "B",
        "I",
        "G",
        "F",
        "H",
        "G",
        "C",
        "J",
        "D",
        "C",
        "E",
        "G",
        "F",
        "C",
        "H",
        "D",
        "A",
        "C",
        "D",
        "H",
        "B",
        "C",
        "H",
        "I",
        "B",
        "A",
        "J",
        "C",
        "B",
        "D",
        "J",
        "D",
        "H",
        "F",
        "B",
        "A",
        "G",
        "G",
        "J",
        "I",
        "E",
        "F",
        "A",
        "D",
        "H",
        "D",
        "B",
        "C",
        "A",
        "H",
        "F",
        "G",
        "B",
        "F",
        "H",
        "B",
        "H",
        "I",
        "J",
        "D",
        "H",
        "I",
        "B",
        "C",
        "D",
        "G",
        "A",
        "E",
        "A",
        "A",
        "I",
        "F",
        "I",
        "F",
        "B",
        "B",
        "I",
        "F",
        "A",
        "E",
        "I",
        "A",
        "B",
        "G",
        "C",
        "F",
        "I",
        "A",
        "F",
        "I",
        "D",
        "H",
        "B",
        "I",
        "I",
        "B",
        "J",
        "F",
        "E",
        "B",
        "B",
        "B",
        "D",
        "C",
        "J",
        "E",
        "J",
        "J",
        "G",
        "D",
        "F",
        "F",
        "F",
        "G",
        "I",
        "H",
        "J",
        "J",
        "G",
        "D",
        "G",
        "F",
    ]
    n = 8
    assert sol.leastInterval(tasks, n) == 1000  # Expected output: 1000

    print("All test cases passed!")


if __name__ == "__main__":
    main()
