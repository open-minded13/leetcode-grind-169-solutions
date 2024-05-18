const isPalindrome = require("./Easy 125. Valid Palindrome")

describe('isPalindrome', () => {
    it('should return false for null and undefined', () => {
        expect(isPalindrome(null)).toBe(false);
        expect(isPalindrome(undefined)).toBe(false);
    });

    it('should return true for an empty string', () => {
        expect(isPalindrome('')).toBe(true);
    });

    it('should return true for a string containing only whitespace', () => {
        expect(isPalindrome('   ')).toBe(true);
    });

    it('should return true for a single character string', () => {
        expect(isPalindrome('a')).toBe(true);
    });

    it('should return true for a numeric string', () => {
        expect(isPalindrome('12321')).toBe(true);
    });

    it('should handle mixed case characters', () => {
        expect(isPalindrome('RaceCar')).toBe(true);
        expect(isPalindrome('RoTator')).toBe(true);
    });

    it('should ignore non-alphanumeric characters', () => {
        expect(isPalindrome('RaceCar!@#')).toBe(true);
        expect(isPalindrome('Hello@# World')).toBe(false);
    });
});