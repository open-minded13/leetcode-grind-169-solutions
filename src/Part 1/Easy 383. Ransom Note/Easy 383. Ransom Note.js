// Date of Last Practice: May 26, 2024

// Time Complexity: O(N+M), where N and M are the length of the ransomNote and magazine strings respectively.

// Space Complexity: O(N), where N is the length of the ransomNote.
//                   In the worst case, as the letter_counter dictionary can store
//                   at most all distinct letters from the magazine string.

var canConstruct = function (ransomNote, magazine) {
    const magazineCount = {}

    for (let item of magazine) {
        magazineCount[item] = (magazineCount[item] || 0) + 1
    }

    for (let item of ransomNote) {
        if (!magazineCount[item] || magazineCount[item] === 0) {
            return false
        }
        magazineCount[item]--
    }
    return true
};

module.exports = canConstruct