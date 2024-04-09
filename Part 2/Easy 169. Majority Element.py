from typing import List

# Date of Last Practice: Oct 29, 2023 -> Feb 2, 2024
#
# Time Complexity: O(N), where N is the amount of numbers in the list.
#                  This is because we use a for loop to iterate the "nums" list .
# Space Complexity: O(1) because we use a constant amount of extra space to store two variables.
#
# Moore Voting Algorithm: The algorithm is based on the fun fact that
#                         the majority element will always survive
#                         during the process of count-based elimination.
#                         The algorithm's core idea is picking a candidate, pairing it with others,
#                         and ensuring the majority element can survive
#                         through the elimination process.


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority_num = None
        counter = 0
        for num in nums:
            if counter == 0:
                majority_num = num
                counter += 1
            elif num == majority_num:
                counter += 1
            else:
                counter -= 1
        return majority_num


class First_Solution:
    # Time Complexity: O(N)
    # Space Complexity: O(N)
    def majorityElement(self, nums: List[int]) -> int:
        num_counter = {}
        for num in nums:
            if num in num_counter:
                num_counter[num] += 1
            else:
                num_counter[num] = 1
            if num_counter[num] > len(nums) // 2:
                return num


# Test cases
solution = Solution()
test_input_1 = [3, 2, 3]
test_input_2 = [2, 2, 1, 1, 1, 2, 2]
test_input_3 = [1]
test_input_4 = [1, 2, 3, 4, 5, 6, 7, 8, 1, 1, 1]

print(solution.majorityElement(test_input_1))  # Output: 3
print(solution.majorityElement(test_input_2))  # Output: 2
print(solution.majorityElement(test_input_3))  # Output: 1
print(solution.majorityElement(test_input_4))  # Output: None
