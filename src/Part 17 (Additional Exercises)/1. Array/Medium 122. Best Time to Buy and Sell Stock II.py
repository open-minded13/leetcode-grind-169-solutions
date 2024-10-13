"""
Calculate the maximum profit from stock prices.

We are given stock prices for consecutive days. We want to buy stocks when
the price is going up and ignore the days when the price is going down.

Hint: We want to buy all the stocks when the line is going up and ignore
all the lines when the line is going down. Perform a loop through the array,
and only count the increasing segments, comparing two adjacent elements.
"""

from typing import List

# Date of Last Practice: Oct 13, 2024
#
# Time Complexity: O(N), where N is the number of stock prices in the list.
#                  The algorithm iterates through the list of prices once.
#
# Space Complexity: O(1). The algorithm uses a constant amount of extra space
#                   regardless of the size of the input list.


class Solution:
    """Calculate the maximum profit for stock trading."""

    def maxProfit(self, prices: List[int]) -> int:
        """
        Calculate the maximum profit from stock price changes.

        Args:
            prices: List of stock prices, where prices[i] is the price on day i.

        Returns:
            The maximum profit that can be made by buying and selling stocks.
        """
        max_profit = 0  # Initialize the maximum profit.

        # Step 1 - Iterate through the price list from day 1 to the last day.
        for today in range(1, len(prices)):
            # Step 2 - If today's price is higher than yesterday's, add the
            #          difference to the profit.
            profit_delta = prices[today] - prices[today - 1]
            if profit_delta > 0:
                max_profit += profit_delta

        return max_profit


def test_maxProfit():
    """Test cases to validate the maxProfit function."""
    solution = Solution()

    # Test case 1 - Prices fluctuate, multiple buy-sell opportunities.
    prices = [7, 1, 5, 3, 6, 4]
    assert solution.maxProfit(prices) == 7, "Test case 1 failed"

    # Test case 2 - Prices continuously rise, one buy-sell opportunity.
    prices = [1, 2, 3, 4, 5]
    assert solution.maxProfit(prices) == 4, "Test case 2 failed"

    # Test case 3 - Prices continuously fall, no buy-sell opportunities.
    prices = [7, 6, 4, 3, 1]
    assert solution.maxProfit(prices) == 0, "Test case 3 failed"

    # Test case 4 - Single day, no transactions possible.
    prices = [5]
    assert solution.maxProfit(prices) == 0, "Test case 4 failed"

    # Test case 5 - Empty prices list, no transactions possible.
    prices = []
    assert solution.maxProfit(prices) == 0, "Test case 5 failed"

    print("All test cases passed!")


if __name__ == "__main__":
    test_maxProfit()
