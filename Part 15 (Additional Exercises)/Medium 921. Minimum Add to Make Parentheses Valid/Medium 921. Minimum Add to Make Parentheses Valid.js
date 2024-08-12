// Date of Last Practice: Mar 15, 2024
//
// Time Complexity: O(N), where N is the length of the string.
//                  This is because the solution iterates through each character of
//                  the string exactly once.
//
// Space Complexity: O(1).The solution uses only a constant amount of extra space
//                   to store the variables left_parenthesis and right_parenthesis,
//                   regardless of the size of the input string.

var minAddToMakeValid = function (s) {
    let left_parentheses = 0
    let right_parenthses = 0

    for (const char of s) {
        if (char === "(") {
            left_parentheses++
        }
        else if (char === ")") {
            if (left_parentheses) {
                left_parentheses--
            }
            else {
                right_parenthses++
            }
        }
    }

    return left_parentheses + right_parenthses
}

module.exports = minAddToMakeValid


// The following are the increased versions for {}, [], ():
// 
// var minAddToMakeValid = function (s) {
//     let leftParentheses = 0;
//     let rightParentheses = 0;
//     let leftBrackets = 0;
//     let rightBrackets = 0;
//     let leftCurlyBraces = 0;
//     let rightCurlyBraces = 0;

//     for (const char of s) {
//         if (char === '(') {
//             leftParentheses++;
//         } else if (char === ')') {
//             if (leftParentheses > 0) {
//                 leftParentheses--;
//             } else {
//                 rightParentheses++;
//             }
//         } else if (char === '[') {
//             leftBrackets++;
//         } else if (char === ']') {
//             if (leftBrackets > 0) {
//                 leftBrackets--;
//             } else {
//                 rightBrackets++;
//             }
//         } else if (char === '{') {
//             leftCurlyBraces++;
//         } else if (char === '}') {
//             if (leftCurlyBraces > 0) {
//                 leftCurlyBraces--;
//             } else {
//                 rightCurlyBraces++;
//             }
//         }
//     }

//     return leftParentheses + rightParentheses + leftBrackets + rightBrackets + leftCurlyBraces + rightCurlyBraces;
// }


// module.exports = minAddToMakeValid