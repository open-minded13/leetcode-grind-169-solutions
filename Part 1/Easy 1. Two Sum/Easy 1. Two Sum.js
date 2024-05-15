// Date of Last Practice: Apr 29, 2024
// 
// Time complexity: O(N), where N is the length of nums.
//                  Overall, the time complexity of this solution is O(n)
//                  since it only iterates over the input list once.
//
// Space Complexity: O(N), where N is the length of nums.
//                   The space complexity is also O(n) since
//                   the dictionary mp can store up to all elements of the input vector.

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */

const twoSum = (nums, target) => {
    seen = {}
    for (let i = 0; i < nums.length; i++) {
        const complement = target - nums[i]
        if (complement in seen) {
            return [seen[complement], i]
        }
        seen[nums[i]] = i
    }
    return [-1, -1]
}

module.exports = twoSum;