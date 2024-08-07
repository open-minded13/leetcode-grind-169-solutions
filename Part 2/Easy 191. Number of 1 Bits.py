"""
Count the number of set bits (1s) in the binary representation of a positive integer.

This module defines a class with three methods to solve the problem using different
approaches: modulo method, bin() method, and bitwise shift method.

Typical usage example:

1. Create an instance of the Solution class.
2. Call one of the methods with a positive integer.
"""

# Date of Last Practice: Aug 7, 2024
#
# Time Complexity: O(1), as n has a constraint of 32 bits.
#                  Generally, the time complexity is O(log N), where N is the input
#                  integer. However, since the input integer is constrained to 32 bits,
#                  the time complexity is O(1).
#
# Space Complexity: O(1), as no extra space is used.


class Solution:
    """
    A class to count the number of set bits in the binary representation of an integer.
    """

    def hammingWeight(self, n: int) -> int:
        """
        Counts the number of set bits using the modulo method.

        Args:
            n: A positive integer.

        Returns:
            The number of set bits in the binary representation of n.
        """
        counter = 0
        while n != 0:
            counter += n % 2
            n = n // 2
        return counter

    def bin_method(self, n: int) -> int:
        """
        Counts the number of set bits using Python's bin() function.

        Args:
            n: A positive integer.

        Returns:
            The number of set bits in the binary representation of n.
        """
        return bin(n).count("1")

    def bitwise_shift_method(self, n: int) -> int:
        """
        Counts the number of set bits using bitwise shift operations.

        Args:
            n: A positive integer.

        Returns:
            The number of set bits in the binary representation of n.
        """
        counter = 0
        while n:
            counter += n & 1
            n >>= 1
        return counter


def main():
    """
    Main function to demonstrate the usage of the Solution class and its methods.
    """
    hamming_weight = Solution()

    # Test cases with assert statements
    assert hamming_weight.hammingWeight(11) == 3
    assert hamming_weight.hammingWeight(128) == 1
    assert hamming_weight.hammingWeight(2147483645) == 30

    assert hamming_weight.bin_method(11) == 3
    assert hamming_weight.bin_method(128) == 1
    assert hamming_weight.bin_method(2147483645) == 30

    assert hamming_weight.bitwise_shift_method(11) == 3
    assert hamming_weight.bitwise_shift_method(128) == 1
    assert hamming_weight.bitwise_shift_method(2147483645) == 30

    print("All test cases passed!")


if __name__ == "__main__":
    main()
