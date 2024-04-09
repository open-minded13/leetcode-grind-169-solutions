# Date of Last Practice: June 11, 2023 -> Jan 21, 2024
#
# Time complexity: O(N), where N is the length of nums.
#                  Overall, the time complexity of this solution is O(n)
#                  since it only iterates over the input list once.
#
# Space Complexity: O(N), where N is the length of nums.
#                   The space complexity is also O(n) since
#                   the dictionary mp can store up to all elements of the input vector.


class Solution:
    def two_sum(self, nums, target):
        # A new dictionary called 'mp' is created to store the key-value pairs.
        mp = {}
        for i in range(len(nums)):
            # For each element, the code checks if 'target - nums[i]' exists as a key in the dictionary.
            # If it doesn't exist, the current element 'nums[i]' is added as a key and its index 'i' is added
            # as a value to the dictionary. This means that in future iterations,
            # if another element is found that when added to the current element equals 'target',
            # the index of the current element can be retrieved in constant time.
            if target - nums[i] not in mp:
                mp[nums[i]] = i
            # If it does exist, this means that we have found the pair of indices that add up to the target value.
            # So, the current index 'i' is returned along with
            # the index of the existing key-value pair 'mp[target - nums[i]]'.
            else:
                return [mp[target - nums[i]], i]
        return [-1, -1]


nums = [4, 5, 2, 3]
target = 9

solution = Solution()
result = solution.two_sum(nums, target)

if result != [-1, -1]:
    print(result[0], "and", result[1])
else:
    print("Not Found!")
