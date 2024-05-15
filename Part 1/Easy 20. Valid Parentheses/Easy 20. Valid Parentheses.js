// Date of Last Practice: May 14, 2024

// Time Complexity: O(N), where n is the length of the input string because
//                  the method iterates through each character in the input string.

// Space Complexity: O(N), where n is the maximum of the size of the stack,
//     depending on the input string.This is because, in the worst case,
//                   the method keeps adding a new stack if it can't find the correct closing bracket.

var isValid = function (s) {
    const stack = []
    for (char of s) {
        if (char === "(" || char === "{" || char === "[") {
            stack.push(char)
        }
        else {
            if (stack.length === 0) {
                return false
            }
            else if ((char === ")" && "(" === stack[stack.length - 1]) ||
                (char === "}" && "{" === stack[stack.length - 1]) ||
                (char === "]" && "[" === stack[stack.length - 1])) {
                stack.pop()
            }
            else {
                stack.push(char)
            }
        }
    }
    return stack.length === 0
};