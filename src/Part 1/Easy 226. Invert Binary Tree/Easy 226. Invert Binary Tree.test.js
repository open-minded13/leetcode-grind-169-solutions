const invertTree = require('./Easy 226. Invert Binary Tree') // Replace with the correct import path

describe('invertTree', () => {
    // First edge case: A null root node
    it('should handle a null root node', () => {
        const root = null;
        const result = invertTree(root);
        expect(result).toBeNull();
    });
    // Second edge case: A single node tree
    it('should handle a single node tree', () => {
        const root = { val: 1 };
        const expected = { val: 1 };
        const result = invertTree(root);
        expect(result).toEqual(expected);
    });
    // Third edge case: Left subtree is empty, right subtree is not
    it('should invert a tree with an empty left subtree', () => {
        const root = {
            val: 1,
            right: { val: 3, right: { val: 5 } }
        };
        const expected = {
            val: 1,
            left: { val: 3, left: { val: 5 } }
        };
        const result = invertTree(root);
        expect(result).toEqual(expected);
    });
    // Fourth edge case: Right subtree is empty, left subtree is not
    it('should invert a tree with an empty right subtree', () => {
        const root = {
            val: 1,
            left: { val: 2 }
        };
        const expected = {
            val: 1,
            right: { val: 2 }
        };
        const result = invertTree(root);
        expect(result).toEqual(expected);
    });
    // Fifth edge case: Both subtrees are empty
    it('should handle a node with empty subtrees', () => {
        const root = { val: 1 };
        const expected = { val: 1 };
        const result = invertTree(root);
        expect(result).toEqual(expected);
    });
    // Sixth edge case: A larger, more unbalanced binary tree.
    it('should correctly invert a larger, unbalanced binary tree', () => {
        const root = {
            val: 4,
            left: {
                val: 2,
                left: { val: 1 }
            },
            right: { val: 6 }
        };
        const expected = {
            val: 4,
            right: {
                val: 2,
                right: { val: 1 }
            },
            left: { val: 6 }
        };
        const result = invertTree(root);
        expect(result).toEqual(expected);
    });
    // Seventh edge case: undefined nodes in the tree
    it('should handle nodes with undefined left or right pointers', () => {
        const root = {
            val: 1,
            left: undefined,
            right: { val: 3 }
        };
        const expected = {
            val: 1,
            left: { val: 3 },
            right: undefined
        };
        const result = invertTree(root);
        expect(result).toEqual(expected);
    });
    // Eight edge case: A node with only right child should become the new root with a null left child
    it('should place a node with only a right child as the new root with a null left child', () => {
        const root = {
            val: 0,
            left: null,
            right: { val: 5 }
        };
        const expected = {
            val: 0,
            left: { val: 5 },
            right: null
        }
        const result = invertTree(root);
        expect(result).toEqual(expected);
    });
    // Ninth edge case: Invert a tree with a right node and a left node, where the right node has a left child and the left node has no children.
    it('should correctly invert a tree with mixed child nodes', () => {
        const root = {
            val: 'Grandparent',
            right: { val: 'Parent', left: { val: 'Child' } },
            left: { val: 'Uncle' }
        };
        const expected = {
            val: 'Grandparent',
            left: { val: 'Parent', right: { val: 'Child' } },
            right: { val: 'Uncle' }
        }; const result = invertTree(root); expect(result).toEqual(expected);
    });
    // Tenth edge case: A deeply nested tree
    it('should handle a deeply nested tree', () => {
        const root = {
            val: 'A',
            left: { val: 'B', right: { left: { val: 'C' }, right: { val: 'D' } } }
        };
        const expected = {
            val: 'A',
            right: { val: 'B', left: { right: { val: 'C' }, left: { val: 'D' } } }
        };
        const result = invertTree(root);
        expect(result).toEqual(expected);
    });
});