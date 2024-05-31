// Date of Last Practice: May 30, 2024
// 
// Time Complexity: O(N^2). 
// 
// Space Complexity: O(N). 

var threeSum = function (nums) {
    // Step 1: Sort the array to make it easier to avoid duplicates and use two-pointer technique
    nums.sort((a, b) => a - b)
    const result = []

    // Step 2: Iterate through the array, using each number as a potential first number in the triplet
    for (let i = 0; i < nums.length; i++) {
        // Step 3: Skip duplicate values for the first number
        if (i > 0 && nums[i] === nums[i - 1]) {
            continue
        }

        // Step 4: Use two-pointer approach to find pairs that sum to the negative of the current number
        let cur_element = nums[i]
        let left = i + 1, right = nums.length - 1
        while (left < right) {
            const sum = cur_element + nums[left] + nums[right]

            if (sum === 0) {
                result.push([cur_element, nums[left], nums[right]])

                // Skip duplicate values for the second and third numbers
                while (left + 1 < nums.length - 1 && nums[left + 1] === nums[left]) {
                    left++
                }
                while (right - 1 > i + 1 && nums[right - 1] === nums[right]) {
                    right--
                }
                left++
                right--
            }
            else if (sum < 0) {
                left++
            }
            else {
                right--
            }
        }
    }

    return result
};