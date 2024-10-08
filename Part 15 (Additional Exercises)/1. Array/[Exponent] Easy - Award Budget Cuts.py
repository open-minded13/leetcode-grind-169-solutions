"""
Reallocate research grants to meet the reduced budget constraints.

This module defines a class to find the cap for research grants such that the
sum of the grants meets a new reduced budget, impacting the fewest recipients.
Any grant above the cap is reduced to the cap value.
"""

from typing import List

# Date of Last Practice: Sep 23, 2024 -> Oct 7, 2024
#
# Time Complexity: O(N log N), where N is the number of grants.
#                  - Sorting the grants array takes O(N log N) time.
#                  - Iterating over the grants array takes O(N) time.
#                  - Total time complexity is O(N log N).
#
# Space Complexity: O(1), since we are using constant space.


class Solution:
    """Handles the reallocation of research grants within a reduced budget."""

    def find_grants_cap(self, grantsArray: List[int], newBudget: int) -> float:
        """
        Find the maximum cap to minimize the impact on grants allocation.

        Args:
            grantsArray (List[int]): List of initial grant amounts.
            newBudget (int): The available new budget.

        Returns:
            float: The maximum cap such that the sum of all capped grants equals
                   the new budget.
        """
        # Step 1 - Sort the grants array for easier cap calculation.
        grantsArray.sort()

        # Step 2 - Get the number of grants (N).
        grant_length = len(grantsArray)

        # Step 3 - Initialize the current cap as the average of the new budget.
        current_cap = newBudget / grant_length

        # Step 4 - Iterate over the grants and adjust the budget and cap.
        for i, grant in enumerate(grantsArray):
            # Step 4a - If the current cap is greater than the current grant,
            # reduce the budget by the grant amount.
            if current_cap > grant:
                newBudget -= grant

                # Step 4b - Recalculate the cap for the remaining grants.
                current_cap = newBudget / (grant_length - i - 1)
            else:
                # Step 4c - If the cap is less than or equal to the grant,
                # no further adjustment needed, break the loop.
                break

        # Step 5 - Return the calculated cap.
        return current_cap


def main():
    """
    Main function to demonstrate the usage of the Solution class.
    """
    solution = Solution()

    # Test case 1
    grantsArray1 = [2, 100, 50, 120, 1000]
    newBudget1 = 190
    assert round(solution.find_grants_cap(grantsArray1, newBudget1), 2) == 47.0

    # Test case 2
    grantsArray2 = [2, 4, 6]
    newBudget2 = 6
    assert round(solution.find_grants_cap(grantsArray2, newBudget2), 2) == 2.0

    # Test case 3
    grantsArray3 = [1, 1, 1, 1, 1]
    newBudget3 = 5
    assert round(solution.find_grants_cap(grantsArray3, newBudget3), 2) == 1.0

    # Test case 4
    grantsArray4 = [1, 2, 3, 4, 5]
    newBudget4 = 10
    assert round(solution.find_grants_cap(grantsArray4, newBudget4), 2) == 2.33

    # Test case 5
    grantsArray5 = [210, 200, 150, 193, 130, 110, 209, 342, 117]
    newBudget5 = 1530
    assert round(solution.find_grants_cap(grantsArray5, newBudget5), 2) == 211.0

    print("All test cases passed!")


if __name__ == "__main__":
    main()
