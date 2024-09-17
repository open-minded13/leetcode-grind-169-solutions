import math

# Date of Last Practice: Mar 17, 2024
#
# Time Complexity: O(log N), where N is the power n.
#                  This efficiency is due to the way the algorithm halves the power n
#                  in each iteration of the loop when n is even.
#                  By squaring the base x and halving n, the number of operations required
#                  grows logarithmically with respect to n.
#
# Space Complexity: O(1). It uses a constant amount of extra space
#                   regardless of the input size, since all operations are done in place
#                   and only a fixed number of variables (answer, power_number, x, and n) are used.


class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Base cases: x^0 = 1, and 0^n = 0 for n > 0
        if x == 0:
            return 0
        elif n == 0:
            return 1
        # Handle negative powers
        elif n < 0:
            x = 1 / x
            n = -n

        answer = 1
        while n > 0:
            # If n is odd, multiply answer by x
            if n % 2 == 1:
                answer *= x
            # Square x and halve n for efficient power calculation
            x *= x
            n //= 2

        return answer


# Create an instance of the Solution class
sol = Solution()

# Test cases with a tolerance for floating point arithmetic
epsilon = 1e-9  # Tolerance level
assert math.isclose(sol.myPow(2.00000, 10), 1024.00000, rel_tol=epsilon)
assert math.isclose(sol.myPow(2.10000, 3), 9.26100, rel_tol=epsilon)
assert math.isclose(sol.myPow(2.00000, -2), 0.25000, rel_tol=epsilon)
assert math.isclose(sol.myPow(0, 1), 0, rel_tol=epsilon)
assert sol.myPow(0, 0) == 1  # Exact comparison for non-floating point numbers
assert sol.myPow(1, 0) == 1  # Exact comparison for non-floating point numbers

# Add more test cases as needed
print("All test cases passed successfully!")
