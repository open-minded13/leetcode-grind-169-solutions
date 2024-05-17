// Date of Last Practice: Mar 17, 2024
// 
// Time Complexity: O(N), where N is the length of the input array prices.
//                  This is because the algorithm iterates over the array once in a loop.
//                  Each iteration performs constant time operations,
//                  such as comparisons and arithmetic calculations.
// 
// Space Complexity: O(1). The algorithm only uses a constant amount of extra space
//                   to store the maximum profit and the minimum price seen so far.
//                   Regardless of the size of the input array, the amount of memory
//                   used by the algorithm remains the same.

var maxProfit = function (prices) {
    if (!Array.isArray(prices)) throw new Error('Input must be an array');
    if (prices.some(price => typeof price !== 'number' || price < 0 || !isFinite(price))) {
        throw new Error('Invalid price value');
    }

    let minPrice = Infinity
    let maxProfit = 0

    for (let i = 0; i < prices.length; i++) {
        const curPrice = prices[i]
        minPrice = (curPrice <= minPrice) ? curPrice : minPrice
        if (curPrice - minPrice > maxProfit) {
            maxProfit = curPrice - minPrice
        }
    }

    return maxProfit
};

module.exports = maxProfit