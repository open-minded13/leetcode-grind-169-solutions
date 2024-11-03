from typing import List

# Date of Last Practice: Apr 29, 2024 -> Nov 2, 2024
#
# Time Complexity: O(N), where N is the length of the nums list.
#                  Since all these operations are linear and sequentially executed,
#                  the total time complexity for finding the next permutation is O(N).
#
# Space Complexity: O(1), as we only use a constant amount of extra space for a few
#                   indices and temporary variables required for swapping elements.


class Solution:
    """
    Modifies a list of numbers to the next permutation in lexicographical order.

    This class implements an optimized approach that rearranges the numbers within the
    list to form the next permutation that is lexicographically greater than the current
    arrangement. If no greater permutation is possible, the list is rearranged into the
    lowest possible order.
    """

    def nextPermutation(self, nums: List[int]) -> None:
        """
        Rearranges the list `nums` to its next permutation in-place.

        Efficiently finds the next lexicographical permutation of the provided list of
        numbers. If the list is sorted in descending order, it gets rearranged to
        ascending order.

        Args:
            nums: A list of integers to find the next permutation of.
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
        # NOTE: Strictly speaking, if we want to reverse in place without O(N) memory
        #       allocation, we need to create a reverse_in_place function.
        #
        #       start, end = index + 1, len(nums) - 1
        #       while start < end:
        #           nums[start], nums[end] = nums[end], nums[start]
        #           start += 1
        #           end -= 1
        nums[i + 1 :] = reversed(nums[i + 1 :])


class FirstSolution:
    """
    Modifies a list of numbers to the next permutation in lexicographical order.

    This class demonstrates an initial approach that contains inefficiencies and
    unnecessary steps, which have been identified for learning purposes.
    """

    def nextPermutation(self, nums: List[int]) -> None:
        """
        Modifies nums in-place to the next lexicographical permutation.

        This method uses a somewhat inefficient approach with unnecessary steps:
        1. It maintains a list of visited elements to find the next greater element,
           which is not required and adds complexity.
        2. It sorts the sublist which can be replaced by a simple reversal since the
           sublist is guaranteed to be in descending order when a swap is needed.

        Args:
            nums: A list of integers to find the next permutation of.
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


def main():
    # Demonstrates the functionality using the Solution class.
    solution = Solution()
    test_cases = [
        ([1, 2, 3], [1, 3, 2]),
        ([3, 2, 1], [1, 2, 3]),
        ([1, 1, 5], [1, 5, 1]),
        ([1], [1]),
        ([5, 4, 7, 5, 3, 2], [5, 5, 2, 3, 4, 7]),
    ]

    for nums, expected in test_cases:
        solution.nextPermutation(nums)
        assert nums == expected, f"Test failed for input {nums}"
        print(f"Next permutation: {nums}")


if __name__ == "__main__":
    main()
