# Date of Last Practice: Jun 12, 2023 -> Feb 12, 2024
#
# Time Complexity: O(log N), where N is the length of the input nums.
#
# Space Complexity: O(1), because the space used by the variables is not dependent
#                   on the size of the input array.


class Solution:
    def search(self, nums, target) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            # Python's integers can dynamically adjust their size to accommodate large numbers,
            # so there is no risk of integer overflow in this specific case.
            # Therefore, you can directly use (left + right) // 2.
            pivot = left + (right - left) // 2

            if target == nums[pivot]:
                return pivot

            if nums[left] <= nums[pivot]:
                if target >= nums[left] and target < nums[pivot]:
                    right = pivot - 1
                else:
                    left = pivot + 1

            if nums[right] >= nums[pivot]:
                if target > nums[pivot] and target <= nums[right]:
                    left = pivot + 1
                else:
                    right = pivot - 1
        return -1


solution = Solution()
nums = [4, 5, 6, 7, 8, 0, 1, 2]
target = 0
index = solution.search(nums, target)
if index != -1:
    print(f"Target {target} found at index {index}")
else:
    print(f"Target {target} not found")


# The f in print(f"Target") is a prefix that denotes an f-string in Python.
# An f-string is a string literal that allows you to embed expressions
# inside curly braces {} within the string. These expressions are evaluated at runtime
# and their values are inserted into the string.
#
# Using f-strings makes it easier to create formatted strings by
# embedding variables or expressions directly within the string,
# without the need for explicit string concatenation or formatting functions.
name = "Claire"
age = 25
print(f"{name} is Joe's girlfriend. She is {age} years old.")

# {if age > 25: 'old' else: 'young'} is not valid.
# But we can use a ternary operator inside the curly braces to achieve a similar result.
# It has the form: value_if_true if condition else value_if_false.
print(f"Is {name} 30 years old? {'Yes' if age > 30 else 'No'}")
