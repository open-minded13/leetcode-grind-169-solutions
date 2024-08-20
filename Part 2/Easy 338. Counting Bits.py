"""
A module to count the number of 1s in the binary representation of integers
from 0 to n.

This module defines two approaches to calculate the number of 1s (bits set
to 1) in the binary representation of each integer from 0 to n. The first
solution uses a logarithmic approach, while the second solution uses a more
optimized dynamic programming approach.

Typical usage example:

solution = Solution()
assert solution.countBits(2) == [0, 1, 1]
assert solution.countBits(5) == [0, 1, 1, 2, 1, 2]
"""

import math
from typing import List

# Date of Last Practice: Aug 20, 2024
#
# Time Complexity: O(N), where N is the number of integers from 0 to n.
#                  This is only for the optimized approach (`countBits`).
#                  The logarithmic approach (`countBits_logarithmic`) has a
#                  time complexity of O(N log N) due to the logarithmic
#                  calculation.
#
# Space Complexity: O(N), where N is the number of integers from 0 to n.


class Solution:
    """
    A class to calculate the number of 1s in binary representation for each
    number from 0 to n using two different methods.

    Methods:
        countBits(n): Returns a list of counts of 1s in the binary
                      representation of numbers from 0 to n using
                      an optimized dynamic programming approach.

        countBits_logarithmic(n): Returns a list of counts of 1s in the binary
                                  representation of numbers from 0 to n using
                                  a logarithmic approach.
    """

    def countBits(self, n: int) -> List[int]:
        """
        Calculate the number of 1s in the binary representation of numbers
        from 0 to n using a dynamic programming approach.

        Args:
            n (int): The upper limit integer.

        Returns:
            List[int]: A list where the ith element is the number of 1s in
                       the binary representation of i.

        Explanation:
            # i: binary  ans[i]    ... ans[i >> 1] + (i & 1),
            #                          where (i & 1) is to check if the number is odd.

            # 0: 0       0
            # 1: 1       1         ... ans[1 >> 1] + (1 & 1) = ans[0] + 1 = 0 + 1 = 1

            # 2: 10      1         ... ans[2 >> 1] + (2 & 1) = ans[1] + 0 = 1 + 0 = 1
            # 3: 11      2         ... ans[3 >> 1] + (3 & 1) = ans[1] + 1 = 1 + 1 = 2

            # 4: 100     1         ... ans[4 >> 1] + (4 & 1) = ans[2] + 0 = 1 + 0 = 1
            # 5: 101     2         ... ans[5 >> 1] + (5 & 1) = ans[2] + 1 = 1 + 1 = 2
            # 6: 110     2         ... ans[6 >> 1] + (6 & 1) = ans[3] + 0 = 2 + 0 = 2
            # 7: 111     3         ... ans[7 >> 1] + (7 & 1) = ans[3] + 1 = 2 + 1 = 3

            # 8: 1000    1         ... ans[8 >> 1] + (8 & 1) = ans[4] + 0 = 1 + 0 = 1
            # 9: 1001    2         ... ans[9 >> 1] + (9 & 1) = ans[4] + 1 = 1 + 1 = 2
            # 10: 1010   2         ... ans[10 >> 1] + (10 & 1) = ans[5] + 0 = 2 + 0 = 2
            # 11: 1011   3         ... ans[11 >> 1] + (11 & 1) = ans[5] + 1 = 2 + 1 = 3
            # 12: 1100   2         ... ans[12 >> 1] + (12 & 1) = ans[6] + 0 = 2 + 0 = 2
            # 13: 1101   3         ... ans[13 >> 1] + (13 & 1) = ans[6] + 1 = 2 + 1 = 3
            # 14: 1110   3         ... ans[14 >> 1] + (14 & 1) = ans[7] + 0 = 3 + 0 = 3
            # 15: 1111   4         ... ans[15 >> 1] + (15 & 1) = ans[7] + 1 = 3 + 1 = 4
        """
        ans = [0] * (n + 1)

        # Step 1 - Loop through all numbers from 1 to n
        for i in range(1, n + 1):
            # Step 2 - Calculate number of 1s by using the previously computed value
            ans[i] = ans[i >> 1] + (i & 1)

        return ans

    def countBits_logarithmic(self, n: int) -> List[int]:
        """
        Calculate the number of 1s in the binary representation of numbers
        from 0 to n using a logarithmic approach.

        Args:
            n (int): The upper limit integer.

        Returns:
            List[int]: A list where the ith element is the number of 1s in
                       the binary representation of i.

        Explanation:
            # distance = int(log(i)) = 0
            # 0: 0       0
            # 1: 1       1         ... ans[(1 - 2^distance)] + 1

            # distance = int(log(i)) = 1
            # 2: 10      1         ... ans[(2 - 2^distance)] + 1
            # 3: 11      2         ... ans[(3 - 2^distance)] + 1

            # distance = int(log(i)) = 1
            # 4: 100     1         ... ans[(4 - 2^distance)] + 1
            # 5: 101     2         ... ans[(5 - 2^distance)] + 1
            # 6: 110     2
            # 7: 111     3

            # distance = int(log(i)) = 3
            # 8: 1000    1
            # 9: 1001    2
            # 10: 1010   2
            # 11: 1011   3
            # 12: 1100   2
            # 13: 1101   3
            # 14: 1110   2
            # 15: 1111   4
        """
        ans = [0]
        for i in range(1, n + 1):
            distance = int(math.log(i, 2))
            ans.append(1 + ans[i - 2**distance])
        return ans


def main():
    """
    Main function to demonstrate the usage of the Solution class with both
    methods.
    """
    solution = Solution()

    # Test cases for logarithmic approach
    assert solution.countBits_logarithmic(2) == [
        0,
        1,
        1,
    ], "Logarithmic Test case 1 failed"
    assert solution.countBits_logarithmic(5) == [
        0,
        1,
        1,
        2,
        1,
        2,
    ], "Logarithmic Test case 2 failed"
    assert solution.countBits_logarithmic(0) == [0], "Logarithmic Test case 3 failed"
    assert solution.countBits_logarithmic(10) == [
        0,
        1,
        1,
        2,
        1,
        2,
        2,
        3,
        1,
        2,
        2,
    ], "Logarithmic Test case 4 failed"

    # Test cases for optimized approach
    assert solution.countBits(2) == [0, 1, 1], "Optimized Test case 1 failed"
    assert solution.countBits(5) == [
        0,
        1,
        1,
        2,
        1,
        2,
    ], "Optimized Test case 2 failed"
    assert solution.countBits(0) == [0], "Optimized Test case 3 failed"
    assert solution.countBits(10) == [
        0,
        1,
        1,
        2,
        1,
        2,
        2,
        3,
        1,
        2,
        2,
    ], "Optimized Test case 4 failed"

    print("All test cases passed!")


if __name__ == "__main__":
    main()
