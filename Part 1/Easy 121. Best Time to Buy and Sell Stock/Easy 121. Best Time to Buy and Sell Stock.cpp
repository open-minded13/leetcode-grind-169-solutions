// Complexity
// Time complexity: O(N);
// Space Complexity: O(1);
// The algorithm only uses a constant amount of extra space to
// store the maximum profit and the minimum price seen so far.
// This means that the amount of memory used by the algorithm
// does not depend on the size of the input array.

#include <iostream>
#include <vector>
using namespace std;

class Solution
{
public:
    int maxProfit(vector<int> &prices)
    {
        int max_profit = 0;
        int min_price = INT_MAX;
        for (int i = 0; i < prices.size(); i++)
        {
            if (prices[i] < min_price)
            {
                min_price = prices[i];
            }
            int net_profit = prices[i] - min_price;
            if (net_profit > max_profit)
            {
                max_profit = net_profit;
            }
        }
        return max_profit;
    }
};

int main()
{
    // Create an instance of the Solution class
    Solution s;

    // Define the input array of stock prices
    vector<int> prices = {7, 1, 5, 3, 6, 4};

    // Call the maxProfit method and print the result
    int max_profit = s.maxProfit(prices);
    cout << "The maximum profit is: " << max_profit << endl;

    return 0;
}
