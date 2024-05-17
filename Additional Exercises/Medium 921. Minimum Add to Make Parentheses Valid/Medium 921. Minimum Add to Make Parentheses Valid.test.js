const minAddToMakeValid = require('./Medium 921. Minimum Add to Make Parentheses Valid');

describe('Min Add To Make Valid', () => {
    it('should return 0 for empty string', () => {
        expect(minAddToMakeValid("")).toBe(0);
    });

    it('should return 1 for single closing parenthesis', () => {
        expect(minAddToMakeValid(")")).toBe(1);
    });

    it('should return 1 for single opening parenthesis', () => {
        expect(minAddToMakeValid("(")).toBe(1);
    });

    it('should return 0 for balanced parentheses', () => {
        expect(minAddToMakeValid("()")).toBe(0);
    });

    it('should return 1 for unbalanced parentheses', () => {
        expect(minAddToMakeValid("())")).toBe(1);
    });

    it('should return 2 for two unbalanced parentheses', () => {
        expect(minAddToMakeValid("hello))")).toBe(2);
    });

    it('should return 3 for three unbalanced parentheses', () => {
        expect(minAddToMakeValid("hello)))")).toBe(3);
    });

    it('should return 1 for nested unbalanced parentheses', () => {
        expect(minAddToMakeValid("(hello) world)")).toBe(1);
    });

    it('should return 2 for two nested unbalanced parentheses', () => {
        expect(minAddToMakeValid("(hello) world))")).toBe(2);
    });

    it('should return 1 for unbalanced parentheses at the start', () => {
        expect(minAddToMakeValid(")hello world")).toBe(1);
    });

    it('should return 1 for unbalanced parentheses at the end', () => {
        expect(minAddToMakeValid("hello world(")).toBe(1);
    });

    it('should return 2 for two unbalanced parentheses at the start', () => {
        expect(minAddToMakeValid("))hello world")).toBe(2);
    });

    it('should return 2 for two unbalanced parentheses at the end', () => {
        expect(minAddToMakeValid("hello world((")).toBe(2);
    });

    it('should return 0 for string with non-parentheses characters', () => {
        expect(minAddToMakeValid("hello world")).toBe(0);
    });

    it('should return 1 for string with non-parentheses characters and unbalanced parentheses', () => {
        expect(minAddToMakeValid("hello world(")).toBe(1);
    });

    it('should return 1 for unbalanced square brackets', () => {
        expect(minAddToMakeValid("[hello world")).toBe(1);
    });

    it('should return 1 for unbalanced curly braces', () => {
        expect(minAddToMakeValid("{hello world")).toBe(1);
    });

    it('should return 0 for two balanced square brackets', () => {
        expect(minAddToMakeValid("[hello world]")).toBe(0);
    });

    it('should return 0 for two balanced curly braces', () => {
        expect(minAddToMakeValid("{hello world}")).toBe(0);
    });

    it('should return 1 for mixed unbalanced parentheses', () => {
        expect(minAddToMakeValid("(hello [world]")).toBe(1);
    });
});