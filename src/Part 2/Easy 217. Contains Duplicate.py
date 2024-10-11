from typing import List

# Date of Last Practice: July 1, 2023 -> Oct 29, 2023 -> Feb 2, 2024
#
# Time Complexity: O(N), where N is the length of the "nums" list.
#
# Space Complexity: O(N). This is because when all numbers are different,
#                         we will need N extra spaces to store the numbers we see.


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            else:
                seen.add(num)
        return False


class Another_Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        unique_num_set = set(nums)
        if len(unique_num_set) == len(nums):
            return False
        else:
            return True


# Test cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1: Contains duplicate
    input1 = [1, 2, 3, 1]
    expected1 = True
    output1 = solution.containsDuplicate(input1)
    assert output1 == expected1, f"Test case 1 failed: {output1}"

    # Test case 2: No duplicates
    input2 = [1, 2, 3, 4]
    expected2 = False
    output2 = solution.containsDuplicate(input2)
    assert output2 == expected2, f"Test case 2 failed: {output2}"

    # Test case 3: Empty list
    input3 = []
    expected3 = False
    output3 = solution.containsDuplicate(input3)
    assert output3 == expected3, f"Test case 3 failed: {output3}"

    # Test case 4: Contains duplicate
    input4 = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    expected4 = True
    output4 = solution.containsDuplicate(input4)
    assert output4 == expected4, f"Test case 4 failed: {output4}"

    print("All test cases passed!")
