"""
Detect cycles in a circular array using an optimized approach.

This module contains the Solution class, which provides a method to determine
if there exists a cycle with a consistent direction in a given array.
"""

from typing import List

# Date of Last Practice: Aug 15, 2024
#
# Time Complexity: O(N), where N is the number of elements in the array.
#                  The time complexity is O(N) because we traverse each element
#                  in the array at most once. We mark the visited elements as 0
#                  to avoid reprocessing them.
#
# Space Complexity: O(1), as we use a constant amount of extra space.


class Solution:
    """
    Checks for cycles in a circular array with consistent direction.

    This class provides the circularArrayLoop method to determine if a circular
    array contains a cycle with all elements moving in the same direction.
    """

    def circularArrayLoop(self, nums: List[int]) -> bool:
        """
        Determine if the array contains a cycle with consistent direction.

        Args:
            nums: List[int]. A circular array where each element indicates the
                  steps to move forward or backward.

        Returns:
            bool: True if there exists a cycle in the array with consistent direction,
                  otherwise False.
        """
        if len(nums) <= 1:
            return False

        def next_index(index):
            """
            Calculate the next index to move to in the circular array.

            Args:
                index: int. The current index.

            Returns:
                int: The next index after moving according to nums[index].
            """
            return (index + nums[index]) % len(nums)

        for start_index in range(len(nums)):
            if nums[start_index] == 0:
                continue

            slow, fast = start_index, next_index(start_index)
            direction = (
                nums[start_index] > 0
            )  # Determine the direction (True for positive)

            # Traverse the array following the direction
            while (
                nums[fast] != 0
                and (nums[fast] > 0) == direction
                and (nums[next_index(fast)] > 0) == direction
            ):
                slow = next_index(slow)
                fast = next_index(next_index(fast))

                if slow == fast:
                    # Check if the loop is not a single-element loop
                    if slow == next_index(slow):
                        break
                    return True

            # Mark the visited elements as 0 to avoid reprocessing
            current = start_index
            while nums[current] != 0 and (nums[current] > 0) == direction:
                temp = next_index(current)
                nums[current] = 0
                current = temp

        return False


# Test cases
def main():
    """
    Test the Solution class and its circularArrayLoop method.

    Uses assert statements to validate the correctness of the solution.
    """
    solution = Solution()

    # Test case 1: Standard cycle exists
    nums1 = [2, -1, 1, 2, 2]
    assert solution.circularArrayLoop(nums1) == True, "Test case 1 failed"

    # Test case 2: No valid cycle (single element cycle)
    nums2 = [-1, -2, -3, -4, -5, 6]
    assert solution.circularArrayLoop(nums2) == False, "Test case 2 failed"

    # Test case 3: Mixed direction, no valid cycle
    nums3 = [1, -1, 5, 1, 4]
    assert solution.circularArrayLoop(nums3) == True, "Test case 3 failed"

    # Test case 4: No cycle, element looping to itself
    nums4 = [-2, 1, -1, -2, -2]
    assert solution.circularArrayLoop(nums4) == False, "Test case 4 failed"

    # Additional Test case 5: Large jump in a small array
    nums5 = [3, 1, 2]
    assert solution.circularArrayLoop(nums5) == True, "Test case 5 failed"

    print("All test cases passed!")


if __name__ == "__main__":
    main()
