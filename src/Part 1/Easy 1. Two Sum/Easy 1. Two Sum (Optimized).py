"""Find two indices of numbers in a list that add up to a specific target."""

from typing import List

# Date of Last Practice: Jun 11, 2023 -> Jan 21, 2024 -> Sep 18, 2024
#
# Time complexity: O(N), where N is the length of nums.
#                  Overall, the time complexity of this solution is O(n)
#                  since it only iterates over the input list once.
#
# Space Complexity: O(N), where N is the length of nums.
#                   The dictionary mp can store up to all elements of the input vector.


class Solution:
    """Provides a method to find two indices that sum up to a target value."""

    def two_sum(self, nums: List[int], target: int) -> List[int]:
        """Return indices of the two numbers such that they add up to target.

        Args:
            nums: A list of integers.
            target: The target sum to find.

        Returns:
            A list containing the indices of the two numbers adding up to target.
            If no such pair exists, returns [-1, -1].
        """
        # Initialize a dictionary to store number and its corresponding index
        mp = {}

        # Iterate over the list of numbers
        for i, num in enumerate(nums):
            # Check if the complement exists in the dictionary
            if target - num in mp:
                # Return the indices of the two numbers
                return [mp[target - num], i]
            # Store the current number and its index in the dictionary
            mp[num] = i

        # Return [-1, -1] if no such pair is found
        return [-1, -1]


def main() -> None:
    """Main function to demonstrate the usage of the Solution class."""
    # Test cases
    solution = Solution()

    # Test case 1
    nums1 = [2, 7, 11, 15]
    target1 = 9
    assert solution.two_sum(nums1, target1) == [0, 1], "Test case 1 failed"

    # Test case 2
    nums2 = [3, 2, 4]
    target2 = 6
    assert solution.two_sum(nums2, target2) == [1, 2], "Test case 2 failed"

    # Test case 3
    nums3 = [3, 3]
    target3 = 6
    assert solution.two_sum(nums3, target3) == [0, 1], "Test case 3 failed"

    # Test case 4 (no solution)
    nums4 = [1, 2, 3]
    target4 = 7
    assert solution.two_sum(nums4, target4) == [-1, -1], "Test case 4 failed"

    print("All test cases passed!")


if __name__ == "__main__":
    main()
