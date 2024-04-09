# Date of Last Practice: Apr 12, 2023 -> Jun 11, 2023 -> Jan 27, 2024
#
# Time Complexity: O(N), where N is the length of the input array prices.
#                  This is because the algorithm iterates over the array once in a loop.
#                  Each iteration performs constant time operations, such as comparisons and arithmetic calculations.
#
# Space Complexity: O(1). The algorithm only uses a constant amount of extra space
#                   to store the maximum profit and the minimum price seen so far.
#                   Regardless of the size of the input array, the amount of memory used by the algorithm remains the same.


class Solution:
    def maxProfit(self, prices):
        max_profit = 0

        # In Python, using float('inf') and -float('inf') instead of an integer value
        # like INT_MAX and INT_MIN is a common approach to represent
        # positive and negative infinity, respectively.
        min_price = float("inf")
        for price in prices:
            if price < min_price:
                min_price = price
            net_profit = price - min_price
            if net_profit > max_profit:
                max_profit = net_profit
        return max_profit


# Create an instance of the Solution class
s = Solution()

# Define the input array of the stock prices
prices = [7, 1, 5, 3, 6, 4, 20]

# Call the maxProfit method and print the result
max_profit = s.maxProfit(prices)
print("The maximum profit is:", max_profit)
