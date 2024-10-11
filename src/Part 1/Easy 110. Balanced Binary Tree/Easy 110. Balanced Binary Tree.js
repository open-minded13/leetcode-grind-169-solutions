// Date of Last Practice: May 16, 2024

// Time Complexity: O(N), where N is the total number of nodes in the tree.

// Space Complexity: O(H), where H is the height of the tree, due to the recursive call stack.
//                   In the worst case, the tree could be skewed, making the space complexity O(N).

var isBalanced = function (root) {

    function checkDepth(node) {
        if (!node) {
            return 0
        }
        const leftDepth = checkDepth(node.left)
        const rightDepth = checkDepth(node.right)
        if (leftDepth === -1 || rightDepth === -1 || Math.abs(leftDepth - rightDepth) > 1) {
            return -1
        }
        return Math.max(leftDepth, rightDepth) + 1
    }

    return checkDepth(root) !== -1
};

module.exports = isBalanced