"""Finds the median from a data stream using a two-heap approach.

This module defines the `MedianFinder` class that allows adding numbers
to a data stream and finding the median of all numbers added so far. It 
uses two heaps (min heap and max heap) to maintain the balance of the 
elements for efficient median calculation.

Typical usage example:
    median_finder = MedianFinder()
    median_finder.addNum(1)
    median_finder.addNum(2)
    median = median_finder.findMedian()
"""

from heapq import heappush, heappop

# Date of Last Practice: Mar 29, 2024 -> Apr 15, 2024 -> Aug 7, 2024 -> Oct 23, 2024
#
# Time Complexity: O(log N), where N is the number of elements in the heap.
#                  Adding a number to a heap has a time complexity of (log N). Each call
#                  to addNum involves adding a number to a heap and possibly moving the
#                  root element (index 0) between the heaps.
#
# Space Complexity: O(N), where N is the number of elements added to the MedianFinder.
#                   This is because all elements are stored within the two heaps (low
#                   and high), and the space required grows linearly with the number of
#                   elements added.
#
# Follow-Up Questions:
#
# 1) If all integer numbers from the stream are in the range [0, 100], how would you
#    optimize your solution?
#
#    A: Use an array of size 101 to store the frequency of each number. The low and high
#       heaps are not needed in this case. The median can be calculated by iterating
#       over the frequency array and counting until reaching the middle. If the total
#       number of elements is odd, the median is the number at the middle index. If the
#       total number of elements is even, the median is the average of the two middle
#       numbers.
#
#       The time complexity of this approach is O(1) for adding a number and O(101) for
#       finding the median. The space complexity is O(101) for storing the frequency
#       array.
#
# 2) If 99% of all integer numbers from the stream are in the range [0, 100], how would
#    you optimize your solution?
#
#    A: Combine the frequency array approach for numbers within [0, 100] and use heaps
#       for outliers.
#
# NOTE: We don't need an extra counter or id to perform the operations when two values
#       are equal. We will need this if we need to store another object along with the
#       value, e.g., heap = [(1, 0, node1), (1, 1, node2)].
#
#       Check: "Hard 23. Merge k Sorted Lists".


class MedianFinder:
    """Maintains a data stream and efficiently calculates the median."""

    def __init__(self):
        """Initializes two heaps for storing the numbers."""
        self.min_heap = []  # Min heap for the upper half of the numbers.
        self.max_heap = []  # Max heap for the lower half (inverted values).

    def addNum(self, num: int) -> None:
        """Adds a number from the data stream.

        Balances the heaps to ensure that the size difference between them
        is at most one.

        Args:
            num: The number to be added to the data stream.
        """
        # Step 1 - Add to min heap, then move the smallest to max heap.
        heappush(self.min_heap, num)
        heappush(self.max_heap, -heappop(self.min_heap))

        # Step 2 - If max heap has more elements, move one back to min heap.
        if len(self.max_heap) > len(self.min_heap):
            heappush(self.min_heap, -heappop(self.max_heap))

    def findMedian(self) -> float:
        """Finds the median of all added numbers.

        Returns:
            The median of the numbers as a float. If the total number of elements
            is odd, the median is the middle element. If even, it is the average
            of the two middle elements.
        """
        # Step 3 - If min heap has more elements, return its top as the median.
        if len(self.min_heap) > len(self.max_heap):
            return self.min_heap[0]
        # Step 4 - If both heaps are equal, return the average of their tops.
        return (self.min_heap[0] + -self.max_heap[0]) / 2


def main():
    """Demonstrates the usage of the MedianFinder class with test cases."""
    median_finder = MedianFinder()

    # Test case 1
    median_finder.addNum(1)
    median_finder.addNum(2)
    assert median_finder.findMedian() == 1.5, "Test case 1 failed"

    # Test case 2
    median_finder.addNum(3)
    assert median_finder.findMedian() == 2.0, "Test case 2 failed"

    # Test case 3 - Adding more elements to check odd and even cases
    median_finder.addNum(4)
    median_finder.addNum(5)
    assert median_finder.findMedian() == 3.0, "Test case 3 failed"

    # Test case 4 - Testing negative numbers and larger range
    median_finder.addNum(-1)
    median_finder.addNum(6)
    assert median_finder.findMedian() == 3, "Test case 4 failed"

    # Test case 5 - Testing a large number of elements
    for i in range(10, 20):
        median_finder.addNum(i)
    assert median_finder.findMedian() == 11, "Test case 5 failed"

    print("All test cases passed successfully!")


if __name__ == "__main__":
    main()
