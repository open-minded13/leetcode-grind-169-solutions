"""
Find the earliest meeting time slot that works for both participants.

This module contains a class with a method that finds the earliest available 
time slot for two participants given their availability slots and the required 
meeting duration.
"""

from typing import List

# Date of Last Practice: 24 Sep, 2024 -> 6 Oct, 2024
#
# Time Complexity: O(N * log N + M * log M), where N and M are the lengths of
#                  slots1 and slots2.
#
#                  - Sorting both lists takes O(N * log N + M * log M) time.
#                  - Traversing the sorted lists takes O(N + M) time.
#
# Space Complexity: O(N + M), where N and M are the lengths of slots1 and slots2.
#                   In Python, the sort() method uses Timsort, which is a hybrid sorting
#                   algorithm derived from merge sort and insertion sort. The sort()
#                   method has a space complexity of O(N) for the worst-case scenario,
#                   where N is the length of the input list. Therefore, the space
#                   complexity of the sorting step is O(N + M) for the two input lists.


class Solution:
    """Provides a solution to find the earliest common available duration."""

    def minAvailableDuration(
        self, slots1: List[List[int]], slots2: List[List[int]], duration: int
    ) -> List[int]:
        """
        Returns the earliest common time slot that satisfies the required duration.

        Args:
            slots1: List of time slots for the first participant, where each slot
                    is a list of two integers representing [start, end].
            slots2: List of time slots for the second participant, where each slot
                    is a list of two integers representing [start, end].
            duration: The required meeting duration.

        Returns:
            A list with the start and end times of the earliest available common
            time slot of the required duration. If no common time slot is found,
            returns an empty list.
        """

        # Step 1 - Sort both lists based on the start times
        slots1.sort(key=lambda item: item[0])
        slots2.sort(key=lambda item: item[0])

        # Step 2 - Initialize two pointers for traversing slots1 and slots2
        s1_index, s2_index = 0, 0

        # Step 3 - Iterate through both lists
        while s1_index < len(slots1) and s2_index < len(slots2):
            # Find the maximum start time and minimum end time of the current slots
            start = max(slots1[s1_index][0], slots2[s2_index][0])
            end = min(slots1[s1_index][1], slots2[s2_index][1])

            # Step 4 - Check if there is enough time in this overlap
            if end - start >= duration:
                # Return the earliest possible time slot of the required duration
                return [start, start + duration]

            # Step 5 - Move to the next slot in the list with the earlier end time
            if slots1[s1_index][1] < slots2[s2_index][1]:
                s1_index += 1
            else:
                s2_index += 1

        # Step 6 - Return an empty list if no valid time slot is found
        return []


def main():
    """
    Demonstrates the usage of the Solution class by testing various test cases.
    """
    solution = Solution()

    # Test Case 1
    slots1 = [[10, 50], [60, 120], [140, 210]]
    slots2 = [[0, 15], [60, 70]]
    duration = 8
    assert solution.minAvailableDuration(slots1, slots2, duration) == [60, 68]

    # Test Case 2
    slots1 = [[10, 50], [60, 120], [140, 210]]
    slots2 = [[0, 15], [60, 70]]
    duration = 12
    assert solution.minAvailableDuration(slots1, slots2, duration) == []

    # Test Case 3
    slots1 = [[0, 5], [10, 15]]
    slots2 = [[5, 10], [15, 20]]
    duration = 5
    assert solution.minAvailableDuration(slots1, slots2, duration) == []

    print("All test cases passed!")


if __name__ == "__main__":
    main()
