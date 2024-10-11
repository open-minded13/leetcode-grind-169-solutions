from typing import List

# Date of Last Practice: Apr 29, 2024
#
# Time Complexity: O(N), where N is the length of the nums list.
#                  Since all these operations are linear and sequentially executed,
#                  the total time complexity for finding the next permutation is O(N).
#
# Space Complexity: O(1), as we only use a constant amount of extra space
#                   for a few indices and temporary variables required for swapping elements.


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Modifies nums in-place to the next lexicographical permutation.
        """
        i = len(nums) - 2

        # Step 1: Find the first index 'i' such that nums[i] < nums[i+1]
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        # Step 2: If such a pair was found
        if i >= 0:
            j = len(nums) - 1

            # Step 2: Find the first index 'j' from the end that is greater than nums[i]
            while nums[j] <= nums[i]:
                j -= 1

            # Swap elements at i and j
            nums[i], nums[j] = nums[j], nums[i]

        # Step 3: Reverse the part of the array after i
        #         To reverse, the correct expression is
        #         nums[i + 1 :] = nums[i + 1 :][::-1] (NOT nums[i+1::-1] or nums[:i:-1])
        #
        # NOTE: Strictly speaking, if we want to reverse in place without O(N) memory allocation,
        #       we need to create a reverse_in_place function.
        #       start, end = index + 1, len(nums) - 1
        #       while start < end:
        #           nums[start], nums[end] = nums[end], nums[start]
        #           start += 1
        #           end -= 1
        nums[i + 1 :] = reversed(nums[i + 1 :])


class FirstSolution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return

        def _find_visited_next_larger_num(cur_num):
            # Problem: We don't actually need this
            #          since the numbers are decremented in the visited list.
            next_larger = None
            for num, index in visited:
                if next_larger is None and num > cur_num:
                    next_larger = (num, index)
                elif cur_num < num < next_larger[0]:
                    next_larger = (num, index)
            return next_larger[0], next_larger[1]

        visited = [(nums[-1], len(nums) - 1)]
        max_num = nums[-1]
        for index in range(len(nums) - 2, -1, -1):
            cur_num = nums[index]
            if max_num > cur_num:
                new_num, new_num_index = _find_visited_next_larger_num(cur_num)
                nums[index], nums[new_num_index] = nums[new_num_index], nums[index]

                # Problem: We don't actually need to sort!
                #          Instead, the reversed() can achieve the same result.
                nums[index + 1 :] = sorted(nums[index + 1 :])
                return
            elif cur_num > max_num:
                max_num = cur_num
            visited.append((cur_num, index))

        # Problem: We don't actually need to sort!
        #          Instead, the reversed() can achieve the same result.
        # Note: Use `nums[:] = reversed(nums)` rather than `nums = reversed(nums)`
        nums.sort()
        return


# Test cases
sol = Solution()
test1 = [1, 2, 3]
sol.nextPermutation(test1)
assert test1 == [1, 3, 2], "Test case 1 failed"

test2 = [3, 2, 1]
sol.nextPermutation(test2)
assert test2 == [1, 2, 3], "Test case 2 failed"

test3 = [1, 1, 5]
sol.nextPermutation(test3)
assert test3 == [1, 5, 1], "Test case 3 failed"

test4 = [1]
sol.nextPermutation(test4)
assert test4 == [1], "Test case 4 failed"

test5 = [5, 4, 7, 5, 3, 2]
sol.nextPermutation(test5)
assert test5 == [5, 5, 2, 3, 4, 7], "Test case 5 failed"

print("All tests passed.")
