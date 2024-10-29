"""
Solve the Longest Increasing Subsequence problem.

This module contains a class `Solution` with two methods:
- `lengthOfLIS_DP`: A beginner-friendly dynamic programming approach to find 
  the longest increasing subsequence.
- `lengthOfLIS`: An optimized solution using dynamic programming with binary 
  search for improved time complexity.
"""

from typing import List
import bisect

# Date of Last Practice: Aug 11, 2024 -> Oct 29, 2024
#
# Time Complexity: O(N * log(N)), where N is the number of elements in the given list.
#                  The time complexity is dominated by the binary search operation
#                  inside the loop that iterates through the elements of the list.
#                  This only applies to the lengthOfLIS method.
#
#                  The lengthOfLIS_DP method has a time complexity of O(N^2) due to
#                  the nested loop that iterates through the elements of the list.
#
# Space Complexity: O(N), where N is the number of elements in the given list.
#                   The space complexity is due to the list `subsequence_tails` that
#                   stores the smallest tail of increasing subsequences.


class Solution:
    """
    A class to represent solutions for finding the longest increasing subsequence.

    This class provides two methods:
    - `lengthOfLIS_DP`: Dynamic programming approach for beginners to understand the
                        LIS problem.
    - `lengthOfLIS`: Optimized solution using dynamic programming with binary search.
    """

    def lengthOfLIS_DP(self, nums: List[int]) -> int:
        """
        Beginner-friendly approach using dynamic programming to find the LIS.

        Check: https://www.youtube.com/watch?v=4fQJGoeW5VE

        Args:
            nums (List[int]): A list of integers.

        Returns:
            int: The length of the longest increasing subsequence.
        """
        if not nums:
            return 0

        # Step 1 - Initialize sub_lis where each sub_lis[i] stores the LIS
        #          ending at index i
        sub_lis = [
            [] for _ in range(len(nums))
        ]  # sub_lis[i] holds the LIS ending at nums[i]
        sub_lis[0].append(nums[0])

        # Step 2 - Fill sub_lis based on previous subsequences
        for i in range(1, len(nums)):
            cur_num = nums[i]

            # Step 3 - Find the longest increasing subsequence ending before the
            #          current index
            for j in range(i):
                if sub_lis[j][-1] < cur_num and len(sub_lis[j]) >= len(sub_lis[i]):
                    sub_lis[i] = list(sub_lis[j])

            # Step 4 - Append the current number to extend the subsequence
            sub_lis[i].append(cur_num)

        # Step 5 - Return the length of the longest subsequence found
        return max(len(lis) for lis in sub_lis)

    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        Optimized approach using dynamic programming with binary search to find the LIS.

        Args:
            nums (List[int]): A list of integers.

        Returns:
            int: The length of the longest increasing subsequence.
        """
        if not nums:
            return 0

        # Step 1 - Initialize an empty list to store the longest increasing subsequence
        #          so far
        longest_increasing_subsequence = []

        # Step 2 - Iterate through the given list of integers
        for num in nums:
            # Step 3 - Use binary search to find the position where `num` can replace
            #          an element
            index = bisect.bisect_left(longest_increasing_subsequence, num)

            # Step 4 - If the index is equal to the length of the list, append the
            #          number
            if index == len(longest_increasing_subsequence):
                longest_increasing_subsequence.append(num)
            else:
                # Step 5 - Otherwise, replace the element at the found index
                longest_increasing_subsequence[index] = num

        # Step 6 - The length of longest_increasing_subsequence is the length of the LIS
        return len(longest_increasing_subsequence)


def main():
    """
    Demonstrate the usage of the Solution class.
    """
    solution = Solution()

    # Test cases with assertions for lengthOfLIS_DP method
    assert (
        solution.lengthOfLIS_DP([10, 9, 2, 5, 3, 7, 101, 18]) == 4
    ), "Test case 1 failed for DP"
    assert solution.lengthOfLIS_DP([0, 1, 0, 3, 2, 3]) == 4, "Test case 2 failed for DP"
    assert (
        solution.lengthOfLIS_DP([7, 7, 7, 7, 7, 7, 7]) == 1
    ), "Test case 3 failed for DP"
    assert (
        solution.lengthOfLIS_DP([4, 10, 4, 3, 8, 9]) == 3
    ), "Test case 4 failed for DP"

    # Test cases with assertions for lengthOfLIS method
    assert (
        solution.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]) == 4
    ), "Test case 1 failed for bisect"
    assert (
        solution.lengthOfLIS([0, 1, 0, 3, 2, 3]) == 4
    ), "Test case 2 failed for bisect"
    assert (
        solution.lengthOfLIS([7, 7, 7, 7, 7, 7, 7]) == 1
    ), "Test case 3 failed for bisect"
    assert (
        solution.lengthOfLIS([4, 10, 4, 3, 8, 9]) == 3
    ), "Test case 4 failed for bisect"

    print("All test cases passed!")


if __name__ == "__main__":
    main()
