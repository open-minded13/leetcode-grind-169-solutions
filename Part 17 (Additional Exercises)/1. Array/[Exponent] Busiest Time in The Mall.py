"""
Find the busiest time in a mall using data from door detectors.

This module defines the Solution class and its method to find the time at
which the mall reached its busiest moment, given data points representing
visitor counts and entry/exit records.
"""

from typing import List

# Date of Last Practice: Oct 3, 2024
#
# Time Complexity: O(N), where N is the number of data points in the list.
#                  We iterate over each data point once.
#
# Space Complexity: O(1), as we use only a constant amount of space to store
#                   the current visitor count and peak visitor count.


class Solution:
    """
    Solution class to find the busiest moment in the mall last year.
    """

    def find_busiest_period(self, data: List[List[int]]) -> int:
        """
        Find the timestamp when the mall was busiest.

        This function takes a list of data points where each data point contains:
        - timestamp (int): Time in Unix format.
        - visitor count (int): Number of visitors entering or exiting.
        - entrance/exit flag (int): 1 for entrance, 0 for exit.

        Args:
            data (List[List[int]]): A sorted list of data points representing
                                    mall entries/exits.

        Returns:
            int: The timestamp at which the mall reached its busiest moment.
        """
        counter = 0  # Current number of people in the mall
        peak, peak_time = 0, 0  # Track peak visitor count and its timestamp

        # Step 1 - Iterate over each data point in the list.
        for i, (time, num_of_ppl, is_entrance) in enumerate(data):
            # Step 2 - Adjust counter based on whether visitors entered or exited.
            counter += num_of_ppl if is_entrance else -num_of_ppl

            # Step 3 - Check if the next data point has the same timestamp.
            # If yes, we skip the update until we process all records for the same time.
            if (i + 1) < len(data) and time == data[i + 1][0]:
                continue

            # Step 4 - Update the peak if the current counter exceeds the previous peak.
            if counter > peak:
                peak, peak_time = counter, time

        # Step 5 - Return the timestamp when the visitor count reached the highest.
        return peak_time


def main():
    """
    Main function to run test cases for the Solution class.
    """
    solution = Solution()

    # Test case 1
    data = [[1487799426, 21, 1]]
    assert solution.find_busiest_period(data) == 1487799426

    # Test case 2
    data = [[1487799425, 21, 0], [1487799427, 22, 1], [1487901318, 7, 0]]
    assert solution.find_busiest_period(data) == 1487799427

    # Test case 3
    data = [[1487799425, 21, 1], [1487799425, 4, 0], [1487901318, 7, 0]]
    assert solution.find_busiest_period(data) == 1487799425

    # Test case 4
    data = [
        [1487799425, 14, 1],
        [1487799425, 4, 0],
        [1487799425, 2, 0],
        [1487800378, 10, 1],
        [1487801478, 18, 0],
        [1487801478, 18, 1],
        [1487901013, 1, 0],
        [1487901211, 7, 1],
        [1487901211, 7, 0],
    ]
    assert solution.find_busiest_period(data) == 1487800378

    # Test case 5
    data = [
        [1487799425, 14, 1],
        [1487799425, 4, 1],
        [1487799425, 2, 1],
        [1487800378, 10, 1],
        [1487801478, 18, 1],
        [1487901013, 1, 1],
        [1487901211, 7, 1],
        [1487901211, 7, 1],
    ]
    assert solution.find_busiest_period(data) == 1487901211

    # Test case 6
    data = [
        [1487799425, 14, 1],
        [1487799425, 4, 0],
        [1487799425, 2, 0],
        [1487800378, 10, 1],
        [1487801478, 18, 0],
        [1487801478, 19, 1],
        [1487801478, 1, 0],
        [1487801478, 1, 1],
        [1487901013, 1, 0],
        [1487901211, 7, 1],
        [1487901211, 8, 0],
    ]
    assert solution.find_busiest_period(data) == 1487801478

    print("All test cases passed!")


if __name__ == "__main__":
    main()
