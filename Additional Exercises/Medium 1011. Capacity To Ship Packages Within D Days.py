"""
Determine the minimum ship capacity to ship packages within a given number of days.

This module defines a class to compute the least weight capacity of a ship that allows
all packages on a conveyor belt to be shipped within the specified number of days.

Typical usage example:

1. Import the Solution class.
2. Create an instance of Solution and call the shipWithinDays method with appropriate 
   arguments.
"""

from typing import List


class Solution:
    """
    Find the minimum ship capacity to ship packages within a given number of days.

    Methods:
        shipWithinDays(weights: List[int], days: int) -> int
    """

    def shipWithinDays(self, weights: List[int], days: int) -> int:
        """
        Find the minimum ship capacity to ship packages within a given number of days.

        The function uses binary search to find the minimum ship capacity required to
        ship all packages within the given number of days.

        Args:
            weights: List[int]: List of package weights.
            days: int: Number of days to ship all packages.

        Returns:
            int: Minimum ship capacity required.
        """

        def _is_valid_capacity(capacity: int, days: int) -> bool:
            """
            Checks if a given ship capacity can ship all packages within `days`.

            Args:
                capacity: int: Ship capacity to test.
                days: int: Number of days to ship all packages.

            Returns:
                bool: True if the capacity is valid, otherwise False.
            """
            current_weight = 0
            for weight in weights:
                current_weight += weight
                if current_weight > capacity:
                    days -= 1
                    if days == 0:
                        return False
                    current_weight = weight
            return True

        # Step 1: Initialize left to max(weights) and right to sum(weights)
        left, right = max(weights), sum(weights)

        # Step 2: Perform binary search
        while left <= right:
            mid = (left + right) // 2
            if _is_valid_capacity(mid, days):
                right = mid - 1
            else:
                left = mid + 1

        # Step 3: Return the minimum capacity found
        return left


# Test Cases
def test_solution():
    """Perform unit tests."""

    sol = Solution()

    # Test Case 1
    assert sol.shipWithinDays([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5) == 15

    # Test Case 2
    assert sol.shipWithinDays([3, 2, 2, 4, 1, 4], 3) == 6

    # Test Case 3
    assert sol.shipWithinDays([1, 2, 3, 1, 1], 4) == 3

    # Additional Test Case 4
    assert sol.shipWithinDays([10, 50, 100, 20, 5], 3) == 100

    # Additional Test Case 5
    assert sol.shipWithinDays([5, 5, 5, 5, 5, 5], 3) == 10

    print("All test cases passed.")


if __name__ == "__main__":
    test_solution()
