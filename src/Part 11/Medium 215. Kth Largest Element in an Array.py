from typing import List
import random
import heapq

# Date of Last Practice: Mar 13, 2024 -> Aug 6, 2024
#
# Time Complexity: O(N * log K), where N is the number of elements in the input array
#                  and K is the input integer K. We iterate through all elements in
#                  the array and perform heap operations with a time complexity of
#                  O(log K) for each element.
#
# Space Complexity: O(K), where K is the input integer K. We maintain a heap of size K.


class Solution:
    def findKthLargest(self, nums, k):
        # Step 1 - Initialize an empty heap
        heap_list = []

        # Step 2 - Iterate through all numbers in the array
        for num in nums:
            # Step 3 - Maintain a heap of size k
            heapq.heappush(heap_list, num)
            if len(heap_list) > k:
                heapq.heappop(heap_list)

        # Step 4 - The root of the heap is the kth largest element
        kth_largest = heapq.heappop(heap_list)
        return kth_largest


class QuickSelectSolution:
    # Time Complexity: O(N) in the average case and O(N^2) in the worst case.
    #
    #                  The average time complexity of the quick select is O(N),
    #                  where N is the number of elements in the input array.
    #                  This is because, on average, we reduce the problem size by half,
    #                  and N + N/2 + N/4 + ... + 1 = 2N - 1, which is O(N).
    #
    #                  In the worst case, the time complexity can be O(N^2) if the pivot
    #                  selection is not optimal and the partitioning is unbalanced.
    #
    #                  For example, [1, 2, 3, 4, 5] and we always choose the rightmost
    #                  element as the pivot. If we are going to find the 1st smallest
    #                  element, we iterate through all elements from left to right for
    #                  each pivot, resulting in N + N-1 + N-2 + ... + 1 = N*(N+1)/2
    #                  = O(N^2).
    #
    #                  For example,
    #
    #                  [1, 2, 3, 4, 5] -> [1, 2, 3, 4, 5] -> [1, 2, 3, 4, 5] -> ...
    #                               ^               ^               ^
    #                             pivot           pivot           pivot
    #
    # Space Complexity: O(1), since we do not use any extra space for the algorithm.

    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k  # Adjust k to find the (len(nums) - k)th smallest element

        def quick_select(left: int, right: int) -> int:
            if left == right:  # If the list contains only one element,
                return nums[left]  # return that element

            # Choose a pivot randomly and swap it with the end.
            # This step is not necessary but it may help to avoid worst-case time
            # complexity.
            pivot_index = random.randint(left, right)
            nums[pivot_index], nums[right] = nums[right], nums[pivot_index]

            pivot_num, cur_pivot = nums[right], left
            for i in range(left, right):
                if nums[i] <= pivot_num:
                    nums[cur_pivot], nums[i] = nums[i], nums[cur_pivot]
                    cur_pivot += 1
            nums[right], nums[cur_pivot] = nums[cur_pivot], nums[right]

            # Now cur_pivot is the position of the pivot element in the sorted array
            if cur_pivot > k:
                return quick_select(left, cur_pivot - 1)
            elif cur_pivot < k:
                return quick_select(cur_pivot + 1, right)
            else:
                return nums[cur_pivot]

        return quick_select(0, len(nums) - 1)


# Example usage
if __name__ == "__main__":
    solution = Solution()
    quick_select_solution = QuickSelectSolution()
    assert solution.findKthLargest([3, 2, 1, 5, 6, 4], 2) == 5, "Test case 1 failed"
    assert (
        solution.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4
    ), "Test case 2 failed"
    assert (
        quick_select_solution.findKthLargest([3, 2, 1, 5, 6, 4], 2) == 5
    ), "Test case 3 failed"
    assert (
        quick_select_solution.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4
    ), "Test case 4 failed"

    print("All test cases passed!")
