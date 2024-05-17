const isBalanced = require('./Easy 110. Balanced Binary Tree')

describe('isBalanced', () => {
    test('empty tree', () => {
        expect(isBalanced(null)).toBe(true);
    });

    test('single node tree', () => {
        const root = { val: 1, left: null, right: null };
        expect(isBalanced(root)).toBe(true);
    });

    test('balanced tree', () => {
        const root = {
            val: 1,
            left: { val: 2, left: null, right: null },
            right: { val: 3, left: null, right: null }
        };
        expect(isBalanced(root)).toBe(true);
    });

    test('unbalanced tree (left-heavy)', () => {
        const root = {
            val: 1,
            left: {
                val: 2,
                left: { val: 4, left: null, right: null },
                right: null
            },
            right: null
        };
        expect(isBalanced(root)).toBe(false);
    });

    test('unbalanced tree (right-heavy)', () => {
        const root = {
            val: 1,
            left: null,
            right: {
                val: 3,
                left: null,
                right: { val: 4, left: null, right: null }
            }
        };
        expect(isBalanced(root)).toBe(false);
    });

    test('edge case: very deep unbalanced tree', () => {
        let root = { val: 1, left: null, right: null };
        for (let i = 0; i < 1000; i++) {
            root = { val: i, left: null, right: root };
        }
        expect(isBalanced(root)).toBe(false);
    });

    test('should return true for a balanced tree', () => {
        const root = {
            val: 1,
            left: {
                val: 2,
                left: { val: 3 },
                right: { val: 4 }
            },
            right: {
                val: 5,
                left: { val: 6 },
                right: { val: 7 }
            }
        };
        expect(isBalanced(root)).toBe(true);
    });

    test('should return false for a balanced tree', () => {
        const root = {
            val: 1,
            left: {
                val: 2,
                left: { val: 3 },
                right: { val: 4 }
            },
            right: {
                val: 5,
                left: { val: 6 },
                right: {
                    val: 7,
                    right: { val: 8 }
                }
            }
        };
        expect(isBalanced(root)).toBe(false);
    });

    test('should return true for a tree with a single node', () => {
        const root = { val: 1 };
        expect(isBalanced(root)).toBe(true);
    });

    test('should return true for an empty tree', () => {
        expect(isBalanced(null)).toBe(true);
    });

    test('should return false for a tree with a skewed left subtree', () => {
        const root = {
            val: 1,
            left: {
                val: 2,
                left: { val: 3 },
                right: null
            },
            right: null
        };
        expect(isBalanced(root)).toBe(false);
    });

    test('should return false for a tree with a skewed right subtree', () => {
        const root = {
            val: 1,
            left: null,
            right: {
                val: 2,
                left: null,
                right: { val: 3 }
            }
        };
        expect(isBalanced(root)).toBe(false);
    });
});