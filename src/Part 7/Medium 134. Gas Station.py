"""
Solution to the Gas Station problem using a single-pass greedy algorithm.

This module provides a solution to the Gas Station problem using a single-pass
greedy algorithm. The solution determines the starting gas station index from 
which a car can complete a circuit around the gas stations, or returns -1 if 
no such station exists.
"""

from typing import List

# Date of Last Practice: Aug 13, 2024
#
# Time Complexity: O(N), where N is the length of the gas list.
#
# Space Complexity: O(1), as we only use a constant amount of extra space.


class Solution:
    """Determine the starting gas station index."""

    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """
        One pass greedy algorithm to determine the starting gas station index.

        Determines if there exists a starting gas station index from which
        the car can complete the circuit. Returns the starting index or -1 if
        no such station exists.

        Args:
            gas: List of integers representing gas available at each station.
            cost: List of integers representing gas cost to travel to the next station.

        Returns:
            int: The starting station index if a valid start exists, otherwise -1.
        """
        total_gas = 0
        total_cost = 0
        start = 0
        tank = 0

        for i, _ in enumerate(gas):
            total_gas += gas[i]
            total_cost += cost[i]
            tank += gas[i] - cost[i]

            # If tank is negative, it indicates that this segment cannot be part of
            # a feasible solution, so reset the starting station to i + 1.
            if tank < 0:
                start = i + 1
                tank = 0

        # Global Guarantee: The single pass simultaneously tracks the total gas
        # and total cost. If total_gas >= total_cost, there is enough fuel in
        # the system to complete the entire circuit. Therefore, by the time the
        # algorithm finishes this single pass, if a valid start index exists,
        # the algorithm will have identified it.
        #
        # If a lack of gas forces you to skip an earlier station, the new
        # starting point must compensate for the previous deficiency when
        # completing the cycle.

        return start if total_gas >= total_cost else -1


def main():
    """Demonstrate the Solution class with test cases."""
    solution = Solution()

    # Test Case 1: Expected output is 3
    assert solution.canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]) == 3

    # Test Case 2: Expected output is -1
    assert solution.canCompleteCircuit([2, 3, 4], [3, 4, 3]) == -1

    # Test Case 3: Expected output is 4
    assert solution.canCompleteCircuit([5, 1, 2, 3, 4], [4, 4, 1, 5, 1]) == 4

    # Test Case 4: Expected output is -1
    assert solution.canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 2, 2]) == -1

    print("All test cases passed!")


if __name__ == "__main__":
    main()
