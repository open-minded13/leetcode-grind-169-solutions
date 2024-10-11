const climbStairs = require('./Easy 70. Climbing Stairs')

describe('climbStairs', () => {
    test('should return 0 for n = 0', () => {
        expect(climbStairs(0)).toBe(0);
    });

    test('should return 1 for n = 1', () => {
        expect(climbStairs(1)).toBe(1);
    });

    test('should return 2 for n = 2', () => {
        expect(climbStairs(2)).toBe(2);
    });

    test('should return 3 for n = 3', () => {
        expect(climbStairs(3)).toBe(3);
    });

    test('should return 5 for n = 4', () => {
        expect(climbStairs(4)).toBe(5);
    });

    test('should return 8 for n = 5', () => {
        expect(climbStairs(5)).toBe(8);
    });

    test('should throw an error for negative n', () => {
        expect(() => climbStairs(-1)).toThrowError('n should be a non-negative integer');
    });

    test('should throw an error for non-integer n', () => {
        expect(() => climbStairs(1.5)).toThrowError('n should be a non-negative integer');
    });
});