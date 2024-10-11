"""
Solve the problem of moving all zeroes in a list to the end while preserving 
the order of non-zero elements.
"""

from typing import List

# Date of Last Practice: Sep 10, 2024
#
# Time Complexity: O(N), where N is the number of elements in the input list nums.
#
# Space Complexity: O(1), as the function uses a constant amount of extra space.


class Solution:
    """Provides functionality to move zeroes to the end of a list."""

    def moveZeroes(self, nums: List[int]) -> None:
        """
        Move all zeroes in the list to the end while maintaining the order of
        non-zero elements.

        Args:
            nums: List of integers where some elements may be zero.
        """
        # Step 1 - Initialize a pointer for tracking non-zero positions.
        non_zero_index = 0

        # Step 2 - Iterate over the list, moving non-zero elements to the
        #          front of the list.
        for i, _ in enumerate(nums):
            if nums[i] != 0:
                # Step 3 - Place the non-zero element at the non_zero_index
                #          and increment the pointer.
                nums[non_zero_index] = nums[i]
                non_zero_index += 1

        # Step 4 - Fill the remaining positions with zeroes.
        for i in range(non_zero_index, len(nums)):
            nums[i] = 0


def test_moveZeroes():
    """Test cases for moveZeroes."""

    # Test case 1: Mixed zeroes and non-zero elements.
    nums1 = [0, 1, 0, 3, 12]
    Solution().moveZeroes(nums1)
    assert nums1 == [1, 3, 12, 0, 0], f"Failed on {nums1}"

    # Test case 2: Single zero element.
    nums2 = [0]
    Solution().moveZeroes(nums2)
    assert nums2 == [0], f"Failed on {nums2}"

    # Test case 3: No zero elements.
    nums3 = [1, 2, 3, 4, 5]
    Solution().moveZeroes(nums3)
    assert nums3 == [1, 2, 3, 4, 5], f"Failed on {nums3}"

    # Test case 4: All zeroes.
    nums4 = [0, 0, 0]
    Solution().moveZeroes(nums4)
    assert nums4 == [0, 0, 0], f"Failed on {nums4}"

    # Test case 5: Already sorted with zeroes at the end.
    nums5 = [1, 2, 3, 0, 0]
    Solution().moveZeroes(nums5)
    assert nums5 == [1, 2, 3, 0, 0], f"Failed on {nums5}"


# Run the tests
if __name__ == "__main__":
    test_moveZeroes()
    print("All tests passed.")
