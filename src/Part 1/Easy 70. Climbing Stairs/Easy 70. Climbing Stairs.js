// Date of Last Practice: May 16, 2024

// Time Complexity: O(N), where N is the number of steps we have on the stair.
//                  This is because we use a for loop to iterate from 3 to N.
// Space Complexity: O(1) because we use a constant amount of extra space to store three variables.

var climbStairs = function (n) {
    if (!Number.isInteger(n) || n < 0) {
        throw new Error('n should be a non-negative integer')
    }
    if (n <= 2) {
        return n
    }

    let ways_when_i_minus_2 = 1
    let ways_when_i_minus_1 = 2
    let numOfWays
    for (let i = 3; i <= n; i++) {
        numOfWays = ways_when_i_minus_2 + ways_when_i_minus_1
        ways_when_i_minus_2 = ways_when_i_minus_1
        ways_when_i_minus_1 = numOfWays
    }

    return numOfWays
};

module.exports = climbStairs