"""
Pancake sorting using a series of flips.

This module provides a solution to the Pancake Sorting problem using a class-based 
approach. The goal is to sort a given list of integers by performing a series of 
reversals (flips) on subarrays. A flip operation reverses the order of the first 
k elements in the list.

The module includes the `Solution` class, which implements the pancake sorting 
algorithm using in-place flips, and a `test_pancake_sort` function containing 
several test cases to validate the functionality.

Tutorial: https://leetcode.com/problems/pancake-sorting/description/comments/1564957

Typical usage example:

    solution = Solution()
    result = solution.pancakeSort([3, 2, 4, 1])
    print(result)  # Output: [4, 2, 4, 3]

Attributes:
    Solution: A class that provides the pancake sorting functionality.
    test_pancake_sort: A function containing test cases to validate the solution.
"""

# Date of Last Practice: Sep 22, 2024 -> Oct 6, 2024
#
# Time Complexity: O(N^2), where N is the length of the input list.
#                  The maximum number of flips required to sort the list is N-1.
#                  For each flip, we need to find the maximum element in the current
#                  segment, which requires O(N) time. Hence, the overall time
#                  complexity is O(N^2).
#
# Space Complexity: O(1), as we are not using any extra space except for the
#                   output list to store the k-values of each flip.


class Solution:
    """Perform pancake sorting on an integer array."""

    def pancakeSort(self, arr: list[int]) -> list[int]:
        """Sorts the array using a series of pancake flips.

        Args:
            arr: List of integers to sort using pancake flips.

        Returns:
            A list of integers representing the k-values of each pancake flip.
        """
        answers = []
        n = len(arr)

        # Start from the last index and move down to the first element.
        for cur_len in range(n, 1, -1):
            # Find the index of the maximum value within the current length.
            max_index = self.find_max_index(arr, cur_len)

            if max_index != cur_len - 1:
                # Flip to move max element to the first position, if not already there.
                if max_index > 0:
                    self.flip(arr, max_index + 1)
                    answers.append(max_index + 1)

                # Flip to move the max element to its correct position.
                self.flip(arr, cur_len)
                answers.append(cur_len)

        return answers

    def find_max_index(self, arr: list[int], length: int) -> int:
        """Finds the index of the maximum element within the given length.

        Args:
            arr: List of integers.
            length: Current segment length of the list to consider.

        Returns:
            Index of the maximum element within the specified range.
        """
        max_index = 0
        for i in range(1, length):
            if arr[i] > arr[max_index]:
                max_index = i
        return max_index

    def flip(self, arr: list[int], k: int) -> None:
        """Reverses the sub-array from the start up to index k-1.

        Args:
            arr: List of integers to be flipped.
            k: Position up to which the list needs to be reversed.
        """
        left, right = 0, k - 1
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1


def test_pancake_sort():
    """Test cases to validate the pancake sorting functionality."""
    solution = Solution()

    # Test case 1: Normal case with unsorted list.
    arr = [3, 2, 4, 1]
    result = solution.pancakeSort(arr)
    assert arr == [1, 2, 3, 4], f"Test 1 Failed: {arr}"
    print(f"Test 1 Passed: {arr} -> {result}")

    # Test case 2: Already sorted list.
    arr = [1, 2, 3]
    result = solution.pancakeSort(arr)
    assert arr == [1, 2, 3], f"Test 2 Failed: {arr}"
    print(f"Test 2 Passed: {arr} -> {result}")

    # Test case 3: Single element list.
    arr = [1]
    result = solution.pancakeSort(arr)
    assert arr == [1], f"Test 3 Failed: {arr}"
    print(f"Test 3 Passed: {arr} -> {result}")

    # Test case 4: Reversed list.
    arr = [5, 4, 3, 2, 1]
    result = solution.pancakeSort(arr)
    assert arr == [1, 2, 3, 4, 5], f"Test 4 Failed: {arr}"
    print(f"Test 4 Passed: {arr} -> {result}")

    # Test case 5: Random list.
    arr = [3, 6, 1, 5, 2, 4]
    result = solution.pancakeSort(arr)
    assert arr == [1, 2, 3, 4, 5, 6], f"Test 5 Failed: {arr}"
    print(f"Test 5 Passed: {arr} -> {result}")


if __name__ == "__main__":
    test_pancake_sort()
