import heapq

# Date of Last Practice: Mar 13, 2024
#
# Time Complexity: O(N * logK), where N is the total elements in nums, and K is the size.
#                  The main operations involved are heap insertions (heapq.heappush)
#                  and deletions (heapq.heappop). The solution iterates through
#                  each of the N elements in the given array,
#                  performing a heap insertion for each.
#                  If the heap size exceeds K, it also performs a deletion.
#
# Space Complexity: O(K), where K is the size.
#                   The solution maintains a heap of size k.
#                   Therefore, the space complexity is O(k) for storing these elements.


class Solution:
    def findKthLargest(self, nums, k):
        # Step 1 - Initialize an empty heap
        heap_list = []

        # Step 2 - Iterate through all numbers in the array
        for index, num in enumerate(nums):
            # Step 3 - Maintain a heap of size k
            heapq.heappush(heap_list, (num, index))
            if len(heap_list) > k:
                heapq.heappop(heap_list)

        # Step 4 - The root of the heap is the kth largest element
        kth_largest, _ = heapq.heappop(heap_list)
        return kth_largest


class QuickSelectSolution:
    # Reference: https://www.youtube.com/watch?v=XEmy13g1Qxc
    #
    # Time Complexity: O(N) in average and (N^2) in the worst case.
    #
    # In the average case, the partitioning step divides
    # the array into two parts that are roughly equal in size.
    # This means that each recursive call of _quick_select
    # operates on half the size of the array compared to the previous call.
    #
    # The time complexity can thus be described as:
    #
    # The first call processes the entire array: O(N).
    # The second call processes half of that: O(N/2).
    # The third call processes a quarter: O(N/4).
    # And so on...
    #
    # This series continues until the size of the processed array reduces to 1,
    # forming a series: O(N) + O(N/2) + O(N/4) + O(N/8) + ... which converges to O(2N) = O(N).
    #
    # The worst case can happen if the array is already sorted
    # (either in ascending or descending order), and
    # the pivot chosen is either the smallest or largest element each time.
    #
    # In such cases, the partitioning does not effectively reduce the problem size, leading to:
    # The first call processes the entire array: O(N).
    # The second call processes N-1 elements: O(N-1).
    # The third call processes N-2 elements: O(N-2).
    # And so on until there's only 1 element left.
    #
    # Summing these up gives a series that approximates O((N+1)*N/2), which simplifies to O(N^2).

    def findKthLargest(self, nums, k):
        k = len(nums) - k

        def _quick_select(left, right):
            pivot_index, partition_index = right, left
            for i in range(left, right):
                if nums[i] <= nums[pivot_index]:
                    nums[partition_index], nums[i] = nums[i], nums[partition_index]
                    partition_index += 1
            nums[partition_index], nums[pivot_index] = (
                nums[pivot_index],
                nums[partition_index],
            )

            if partition_index == k:
                return nums[partition_index]
            elif partition_index > k:
                return _quick_select(left, partition_index - 1)
            else:
                return _quick_select(partition_index + 1, right)

        return _quick_select(0, len(nums) - 1)


# Test cases
solution = Solution()

# Test Case 1
assert solution.findKthLargest([3, 2, 1, 5, 6, 4], 2) == 5, "Test case 1 failed"

# Test Case 2
assert (
    solution.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4
), "Test case 2 failed"

print("All test cases passed!")

# Test cases
solution = QuickSelectSolution()

# Test Case 1
assert solution.findKthLargest([3, 2, 1, 5, 6, 4], 2) == 5, "Test case 1 failed"

# Test Case 2
assert (
    solution.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4
), "Test case 2 failed"

print("All test cases passed!")
