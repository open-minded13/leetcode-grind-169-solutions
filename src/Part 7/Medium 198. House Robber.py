"""
Module to solve the House Robber problem using various dynamic programming approaches.

This module provides an object-oriented solution to the problem where a robber
must maximize the money robbed from houses without robbing two adjacent houses.
Multiple methods are implemented, showcasing the evolution of the solution from
a naive recursive approach to an optimized iterative approach.

Four Approaches:
    1. Recursive Top-Down: `recursive_top_down`
    2. Recursive Top-Down with Memoization: `recursive_memo_top_down`
    3. Iterative Bottom-Up with Memoization: `iterative_memo_bottom_up`
    4. Optimized Iterative Bottom-Up with Two Variables: `iterative_two_vars_bottom_up`
"""

from typing import List

# Date of Last Practice: Aug 20, 2024
#
# Time Complexity: O(N), where N is the number of houses.
#
# Space Complexity: O(1), since we are using only two variables.


class Solution:
    """
    Solve the House Robber problem using various approaches.

    Check the tutorial: https://leetcode.com/problems/house-robber/solutions/156523/
                        From-good-to-great.-How-to-approach-most-of-DP-problems

    Methods:
        rob: Calls the iterative_two_vars_bottom_up method, which is the most optimized.

        find_recursive_relation: A naive recursive method to find the maximum amount of
                                 money, which is used by the recursive_top_down method.

        recursive_top_down: A top-down recursive solution to the House Robber problem.

        recursive_memo_top_down: A top-down recursive solution with memoization.

        iterative_memo_bottom_up: An iterative bottom-up solution with memoization.

        iterative_two_vars_bottom_up: An optimized bottom-up solution using two
                                      variables.
    """

    def rob(self, nums: List[int]) -> int:
        """
        The most optimized solution to the House Robber problem, using two variables.

        Args:
            nums: A list of integers representing the amount of money at each house.

        Returns:
            The maximum amount of money that can be robbed.
        """
        return self.iterative_two_vars_bottom_up(nums)

    def find_recursive_relation(self, nums: List[int], i: int) -> int:
        """
        A naive recursive method to find the maximum amount of money that can be robbed.

        Args:
            nums: A list of integers representing the amount of money at each house.
            i: The current index in the list.

        Returns:
            The maximum amount of money that can be robbed up to index i.
        """
        if i < 0:
            return 0
        return max(
            self.find_recursive_relation(nums, i - 2) + nums[i],
            self.find_recursive_relation(nums, i - 1),
        )

    def recursive_top_down(self, nums: List[int]) -> int:
        """
        A top-down recursive solution to the House Robber problem.

        Time Complexity: O(2^N), where N is the number of houses. This is because at
                         each house, we have two choices: either rob the house or skip
                         it. This leads to an exponential number of recursive calls.

        Space Complexity: O(N), where N is the number of houses.

        Args:
            nums: A list of integers representing the amount of money at each house.

        Returns:
            The maximum amount of money that can be robbed.
        """
        return self.find_recursive_relation(nums, len(nums) - 1)

    def recursive_memo_top_down(self, nums: List[int]) -> int:
        """
        A top-down recursive solution with memoization to the House Robber problem.

        Time Complexity: O(N), where N is the number of houses. This is because we
                         memoize the results of the subproblems, which prevents
                         redundant calculations and reduces the time complexity.

        Space Complexity: O(N), where N is the number of houses.

        Args:
            nums: A list of integers representing the amount of money at each house.

        Returns:
            The maximum amount of money that can be robbed.
        """
        memo = [-1] * len(nums)

        def helper(i: int) -> int:
            if i < 0:
                return 0
            if memo[i] >= 0:
                return memo[i]
            memo[i] = max(helper(i - 2) + nums[i], helper(i - 1))
            return memo[i]

        return helper(len(nums) - 1)

    def iterative_memo_bottom_up(self, nums: List[int]) -> int:
        """
        An iterative bottom-up solution with memoization to the House Robber problem.

        Time Complexity: O(N), where N is the number of houses. This is because we
                         iterate through the list of houses once to calculate the
                         maximum amount of money that can be robbed.

        Space Complexity: O(N), where N is the number of houses.

        Args:
            nums: A list of integers representing the amount of money at each house.

        Returns:
            The maximum amount of money that can be robbed.
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        memo = [0] * (len(nums) + 1)
        memo[0] = 0
        memo[1] = nums[0]

        for i in range(1, len(nums)):
            memo[i + 1] = max(memo[i], memo[i - 1] + nums[i])

        return memo[len(nums)]

    def iterative_two_vars_bottom_up(self, nums: List[int]) -> int:
        """
        An optimized bottom-up solution using two variables to solve the problem.

        Time Complexity: O(N), where N is the number of houses. This is because we
                         iterate through the list of houses once to calculate the
                         maximum amount of money that can be robbed.

        Space Complexity: O(1), since we are using only two variables.

        Args:
            nums: A list of integers representing the amount of money at each house.

        Returns:
            The maximum amount of money that can be robbed.
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        prev1 = 0
        prev2 = 0

        for num in nums:
            temp = prev1
            prev1 = max(prev2 + num, prev1)
            prev2 = temp

        return prev1


def main():
    """
    Main function to demonstrate the usage of the Solution class and its methods.
    """
    solution = Solution()

    # Test cases
    nums1 = [1, 2, 3, 1]
    nums2 = [2, 7, 9, 3, 1]

    assert solution.rob(nums1) == 4, f"Test case 1 failed: {solution.rob(nums1)}"
    assert solution.rob(nums2) == 12, f"Test case 2 failed: {solution.rob(nums2)}"

    print("All test cases passed.")


if __name__ == "__main__":
    main()
