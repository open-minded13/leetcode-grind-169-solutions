const minNumOfStickers = require('./Hard 691. Stickers to Spell Word')

describe('minNumOfStickers', () => {
    // Test with simple cases
    it('returns 1 when the target string can be covered by a single sticker', () => {
        const stickers = ["abc"];
        const target = "abc";
        expect(minNumOfStickers(stickers, target)).toBe(1);
    });

    // Test with edge cases
    it('returns -1 when the target string cannot be covered by any stickers', () => {
        const stickers = ["abc"];
        const target = "def";
        expect(minNumOfStickers(stickers, target)).toBe(-1);
    });

    // Test with random inputs
    it('returns the correct number of stickers for a random target string and stickers', () => {
        const stickers = ["abc", "def", "ghi"];
        const target = "abcdefghi";
        expect(minNumOfStickers(stickers, target)).toBe(3);
    });

    // Test with large inputs
    it('returns the correct number of stickers for a large target string and stickers', () => {
        const stickers = ["abc", "def", "ghi", "jkl", "mno", "pqr", "stu", "vwx", "yz"];
        const target = "abcdefghijklmnopqrstuvwxyz";
        expect(minNumOfStickers(stickers, target)).toBe(9);
    });

    // Test with corner cases
    it('returns -1 when the target string contains only one unique character, but the stickers do not contain that character', () => {
        const stickers = ["abc"];
        const target = "dddd";
        expect(minNumOfStickers(stickers, target)).toBe(-1);
    });

    // Test with a variety of sticker lengths
    it('returns the correct number of stickers for stickers of different lengths', () => {
        const stickers = ["a", "bc", "def", "ghij"];
        const target = "abcdefghij";
        expect(minNumOfStickers(stickers, target)).toBe(4);
    });

    // Test with a variety of target string lengths
    it('returns the correct number of stickers for target strings of different lengths', () => {
        const stickers = ["abc"];
        const target = "abcabcabc";
        expect(minNumOfStickers(stickers, target)).toBe(3);
    });

    // Test with simple cases
    it('returns 1 when target can be covered by a single sticker', () => {
        const stickers = ["hello", "world"];
        const target = "hello";
        expect(minNumOfStickers(stickers, target)).toBe(1);
    });

    // Test with edge cases
    it('returns -1 when target cannot be covered by any stickers', () => {
        const stickers = ["hello", "world"];
        const target = "abc";
        expect(minNumOfStickers(stickers, target)).toBe(-1);
    });

    // Test with random inputs
    it('returns correct result for random inputs', () => {
        const stickers = ["goddame", "bless", "people", "young"];
        const target = "godblessyou";
        expect(minNumOfStickers(stickers, target)).toBe(3);
    });

    // Test with large inputs
    it('returns correct result for large inputs', () => {
        const stickers = ["abcdefg", "hijklmn", "opqrst", "uvwxyz"];
        const target = "abcdefghijklmnopqrstuvwxyz";
        expect(minNumOfStickers(stickers, target)).toBe(4);
    });

    // Test with corner cases
    it('returns -1 when target contains only one unique character not in stickers', () => {
        const stickers = ["hello", "world"];
        const target = "a";
        expect(minNumOfStickers(stickers, target)).toBe(-1);
    });

    // Test with a variety of sticker lengths
    it('returns correct result for stickers of different lengths', () => {
        const stickers = ["a", "bc", "def", "ghij"];
        const target = "abcdefghij";
        expect(minNumOfStickers(stickers, target)).toBe(4);
    });

    // Test with a variety of target string lengths
    it('returns correct result for target strings of different lengths', () => {
        const stickers = ["abcdefg", "hijklmn", "opqrst", "uvwxyz"];
        const target = "abcd";
        expect(minNumOfStickers(stickers, target)).toBe(1);
    });
});