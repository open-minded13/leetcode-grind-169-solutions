// Date of Last Practice: Apr 29, 2024

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