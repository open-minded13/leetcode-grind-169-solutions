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