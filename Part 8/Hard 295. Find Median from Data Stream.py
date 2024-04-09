# Date of Last Practice: Mar 29, 2024
#
# Time Complexity: O(log N), where N is the number of elements in the heap.
#                  Adding a number to a heap has a time complexity of (log N).
#                  Each call to addNum involves adding a number to a heap and
#                  possibly moving the root element (index 0) between the heaps.
#
# Space Complexity: O(N), where N is the number of elements added to the MedianFinder.
#                   This is because all elements are stored within the two heaps (low and high),
#                   and the space required grows linearly with the number of elements added.
#
# Follow-Up Questions:
#
# 1) If all integer numbers from the stream are in the range [0, 100],
#    how would you optimize your solution?
#    A: The median can be found by iterating over the array and counting until reaching the middle.
# 2) If 99% of all integer numbers from the stream are in the range [0, 100],
#    how would you optimize your solution?
#    A: Combine the frequency array approach for numbers within [0, 100] and use heaps for outliers.

import heapq
from heapq import heappush, heappop


class MedianFinder:
    def __init__(self):
        # Step 1 - Initialize two heaps: one max heap
        # (invert values for min heap behavior) and one min heap
        self.max_heap = (
            []
        )  # Max heap (Python has min heap, use negative values to simulate max heap)
        self.min_heap = []  # Min heap

    def addNum(self, num: int) -> None:
        # Step 2 - Add a new number to the data structure
        heappush(self.max_heap, -num)  # Add to max heap (invert value)
        heappush(self.min_heap, -heappop(self.max_heap))  # Balance heaps

        # If high has more elements, move one back to low
        if len(self.min_heap) > len(self.max_heap):
            heappush(self.max_heap, -heappop(self.min_heap))

    def findMedian(self) -> float:
        # Step 3 - Calculate the median
        if len(self.max_heap) > len(self.min_heap):  # If odd number of total elements
            return -self.max_heap[0]  # Top of max heap is the median
        else:  # If even number of total elements
            return (
                -self.max_heap[0] + self.min_heap[0]
            ) / 2  # Average of tops of both heaps


class FirstMedianFinder:
    # We don't need extra counters for this problem.
    # We will need a counter if you need to store another object (e.g., a tree node) with num.
    # Check "Hard 23. Merge k Sorted Lists".
    def __init__(self):
        self.max_heap = []
        self.min_heap = []
        self.counter = 0

    def addNum(self, num: int) -> None:
        if self.min_heap and num > self.min_heap[0][0]:
            heapq.heappush(self.min_heap, (num, self.counter))
        else:
            heapq.heappush(self.max_heap, (-num, self.counter))
        self.counter += 1

        if len(self.max_heap) > len(self.min_heap) + 1:
            (num, counter) = heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, (-num, counter))
        elif len(self.min_heap) > len(self.max_heap):
            (num, counter) = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, (-num, counter))

    def findMedian(self) -> float:
        if len(self.max_heap) == len(self.min_heap):
            num1, num2 = -self.max_heap[0][0], self.min_heap[0][0]
            return (num1 + num2) / 2
        else:
            num = -self.max_heap[0][0]
            return num


# Test cases
medianFinder = MedianFinder()
medianFinder.addNum(1)
medianFinder.addNum(2)
assert medianFinder.findMedian() == 1.5, "Test case 1 failed"
medianFinder.addNum(3)
assert medianFinder.findMedian() == 2.0, "Test case 2 failed"

print("All test cases passed successfully!")
