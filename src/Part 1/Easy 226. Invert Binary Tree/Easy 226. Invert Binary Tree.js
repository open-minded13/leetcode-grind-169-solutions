// # Date of Last Practice: May 23, 2024

// Time Complexity: O(N), where N is the total number of nodes in the given tree.
//                  This is because the solution recursively visits each node in the tree exactly once.

// Space Complexity: O(H), where H is the height of the tree. In the recursive calls,
//                   the maximum depth of the call stack is equal to the height of the tree.
//                   Therefore, the space complexity is determined by the maximum depth of the recursion,
//                   which is the height of the tree.
//                   In the worst case, for a skewed tree, the height can be equal to the number of nodes N,
//                   resulting in a space complexity of O(N).
//                   However, for a balanced tree, the height is logarithmic in the number of nodes,
//                   resulting in a space complexity of O(log N).
//                   So, the space complexity is O(H) or O(log N), depending on the height of the tree.

// NOTE: Call Stack: When a function is called recursively,
//                   the system allocates memory on the call stack to store the function call,
//                   including its parameters, return address, and local variables.
//                   The call stack grows as new function calls are made and shrinks as the function calls return.

function invertTree(root) {
    if (root == null || root == undefined) {
        return root
    }

    const temp = root.left
    root.left = root.right
    root.right = temp

    invertTree(root.left)
    invertTree(root.right)

    return root
}

module.exports = invertTree