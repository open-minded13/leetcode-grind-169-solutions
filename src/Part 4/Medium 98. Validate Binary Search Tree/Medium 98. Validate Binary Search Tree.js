// Date of Last Practice: May 31, 2024

// Time Complexity: O(N), where N is the number of nodes in the tree.
//                  The algorithm performs a depth - first traversal of the binary tree.
//                  During this traversal, it visits every node exactly once.

// Space Complexity: O(N), where N is the number of nodes in the tree.
//                   For a skewed tree(worst case), the space complexity is O(N).
//                   For a balanced tree, the space complexity is O(log N).

function TreeNode(val, left, right) {
    this.val = (val === undefined ? 0 : val)
    this.left = (left === undefined ? null : left)
    this.right = (right === undefined ? null : right)
}

function isValidBST(root) {
    // Call the helper function with the initial parameters
    return isValidBSTHelper(root);
}

function isValidBSTHelper(root, min_val = Number.NEGATIVE_INFINITY, max_val = Number.POSITIVE_INFINITY) {
    // Return true when reaching an empty leaf
    if (root === null) {
        return true;
    }

    // Validate the current node's value against the allowed range
    if (root.val <= min_val || root.val >= max_val) {
        return false;
    }

    // Recursively validate the left and right subtrees
    const isValidLeft = isValidBSTHelper(root.left, min_val, root.val);
    const isValidRight = isValidBSTHelper(root.right, root.val, max_val);

    // The current tree is a valid BST if both left and right subtrees are valid
    return isValidLeft && isValidRight;
}

module.exports = isValidBST