const maxProfit = require("./Easy 121. Best Time to Buy and Sell Stock")

describe('maxProfit', () => {
    // Test Case 1: Empty input array
    test('should handle empty input array', () => {
        const prices = [];
        const expectedProfit = 0;
        expect(maxProfit(prices)).toBe(expectedProfit);
    });

    // Test Case 2: Single-element array
    test('should handle a single-element array', () => {
        const prices = [5];
        const expectedProfit = 0;
        expect(maxProfit(prices)).toBe(expectedProfit);
    });

    // Test Case 3: Infinite price (boundary value)
    test('should throw an error for an input array with Infinity', () => {
        const prices = [10, 20, Infinity, 30];
        expect(() => maxProfit(prices)).toThrow();
    });

    // Test Case 4: Negative prices 
    test('should throw an error for an input array with negative prices', () => {
        const prices = [-10, -1, 2, 5];
        expect(() => maxProfit(prices)).toThrow();
    });

    // Test Case 5: All prices are decreasing
    test('should handle a scenario where prices are decreasing', () => {
        const prices = [100, 90, 80, 70];
        const expectedProfit = 0;
        expect(maxProfit(prices)).toBe(expectedProfit);
    });

    // Test Case 6: Undefined input
    test('should handle undefined input', () => {
        //Added undefined as the function parameter.
        expect(() => maxProfit(undefined)).toThrow();
    });

    // Test Case 7: Null input
    test('should handle null input', () => {
        const prices = null;
        expect(() => maxProfit(prices)).toThrow();
    });

    // Test Case 8: Maximum and minimum values are at the first and last index respectively
    test('should consider profit when min and max prices are at edges', () => {
        const prices = [10, 7, 5, 8, 11, 12];
        const expectedProfit = 7;
        expect(maxProfit(prices)).toBe(expectedProfit);
    });
    // Test Case 9:  Duplicate values
    test('should handle an array with duplicate values', () => {
        const prices = [10, 5, 5, 10, 15, 20];
        const expectedProfit = 15;
        expect(maxProfit(prices)).toBe(expectedProfit);
    });

    // Test Case 10: Large dataset
    test('should handle a large dataset', () => {
        const prices = Array.from({ length: 1000 }, () => Math.floor(Math.random() * 1000));

        // Function to calculate the expected max profit
        const calculateExpectedProfit = (prices) => {
            let minPrice = Infinity;
            let maxProfit = 0;

            for (let i = 0; i < prices.length; i++) {
                const curPrice = prices[i];
                minPrice = Math.min(minPrice, curPrice);
                maxProfit = Math.max(maxProfit, curPrice - minPrice);
            }

            return maxProfit;
        };

        const expectedProfit = calculateExpectedProfit(prices);
        expect(maxProfit(prices)).toBe(expectedProfit);
    });
});