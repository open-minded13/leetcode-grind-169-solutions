"""
Reverse the bits of a 32-bit unsigned integer with memoization.

This module defines a class with methods to reverse the bits of a 32-bit
unsigned integer. It includes both a basic implementation and an optimized 
version using memoization for repeated calls.

Example usage:
    solution = Solution()
    result_basic = solution.reverseBits(43261596)
    result_memoized = solution.reverseBitsMemoized(43261596)
"""

# Date of Last Practice: Aug 28, 2024
#
# Time Complexity: O(1), since the input is a 32-bit unsigned integer. We iterate over
#                  32 bits to reverse them.
#
# Space Complexity: O(1), as we use a constant amount of extra space.
#
#                   O(1) only applies to the `reverseBits` method. The `reverseBits`
#                   method uses a constant amount of space.
#
#                   O(2^32) applies to the `reverseBitsMemoized` method in the worst
#                   case as the memoization dictionary could potentially store up to
#                   2^32 entries.


class Solution:
    """Solve the problem of reversing bits in a 32-bit unsigned integer."""

    def __init__(self):
        """Initialize the memoization dictionary."""
        self.memo = {}

    def reverseBits(self, n: int) -> int:
        """
        Reverse the bits of a given 32-bit unsigned integer.

        Args:
            n (int): The 32-bit unsigned integer to reverse.

        Returns:
            int: The integer value of the reversed bits.
        """
        result = 0

        # Reverse the bits.
        for i in range(32):
            result <<= 1
            result |= n & 1
            n >>= 1

        return result

    def reverseBitsMemoized(self, n: int) -> int:
        """
        Reverse the bits of a given 32-bit unsigned integer with memoization.

        Args:
            n (int): The 32-bit unsigned integer to reverse.

        Returns:
            int: The integer value of the reversed bits.
        """
        # Step 1 - Check if result is already computed.
        if n in self.memo:
            return self.memo[n]

        result = 0

        # Step 2 - Reverse the bits.
        for i in range(32):
            result <<= 1
            result |= n & 1
            n >>= 1

        # Step 3 - Store the result in memoization dictionary.
        self.memo[n] = result

        return result


def main():
    """Test the Solution class with sample test cases."""
    solution = Solution()

    # Test cases for basic reverseBits method
    assert (
        solution.reverseBits(0b00000010100101000001111010011100) == 964176192
    ), "Basic Test case 1 failed"
    assert (
        solution.reverseBits(0b11111111111111111111111111111101) == 3221225471
    ), "Basic Test case 2 failed"

    # Test cases for memoized reverseBitsMemoized method
    assert (
        solution.reverseBitsMemoized(0b00000010100101000001111010011100) == 964176192
    ), "Memoized Test case 1 failed"
    assert (
        solution.reverseBitsMemoized(0b11111111111111111111111111111101) == 3221225471
    ), "Memoized Test case 2 failed"

    # Additional test cases to check memoization
    assert (
        solution.reverseBitsMemoized(0b00000010100101000001111010011100) == 964176192
    ), "Memoized Test case 3 failed"
    assert (
        solution.reverseBitsMemoized(0b11111111111111111111111111111101) == 3221225471
    ), "Memoized Test case 4 failed"

    print("All test cases passed!")


if __name__ == "__main__":
    main()
