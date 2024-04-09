from typing import List

# Date of Last Practice: Dec 20, 2023 -> Feb 8, 2024
#
# Time Complexity: O(N*M), where N is the number of coins and M is the number of
#                  the amount variable.
#
#                  Outer Loop (Coins Loop): This loop iterates over each coin in the coins array.
#                  If there are n coins, this loop runs n times.
#
#                  Inner Loop (Amount Loop): For each coin, the inner loop iterates through
#                  all the amounts from the coin value up to the desired amount.
#                  If the amount we are trying to make is M, this loop runs M times for each coin.
#
#                  In the worst-case scenario (where coins = [1, 2, 3, ..., M]),
#                  the number of iterations for the inner loop can be summed up as follows:
#
#                  For coin 1: Iterates M times
#                  For coin 2: Iterates M - 1 times
#                  For coin 3: Iterates M - 2 times
#                  ...
#                  For coin m: Iterates 1 time
#
#                  So, the total number of iterations in the worst-case scenario is
#                  the sum of the first m natural numbers, which is M * (M+1) / 2.
#                  This sum is in the order of O(M^2).
#
# Space Complexity: O(M), where M is the number of the amount variable.
#                   We create a one-dimensional array of size M + 1 (including amount 0 to M).
#                   This array is used to store the minimum number of coins needed for each amount.


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        max_coin_required = amount
        dp = [max_coin_required + 1] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)

        if dp[amount] == max_coin_required + 1:
            return -1
        else:
            return dp[amount]


# Test cases
sol = Solution()

# Test case 1
print("Test Case 1")
coins = [1, 2, 5]
amount = 11
print("Input:", coins, amount)
print("Output:", sol.coinChange(coins, amount))  # Expected output: 3

# Test case 2
print("\nTest Case 2")
coins = [2]
amount = 3
print("Input:", coins, amount)
print("Output:", sol.coinChange(coins, amount))  # Expected output: -1

# Test case 3
print("\nTest Case 3")
coins = [1]
amount = 0
print("Input:", coins, amount)
print("Output:", sol.coinChange(coins, amount))  # Expected output: 0
