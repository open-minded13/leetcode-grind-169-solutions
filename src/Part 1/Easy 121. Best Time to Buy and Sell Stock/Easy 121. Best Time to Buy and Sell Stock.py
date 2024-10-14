"""
Find the maximum profit from stock prices.

This module defines a class with a method to compute the maximum profit
that can be achieved by buying and selling stocks on different days.
"""

# Date of Last Practice: Apr 12, 2023 -> Jun 11, 2023 -> Jan 27, 2024 -> Oct 12, 2024
#
# Time Complexity: O(N), where N is the length of the input array prices.
#                  This is because the algorithm iterates over the array once in a loop.
#                  Each iteration performs constant time operations, such as comparisons
#                  and arithmetic calculations.
#
# Space Complexity: O(1). The algorithm only uses a constant amount of extra space to
#                   store the maximum profit and the minimum price seen so far.
#                   Regardless of the size of the input array, the amount of memory
#                   used by the algorithm remains the same.


class Solution:
    """Class to compute the maximum profit from a list of stock prices."""

    def maxProfit(self, prices):
        """Calculate the maximum profit from stock prices.

        Args:
            prices (List[int]): List of stock prices, where prices[i]
                                is the price of the stock on day i.

        Returns:
            int: Maximum profit that can be achieved. If no profit is possible,
                 returns 0.
        """
        # Step 1 - Initialize variables
        max_profit = 0  # To store the maximum profit
        min_price = float("inf")  # To store the minimum price seen so far

        # Step 2 - Loop through all stock prices
        for price in prices:
            # Step 3 - Update the minimum price if the current price is lower
            if price < min_price:
                min_price = price

            # Step 4 - Calculate the potential profit
            potential_profit = price - min_price

            # Step 5 - Update max profit if the current potential profit is higher
            if potential_profit > max_profit:
                max_profit = potential_profit

        # Step 6 - Return the maximum profit found
        return max_profit


if __name__ == "__main__":
    s = Solution()

    # Test case 1: Normal case with profit
    prices1 = [7, 1, 5, 3, 6, 4]
    assert s.maxProfit(prices1) == 5  # Buy at 1, sell at 6

    # Test case 2: No profit possible
    prices2 = [7, 6, 4, 3, 1]
    assert s.maxProfit(prices2) == 0  # Prices only decrease, no profit

    # Test case 3: Single price (no transaction possible)
    prices3 = [5]
    assert s.maxProfit(prices3) == 0  # Only one price, no transaction

    # Test case 4: Increasing prices
    prices4 = [1, 2, 3, 4, 5]
    assert s.maxProfit(prices4) == 4  # Buy at 1, sell at 5

    # Test case 5: Decreasing and then increasing prices
    prices5 = [7, 6, 4, 3, 5, 6, 2, 8]
    assert s.maxProfit(prices5) == 6  # Buy at 2, sell at 8

    print("All test cases passed!")
