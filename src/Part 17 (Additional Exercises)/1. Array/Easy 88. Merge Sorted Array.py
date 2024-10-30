"""
Merge two sorted integer arrays into a single sorted array in-place.

This module provides a class with a method to merge two sorted arrays where the
merged result is stored in the first array (nums1). The solution operates in 
O(M + N) time complexity, modifying nums1 in-place without extra space.
"""

from typing import List

# Date of Last Practice: Oct 29, 2024
#
# Time Complexity: O(M + N), where M and N are the number of valid elements in nums1
#                  and nums2, respectively.
#
# Space Complexity: O(1), as the solution operates in-place without using extra space.


class Solution:
    """
    Handles in-place merging of two sorted integer arrays.
    """

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Merge two sorted arrays, nums1 and nums2, into nums1 in non-decreasing order.

        Args:
            nums1 (List[int]): First sorted array with extra space at the end.
            m (int): Number of valid elements in nums1.
            nums2 (List[int]): Second sorted array.
            n (int): Number of valid elements in nums2.

        Returns:
            None: Modifies nums1 in-place.
        """
        # Step 1 - Set pointers for nums1, nums2, and the end of merged array
        p1, p2, p_merge = m - 1, n - 1, m + n - 1

        # Step 2 - Merge in reverse order to avoid overwriting nums1's elements
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p_merge] = nums1[p1]
                p1 -= 1
            else:
                nums1[p_merge] = nums2[p2]
                p2 -= 1
            p_merge -= 1

        # Step 3 - If there are remaining elements in nums2, copy them to nums1
        nums1[: p2 + 1] = nums2[: p2 + 1]


def main():
    """
    Main function to demonstrate the merge method with test cases.
    """
    solution = Solution()

    # Test case 1
    nums1 = [1, 2, 3, 0, 0, 0]
    nums2 = [2, 5, 6]
    solution.merge(nums1, 3, nums2, 3)
    assert nums1 == [1, 2, 2, 3, 5, 6], f"Test case 1 failed: {nums1}"

    # Test case 2
    nums1 = [1]
    nums2 = []
    solution.merge(nums1, 1, nums2, 0)
    assert nums1 == [1], f"Test case 2 failed: {nums1}"

    # Test case 3
    nums1 = [0]
    nums2 = [1]
    solution.merge(nums1, 0, nums2, 1)
    assert nums1 == [1], f"Test case 3 failed: {nums1}"

    print("All test cases passed.")


if __name__ == "__main__":
    main()
