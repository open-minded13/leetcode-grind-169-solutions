const isValidBST = require('./Medium 98. Validate Binary Search Tree')

// Definition for a binary tree node.
function TreeNode(val, left = null, right = null) {
    this.val = val;
    this.left = left;
    this.right = right;
}

describe('isValidBST', () => {
    test('Single Node Tree', () => {
        const root = new TreeNode(1);
        expect(isValidBST(root)).toBe(true);
    });

    test('Small Valid BST', () => {
        const root = new TreeNode(2, new TreeNode(1), new TreeNode(3));
        expect(isValidBST(root)).toBe(true);
    });

    test('Small Invalid BST', () => {
        const root = new TreeNode(5, new TreeNode(1), new TreeNode(4, new TreeNode(3), new TreeNode(6)));
        expect(isValidBST(root)).toBe(false);
    });

    test('Large Valid BST', () => {
        const root = new TreeNode(10,
            new TreeNode(5, new TreeNode(2), new TreeNode(7)),
            new TreeNode(15, new TreeNode(12), new TreeNode(20))
        );
        expect(isValidBST(root)).toBe(true);
    });

    test('Large Invalid BST', () => {
        const root = new TreeNode(10,
            new TreeNode(5, new TreeNode(2), new TreeNode(7)),
            new TreeNode(15, new TreeNode(6), new TreeNode(20))
        );
        expect(isValidBST(root)).toBe(false);
    });

    test('BST with Duplicate Values', () => {
        const root = new TreeNode(10, new TreeNode(5), new TreeNode(10));
        expect(isValidBST(root)).toBe(false);
    });

    test('Negative Values in BST', () => {
        const root = new TreeNode(0, new TreeNode(-1), new TreeNode(1));
        expect(isValidBST(root)).toBe(true);
    });

    test('Maximum and Minimum Integer Values', () => {
        const root = new TreeNode(0,
            new TreeNode(Number.MIN_SAFE_INTEGER),
            new TreeNode(Number.MAX_SAFE_INTEGER)
        );
        expect(isValidBST(root)).toBe(true);
    });

    test('Deep Left-Skewed Tree', () => {
        const root = new TreeNode(5,
            new TreeNode(4,
                new TreeNode(3,
                    new TreeNode(2,
                        new TreeNode(1)
                    )
                )
            )
        );
        expect(isValidBST(root)).toBe(true);
    });

    test('Deep Right-Skewed Tree', () => {
        const root = new TreeNode(1,
            null,
            new TreeNode(2,
                null,
                new TreeNode(3,
                    null,
                    new TreeNode(4,
                        null,
                        new TreeNode(5)
                    )
                )
            )
        );
        expect(isValidBST(root)).toBe(true);
    });
});
