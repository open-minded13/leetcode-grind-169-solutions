// Date of Last Practice: May 23, 2024

// Time Complexity: O(n), where n is the length of the strings.
//                  This is because we iterate through both strings once,
//                  and map operations(insertions and lookups) are O(1) on average.

// Space Complexity: O(1), assuming a fixed set of unique characters
//                   (26 for lowercase letters or 128 for the full ASCII set). 
//                   The space used by the charCount object is constant and 
//                   does not depend on the input size.

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