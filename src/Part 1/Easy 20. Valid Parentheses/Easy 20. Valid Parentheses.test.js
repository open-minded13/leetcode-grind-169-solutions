const isValid = require('./Easy 20. Valid Parentheses');

describe('Parentheses Validator', () => {
    it('should return true for empty string', () => {
        expect(isValid("")).toBe(true);
    });

    it('should return true for single pair of parentheses', () => {
        expect(isValid("()")).toBe(true);
    });

    it('should return true for multiple pairs of parentheses', () => {
        expect(isValid("()[]{}")).toBe(true);
    });

    it('should return false for single closing parenthesis', () => {
        expect(isValid(")")).toBe(false);
    });

    it('should return false for single opening parenthesis', () => {
        expect(isValid("(")).toBe(false);
    });

    it('should return false for mismatched parentheses', () => {
        expect(isValid("(]")).toBe(false);
    });

    it('should return false for mismatched parentheses in a sequence', () => {
        expect(isValid("([)]")).toBe(false);
    });

    it('should return true for nested parentheses', () => {
        expect(isValid("{[]}")).toBe(true);
    });

    it('should return false for unbalanced parentheses', () => {
        expect(isValid("({)}")).toBe(false);
    });

    it('should return false for extra closing parentheses', () => {
        expect(isValid("()())")).toBe(false);
    });

    it('should return false for extra opening parentheses', () => {
        expect(isValid("(()")).toBe(false);
    });

    it('should return true for long sequence of balanced parentheses', () => {
        expect(isValid("((()))[]{[]}")).toBe(true);
    });

    it('should return false for long sequence of unbalanced parentheses', () => {
        expect(isValid("((()))[]{[]})")).toBe(false);
    });

    it('should return true for string with non-parentheses characters', () => {
        expect(isValid("hello world")).toBe(true);
    });

    it('should return false for string with non-parentheses characters and unbalanced parentheses', () => {
        expect(isValid("(hello world")).toBe(false);
    });
});