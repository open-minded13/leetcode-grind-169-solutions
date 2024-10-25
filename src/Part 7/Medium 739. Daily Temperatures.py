"""
Solve the 'Daily Temperatures' problem.

This module contains the Solution class, which provides a method to calculate 
the number of days one has to wait for a warmer temperature for each day in the 
input list of daily temperatures.
"""

from typing import List

# Date of Last Practice: Aug 24, 2024
#
# Time Complexity: O(N), where N is the number of temperatures.
#                  For each temperature, we push it onto the stack once and pop it once.
#                  This results in a linear time complexity.
#
# Space Complexity: O(N), where N is the number of temperatures.
#                   The stack can store at most N elements.


class Solution:
    """
    Provides a method to calculate waiting days for a warmer temperature.

    The `dailyTemperatures` method returns a list where each element indicates
    the number of days to wait until a warmer temperature occurs. If no warmer
    temperature is expected, the value will be 0 for that day.
    """

    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        Calculate the number of days until a warmer temperature for each day.

        Args:
            temperatures (List[int]): A list of integers representing daily
                                      temperatures.

        Returns:
            List[int]: A list of integers representing the number of days until
                       a warmer temperature, or 0 if no warmer day exists.
        """
        # Step 1 - Initialize the answer array with zeros and a stack to keep track
        #          of temperatures.
        answer = [0] * len(temperatures)
        pending = []  # Stack to store temperatures and their indices.

        # Step 2 - Iterate through each day's temperature.
        for index, temperature in enumerate(temperatures):
            # Step 3 - Process pending temperatures if the current temperature is
            #          warmer.
            while pending and temperature > pending[-1][0]:
                _, prev_index = pending.pop()
                answer[prev_index] = index - prev_index

            # Step 4 - Append the current temperature and its index to the stack.
            pending.append((temperature, index))

        # Step 5 - Return the result array.
        return answer


def main():
    """
    Main function to demonstrate the usage of the Solution class with test cases.
    """
    solution = Solution()

    # Test case 1
    assert solution.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]) == [
        1,
        1,
        4,
        2,
        1,
        1,
        0,
        0,
    ], "Test case 1 failed"

    # Test case 2
    assert solution.dailyTemperatures([30, 40, 50, 60]) == [
        1,
        1,
        1,
        0,
    ], "Test case 2 failed"

    # Test case 3
    assert solution.dailyTemperatures([30, 60, 90]) == [1, 1, 0], "Test case 3 failed"

    # Test case 4: Edge case with no warmer days
    assert solution.dailyTemperatures([100, 100, 100]) == [
        0,
        0,
        0,
    ], "Test case 4 failed"

    print("All test cases passed!")


if __name__ == "__main__":
    main()
