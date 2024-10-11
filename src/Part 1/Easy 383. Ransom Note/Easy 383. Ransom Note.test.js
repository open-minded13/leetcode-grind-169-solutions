const canConstruct = require("./Easy 383. Ransom Note")

describe('canConstruct', () => {
    // Empty order list and inventory list
    it('returns true when both lists are empty', () => {
        const ransomNote = '';
        const magazine = '';
        expect(canConstruct(ransomNote, magazine)).toBe(true);
    });

    // Empty order list and non-empty inventory list
    it('returns true when order list is empty and inventory list is not', () => {
        const ransomNote = '';
        const magazine = 'abc';
        expect(canConstruct(ransomNote, magazine)).toBe(true);
    });

    // Non-empty order list and empty inventory list
    it('returns false when order list is not empty and inventory list is', () => {
        const ransomNote = 'abc';
        const magazine = '';
        expect(canConstruct(ransomNote, magazine)).toBe(false);
    });

    // Order list and inventory list with same items
    it('returns true when both lists have same items', () => {
        const ransomNote = 'abc';
        const magazine = 'abc';
        expect(canConstruct(ransomNote, magazine)).toBe(true);
    });

    // Order list with duplicate items and inventory list with same items
    it('returns true when order list has duplicates and inventory list has same items', () => {
        const ransomNote = 'aabbcc';
        const magazine = 'abcabc';
        expect(canConstruct(ransomNote, magazine)).toBe(true);
    });

    // Order list with duplicate items and inventory list without enough items
    it('returns false when order list has duplicates and inventory list does not have enough items', () => {
        const ransomNote = 'aabbcc';
        const magazine = 'abc';
        expect(canConstruct(ransomNote, magazine)).toBe(false);
    });

    // Order list with unique items and inventory list with more items
    it('returns true when order list has unique items and inventory list has more items', () => {
        const ransomNote = 'abc';
        const magazine = 'abcdefg';
        expect(canConstruct(ransomNote, magazine)).toBe(true);
    });

    // Order list with unique items and inventory list with less items
    it('returns false when order list has unique items and inventory list has less items', () => {
        const ransomNote = 'abc';
        const magazine = 'ab';
        expect(canConstruct(ransomNote, magazine)).toBe(false);
    });

    // Order list with items not in inventory list
    it('returns false when order list has items not in inventory list', () => {
        const ransomNote = 'abc';
        const magazine = 'def';
        expect(canConstruct(ransomNote, magazine)).toBe(false);
    });

    // Large order list and inventory list
    it('returns true when both lists are large and inventory list can fulfill order', () => {
        const ransomNote = 'abcdefghijklmnopqrstuvwxyz';
        const magazine = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz';
        expect(canConstruct(ransomNote, magazine)).toBe(true);
    });
});
