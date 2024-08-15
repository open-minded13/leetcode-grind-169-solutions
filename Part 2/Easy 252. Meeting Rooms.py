"""
Determine if a person can attend all meetings.

This module provides a solution to check if a set of meeting time intervals
overlap, which would prevent a person from attending all meetings.
"""

from typing import List

# Date of Last Practice: Aug 15, 2024
#
# Time Complexity: O(N log N), where N is the number of meeting time intervals.
#                  The time complexity is dominated by the sorting of the intervals.
#
# Space Complexity: O(1), since we are using only a constant amount of extra space.


class Solution:
    """
    Determine if a person can attend all meetings.

    This class provides a method to check for overlapping intervals in a
    schedule.
    """

    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        """
        Check if a person can attend all meetings.

        The method sorts the intervals by their start time, then checks for
        any overlap between consecutive meetings.

        Args:
            intervals (List[List[int]]): List of meeting time intervals, where
                                         each interval is represented as
                                         [start, end].

        Returns:
            bool: True if a person can attend all meetings, False if there is
                  any overlap between meetings.
        """
        # Sort intervals by start time.
        intervals.sort()

        # Initialize the end time of the last meeting attended.
        current_max_right = 0

        # Iterate through the intervals to check for overlaps.
        for left, right in intervals:
            # If the start time of the current meeting is before the
            # end time of the last meeting attended, return False.
            if left < current_max_right:
                return False
            # Update the end time of the last meeting attended.
            current_max_right = right

        # If no overlaps are found, return True.
        return True


def main():
    """
    Demonstrate the usage of the Solution class with test cases.

    This function initializes the Solution class and runs several test
    cases to verify the correctness of the canAttendMeetings method.
    """
    # Initialize the solution instance.
    solution = Solution()

    # Test cases.
    assert (
        solution.canAttendMeetings([[0, 30], [5, 10], [15, 20]]) is False
    ), "Test case 1 failed"
    assert solution.canAttendMeetings([[7, 10], [2, 4]]) is True, "Test case 2 failed"
    assert (
        solution.canAttendMeetings([[1, 5], [6, 10], [11, 15]]) is True
    ), "Test case 3 failed"
    assert (
        solution.canAttendMeetings([[1, 10], [2, 5], [6, 8]]) is False
    ), "Test case 4 failed"

    print("All test cases passed!")


if __name__ == "__main__":
    main()
