// Date of Last Practice: May 23, 2024

// Time Complexity: O(N), where n is the length of the input strings s and t.
//                  The solution iterates over both strings once to count the frequency of characters and
//                  then checks if the character frequencies match.
// Space Complexity: O(1) because the charCount object always has a fixed size of 26,
//                   representing the lowercase English letters.

var isAnagram = function (s, t) {
    if (s == "" || t == "" || s == null || t == null || s.length != t.length) {
        return false
    }

    let charCount = {}
    for (let char of s) {
        charCount[char] = (charCount[char] || 0) + 1
    }

    for (let char of t) {
        if (!charCount[char]) {
            return false
        }
        charCount[char] -= 1
    }

    return true
}

module.exports = isAnagram