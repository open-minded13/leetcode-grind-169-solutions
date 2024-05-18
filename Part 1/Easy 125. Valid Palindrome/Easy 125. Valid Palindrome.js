// Date of Last Practice: Mar 17, 2024
// 
// Time Complexity: O(N), where N is the length of the string. 
//                  Overall, the time complexity is O(N) due to the linear operations for
//                  removing non - alphanumeric characters O(N), converting to lowercase O(N),
//                  and the loop O(N / 2).
// Space Complexity: O(N), where N is the length of the string. 
//                   This is due to the creation of the letters string.

var isPalindrome = function (s) {
    if (s === null || s === undefined) {
        return false;
    }

    s = s.toLowerCase()
    s = s.replace(/[^a-z0-9]/g, "")

    for (let i = 0, j = s.length - 1; i <= j; i++, j--) {
        if (s[i] !== s[j]) {
            return false
        }
    }
    return true
};

module.exports = isPalindrome