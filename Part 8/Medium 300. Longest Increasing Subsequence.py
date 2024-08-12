"""
A module to solve the Longest Increasing Subsequence problem.

This module contains a class `Solution` that provides a method to find the 
length of the longest strictly increasing subsequence from a given list of 
integers using dynamic programming and binary search for optimal performance.
"""

import bisect

# Date of Last Practice: Aug 11, 2024
#
# Time Complexity: O(N * log(N)), where N is the number of elements in the given list.
#                  The time complexity is dominated by the binary search operation
#                  inside the loop that iterates through the elements of the list.
#
# Space Complexity: O(N), where N is the number of elements in the given list.
#                   The space complexity is due to the list `subsequence_tails`
#                   that stores the smallest tail of increasing subsequences.


class Solution:
    """
    A class to represent the solution for finding the longest increasing subsequence.

    This class provides a method `lengthOfLIS` to find the length of the longest
    strictly increasing subsequence in a given list of integers.
    """

    def lengthOfLIS(self, nums):
        """
        Find the length of the longest increasing subsequence.

        This method uses dynamic programming combined with binary search to find
        the length of the longest strictly increasing subsequence in the given
        list of integers.

        Args:
            nums (List[int]): A list of integers.

        Returns:
            int: The length of the longest increasing subsequence.
        """
        if not nums:
            return 0

        # Step 1 - Initialize an empty list to store the smallest tail of increasing
        #          subsequences
        subsequence_tails = []

        # Step 2 - Iterate through the given list of integers
        for num in nums:
            # Step 3 - Use binary search to find the position where `num` can replace
            #          an element
            index = bisect.bisect_left(subsequence_tails, num)

            # Step 4 - If the index is equal to the length of the list, append the
            #          number
            if index == len(subsequence_tails):
                subsequence_tails.append(num)
            else:
                # Step 5 - Otherwise, replace the element at the found index
                subsequence_tails[index] = num

        # Step 6 - The length of subsequence_tails is the length of the longest
        #          increasing subsequence
        return len(subsequence_tails)


def main():
    """
    Main function to demonstrate the usage of the Solution class.
    """
    solution = Solution()

    # Test cases with assertions
    assert solution.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]) == 4, "Test case 1 failed"
    assert solution.lengthOfLIS([0, 1, 0, 3, 2, 3]) == 4, "Test case 2 failed"
    assert solution.lengthOfLIS([7, 7, 7, 7, 7, 7, 7]) == 1, "Test case 3 failed"
    assert solution.lengthOfLIS([4, 10, 4, 3, 8, 9]) == 3, "Test case 4 failed"

    print("All test cases passed!")


if __name__ == "__main__":
    main()
