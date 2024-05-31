const threeSum = require('./Medium 15. 3Sum');

describe('threeSum', () => {
    test('example case 1', () => {
        const nums = [-1, 0, 1, 2, -1, -4];
        const result = threeSum(nums);
        expect(result).toEqual(expect.arrayContaining([[-1, -1, 2], [-1, 0, 1]]));
    });

    test('example case 2', () => {
        const nums = [0, 1, 1];
        const result = threeSum(nums);
        expect(result).toEqual([]);
    });

    test('example case 3', () => {
        const nums = [0, 0, 0];
        const result = threeSum(nums);
        expect(result).toEqual([[0, 0, 0]]);
    });

    // Edge Case 1: Minimum length input with no zero sum triplet
    test('minimum length input with no zero sum triplet', () => {
        const nums = [1, 2, -2];
        const result = threeSum(nums);
        expect(result).toEqual([]);
    });

    // Edge Case 2: Large numbers
    test('large numbers', () => {
        const nums = [100000, -100000, 0];
        const result = threeSum(nums);
        expect(result).toEqual([[-100000, 0, 100000]]);
    });

    // Edge Case 3: All negative numbers
    test('all negative numbers', () => {
        const nums = [-3, -2, -1];
        const result = threeSum(nums);
        expect(result).toEqual([]);
    });

    // Edge Case 4: All positive numbers
    test('all positive numbers', () => {
        const nums = [1, 2, 3];
        const result = threeSum(nums);
        expect(result).toEqual([]);
    });

    // Edge Case 5: Large input size with multiple triplets
    test('large input size with multiple triplets', () => {
        const nums = Array.from({ length: 3000 }, (_, i) => i - 1500);
        const result = threeSum(nums);
        // A rough check to ensure the result is not empty and has some expected structure
        expect(result.length).toBeGreaterThan(0);
        result.forEach(triplet => {
            expect(triplet.reduce((acc, num) => acc + num, 0)).toBe(0);
        });
    });

    // Edge Case 6: Duplicate numbers leading to multiple same triplets
    test('duplicate numbers leading to multiple same triplets', () => {
        const nums = [-1, -1, 0, 1, 1];
        const result = threeSum(nums);
        expect(result).toEqual([[-1, 0, 1]]);
    });

    // Edge Case 7: Array with zeroes and positive and negative numbers
    test('array with zeroes and positive and negative numbers', () => {
        const nums = [-2, 0, 0, 2, 2];
        const result = threeSum(nums);
        expect(result).toEqual([[-2, 0, 2]]);
    });

    // Edge Case 8: All zeroes
    test('all zeroes', () => {
        const nums = [0, 0, 0, 0, 0];
        const result = threeSum(nums);
        expect(result).toEqual([[0, 0, 0]]);
    });

    // Edge Case 9: Single zero triplet among many non-zero numbers
    test('single zero triplet among many non-zero numbers', () => {
        const nums = [1, 2, -2, -1, -1, 0];
        const result = threeSum(nums);
        expect(result).toEqual([[-2, 0, 2], [-1, -1, 2], [-1, 0, 1]]);
    });

    // Edge Case 10: Negative and positive numbers with zero sum triplet
    test('negative and positive numbers with zero sum triplet', () => {
        const nums = [-1, -1, 2];
        const result = threeSum(nums);
        expect(result).toEqual([[-1, -1, 2]]);
    });
});
