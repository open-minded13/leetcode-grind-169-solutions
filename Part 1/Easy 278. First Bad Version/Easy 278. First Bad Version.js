// Date of Last Practice: May 25, 2024

// Time Complexity: O(log N), where N is the amount of all versions.
//                  In each step of the binary search, we reduce the search space by half.
//                  Therefore, it takes logarithmic time to find the first bad version.

// Space Complexity: O(1), since we use a constant amount of space to store variables.
//                   It does not use any data structures that depend on the input size.


var solution = function (isBadVersion) {
    return function (n) {
        let low = 1, high = n

        while (low <= high) {
            const mid = Math.floor((low + high) / 2)
            if (isBadVersion(mid)) {
                high = mid - 1 // Broken commit is in the lower half
            }
            else {
                low = mid + 1 // Broken commit is in the higher half
            }
        }

        return low
    };
};


module.exports = solution