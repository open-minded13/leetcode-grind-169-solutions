from typing import List

# Date of Last Practice: July 11, 2024 -> Aug 12, 2024
#
# Time Complexity: O(N), where N is the total number of elements in the given list.
#
# Space Complexity: O(1), since the solution uses a constant amount of extra space.


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # Bitwise XOR table:
        # 0 ^ 0 = 0
        # 0 ^ 1 = 1
        # 1 ^ 0 = 1
        # 1 ^ 1 = 0
        #
        # A non-zero number XOR zero will get the number itself:
        # a ^ 0 = a
        #
        # A number XOR itself will get zero:
        # a ^ a = 0
        #
        # Example with the list [6, 6, 7, 7, 8]:
        # 6 ^ 6 ^ 7 ^ 7 ^ 8 = 0 ^ 0 ^ 8 = 8
        #
        # XOR is commutative and associative, allowing nums to be unsorted:
        # a ^ b ^ c = a ^ c ^ b = (a ^ b) ^ c = a ^ (b ^ c)
        # That is, 6 ^ 7 ^ 7 ^ 6 ^ 8 = 0 ^ 0 ^ 8 = 8

        result = 0
        for num in nums:
            result ^= num
        return result


# Initialize the Solution class
solution = Solution()

# Test case 1: Single element
assert solution.singleNumber([1]) == 1, "Test case 1 failed"

# Test case 2: All elements are the same except one
assert solution.singleNumber([2, 2, 3]) == 3, "Test case 2 failed"

# Test case 3: Larger list with a single unique element
assert solution.singleNumber([4, 1, 2, 1, 2]) == 4, "Test case 3 failed"

# Test case 4: Unique element is negative
assert solution.singleNumber([-1, 1, 1, -1, -2]) == -2, "Test case 4 failed"

# Test case 5: Larger list with multiple pairs and one unique element
assert solution.singleNumber([5, 3, 5, 4, 4, 3, 7]) == 7, "Test case 5 failed"

# Test case 6: List with all negative numbers
assert solution.singleNumber([-3, -1, -2, -3, -1]) == -2, "Test case 6 failed"

# Test case 7: Empty list (although it's assumed the list always has one unique element, we test for robustness)
try:
    solution.singleNumber([])
    print("Test case 7 failed")
except Exception as e:
    print("Test case 7 passed")

print("All test cases passed!")
