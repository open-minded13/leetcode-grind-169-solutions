from typing import List

# Date of Last Practice: Dec 26, 2023 -> Feb 13, 2024
#
# Time Complexity: O(N), where N is the number of elements in the input array.
#                  The algorithm goes through the array only once.
#
# Space Complexity: O(1), as it only uses a fixed number of pointers and
#                   modifies the array in-place.
#
# Algorithm: Dutch National Flag. The algorithm can be visualized as
#            rearranging the elements in such a way that all reds are moved to the front,
#            all blues to the back, and whites naturally end up in the middle.
#            This Dutch National Flag algorithm can be more efficient in practice
#            because it only requires a single pass through the array.


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red_ptr, white_ptr, blue_ptr = 0, 0, len(nums) - 1
        while white_ptr <= blue_ptr:
            if nums[white_ptr] == 0:
                nums[red_ptr], nums[white_ptr] = nums[white_ptr], nums[red_ptr]
                red_ptr += 1
                white_ptr += 1
            elif nums[white_ptr] == 1:
                white_ptr += 1
            else:
                nums[blue_ptr], nums[white_ptr] = nums[white_ptr], nums[blue_ptr]
                blue_ptr -= 1


class Two_Pass_Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red, white, blue = 0, 0, 0
        for num in nums:
            if num == 0:
                red += 1
            elif num == 1:
                white += 1
            else:
                blue += 1
        for index in range(len(nums)):
            if red > 0:
                nums[index] = 0
                red -= 1
            elif white > 0:
                nums[index] = 1
                white -= 1
            else:
                nums[index] = 2


# Test cases
sol = Solution()
nums1 = [2, 0, 2, 1, 1, 0]
sol.sortColors(nums1)
print(nums1)  # Output should be [0,0,1,1,2,2]

nums2 = [2, 0, 1]
sol.sortColors(nums2)
print(nums2)  # Output should be [0,1,2]
