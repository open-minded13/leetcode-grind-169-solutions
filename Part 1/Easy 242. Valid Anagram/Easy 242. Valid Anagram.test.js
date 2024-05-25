// Import the isAnagram function
const isAnagram = require('./Easy 242. Valid Anagram');

// . for the isAnagram function
describe('isAnagram', () => {
    // Test case 1: Valid anagram with matching lengths
    it('should return true for valid anagrams with matching lengths', () => {
        const candidate_gene = 'tacgn';
        const laron_gene = 'actgn';
        const result = isAnagram(candidate_gene, laron_gene);
        // Expect the result to be true since 'tacgn' is an anagram of 'actgn'
        expect(result).toBe(true);
    });

    // Test case 2: Invalid anagram with matching lengths
    it('should return false for invalid anagrams with matching lengths', () => {
        const candidate_gene = 'tacgn';
        const laron_gene = 'atckn';
        const result = isAnagram(candidate_gene, laron_gene);
        // Expect the result to be false since 'tacgn' is not an anagram of 'atcgn'
        expect(result).toBe(false);
    });

    // Test case 3: Invalid anagram with the same unique characters but different character counts
    it('should return false for invalid anagram with the same unique characters but different character counts', () => {
        const candidate_gene = 'abc';
        const laron_gene = 'abcc';
        const result = isAnagram(candidate_gene, laron_gene);
        // Expect the result to be false since 'abc' and 'abcc' have different character counts.
        expect(result).toBe(false);
    });

    // Test case 4: Invalid anagram with different lengths
    it('should return false for invalid anagrams with different lengths', () => {
        const candidate_gene = 'abc';
        const laron_gene = 'abcd';
        const result = isAnagram(candidate_gene, laron_gene);
        // Expect the result to be false since 'abc' is not an anagram of 'abcd'
        expect(result).toBe(false);
    });

    // Test case 5: Empty strings
    it('should return false for empty strings', () => {
        const candidate_gene = '';
        const laron_gene = '';
        const result = isAnagram(candidate_gene, laron_gene);
        // Expect the result to be false since both strings are empty
        expect(result).toBe(false);
    });

    // Test case 6: Strings with special characters
    it('should return true for valid anagrams with special characters', () => {
        const candidate_gene = '!@#$%^&*()_+';
        const laron_gene = ')(*&^%$#@!_+';
        const result = isAnagram(candidate_gene, laron_gene);
        // Expect the result to be true since '!@#$%^&*()_+' is an anagram of ')(*&^%$#@!_+'
        expect(result).toBe(true);
    });

    // Test case 7: Strings with repeating characters
    it('should return true for valid anagrams with repeating characters', () => {
        const candidate_gene = 'aabbcc';
        const laron_gene = 'abcabc';
        const result = isAnagram(candidate_gene, laron_gene);
        // Expect the result to be true since 'aabbcc' is an anagram of 'abcabc'
        expect(result).toBe(true);
    });

    // Test case 8: Invalid anagram with repeating characters
    it('should return false for invalid anagrams with repeating characters', () => {
        const candidate_gene = 'aabbcc';
        const laron_gene = 'abcabd';
        const result = isAnagram(candidate_gene, laron_gene);
        // Expect the result to be false since 'aabbcc' is not an anagram of 'abcabd'
        expect(result).toBe(false);
    });

    // Test case 9: Handle null values
    it('should handle null values and return false', () => {
        const candidate_gene = null;
        const laron_gene = 'abc';
        const result = isAnagram(candidate_gene, laron_gene);
        // Expect the result to be false since one of the strings is null
        expect(result).toBe(false);
    });

    // Test case 10: Handle undefined values
    it('should handle undefined values and return false', () => {
        const candidate_gene = 'abc';
        const laron_gene = undefined;
        const result = isAnagram(candidate_gene, laron_gene);
        // Expect the result to be false since one of the strings is undefined
        expect(result).toBe(false);
    });
});