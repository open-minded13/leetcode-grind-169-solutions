"""
Search for the lowest index where the array element equals the index.

This module defines a class to search for the lowest index in a sorted array
where the array element is equal to its index. The function returns the index
if found, otherwise returns -1.

Typical usage example:

    solution = Solution()
    index = solution.index_equals_value_search([-8, 0, 2, 5])
    print(index)  # Output: 2
"""

from typing import List

# Date of Last Practice: Sep 30, 2024
#
# Time Complexity: O(log N), where N is the number of elements in the array.
#                  The binary search algorithm is used to find the index.
#
# Space Complexity: O(1), as we are using a constant amount of extra space.


class Solution:
    """
    A class to find the lowest index where arr[i] == i in a sorted array.

    Methods:
        index_equals_value_search: Performs a binary search to find the lowest
                                   index where arr[i] equals i.
    """

    def index_equals_value_search(self, arr: List[int]) -> int:
        """
        Searches for the lowest index where arr[i] == i using binary search.

        Args:
            arr (List[int]): A sorted array of distinct integers.

        Returns:
            int: The lowest index where arr[i] == i, or -1 if no such index
                 exists.
        """
        left, right = 0, len(arr) - 1

        # Step 1 - Perform binary search
        while left <= right:
            pivot = (left + right) // 2

            # Step 2 - Check if arr[pivot] == pivot
            if arr[pivot] == pivot:
                # Step 3 - Ensure it's the lowest index by checking the previous index
                if pivot == 0 or arr[pivot - 1] != pivot - 1:
                    return pivot
                right = pivot - 1
            # Step 4 - Adjust search space based on the value of arr[pivot]
            elif arr[pivot] > pivot:
                right = pivot - 1
            else:
                left = pivot + 1

        # Step 5 - Return -1 if no index was found where arr[i] == i
        return -1


def main():
    """
    Main function to test the Solution class with various test cases.
    """
    solution = Solution()

    # Test cases with assert statements
    assert solution.index_equals_value_search([0]) == 0, "Test case 1 failed"
    assert solution.index_equals_value_search([0, 3]) == 0, "Test case 2 failed"
    assert (
        solution.index_equals_value_search([-8, 0, 1, 3, 5]) == 3
    ), "Test case 3 failed"
    assert (
        solution.index_equals_value_search([-5, 0, 2, 3, 10, 29]) == 2
    ), "Test case 4 failed"
    assert (
        solution.index_equals_value_search([-5, 0, 3, 4, 10, 18, 27]) == -1
    ), "Test case 5 failed"
    assert (
        solution.index_equals_value_search([-6, -5, -4, -1, 1, 3, 5, 7]) == 7
    ), "Test case 6 failed"

    print("All test cases passed.")


if __name__ == "__main__":
    main()
