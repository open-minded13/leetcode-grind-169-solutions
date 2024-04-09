import heapq
from typing import List

# Date of Last Practice: Nov 25, 2023 -> Feb 4, 2024
#
# Time Complexity: O(N * log K), where N is the number of tokens in the input list.
#                  This is because we iterate over each point, and in each iteration,
#                  we perform heap operations (i.e. heappush() and heappop())
#                  with a time complexity of log K.
#
# Space Complexity: O(N),

# Heapify != Heap Operations
# Note: Heapify, on the other hand, is a different operation.
#       Heapify is considered to have a time complexity of O(N) rather than O(N * log N) because,
#       during the bottom-up construction of the heap, each node's movement towards
#       its correct position involves a constant number of comparisons and swaps.
#       Although the overall height of the heap tree is logarithmic (O(log N)),
#       the majority of the subtrees during construction have relatively small heights.
#       This characteristic allows us to treat the heapify operation as
#       having a constant factor per node rather than a logarithmic one.
#       Consequently, the linear relationship between the number of elements (N)
#       and the total number of operations performed for heapify results in
#       a time complexity of O(N).
#       Additionally, in practical terms, the slow growth of the iterated logarithm function log* N
#       further supports treating heapify as a linear operation for realistic input sizes."


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for point in points:
            # Adding a negative sign is to simulate a max heap,
            # since Python's heapq module provides a min-heap implementation.
            dist = -(point[0] * point[0] + point[1] * point[1])
            heapq.heappush(heap, (dist, point))
            if len(heap) > k:
                heapq.heappop(heap)
        return [tuple[1] for tuple in heap]


# Test Cases
if __name__ == "__main__":
    sol = Solution()

    # Test Case 1
    points1 = [[1, 3], [-2, 2]]
    k1 = 1
    result1 = sol.kClosest(points1, k1)
    print(result1)  # Output: [[-2, 2]]

    # Test Case 2
    points2 = [[3, 3], [5, -1], [-2, 4]]
    k2 = 2
    result2 = sol.kClosest(points2, k2)
    print(result2)  # Output: [[3, 3], [-2, 4]]

    # Test Case 3
    points3 = [[1, 1], [2, 2], [3, 3]]
    k3 = 3
    result3 = sol.kClosest(points3, k3)
    print(result3)  # Output: [[1, 1], [2, 2], [3, 3]]
