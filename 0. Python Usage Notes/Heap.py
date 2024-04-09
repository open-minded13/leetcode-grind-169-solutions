# Date of Last Practice: Dec 12, 2023 -> Jan 21, 2024 -> Jan 26, 2024 -> Feb 4, 2024 -> Mar 20, 2024

import heapq

# Heapify, O(N) != Heap Operation, O(log N)
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

# Creating a Heap
# heapq.heapify(iterable): Transforms the iterable into a valid heap in-place.
# The time complexity is O(n) where n is the length of the iterable.
data = [3, 1, 4, 1, 5, 9, 2]
heapq.heapify(data)

# Pushing and Popping Elements
# heapq.heappush(heap, element): Pushes the element onto the heap and maintains the heap property.
# heapq.heappop(heap): Pops and returns the smallest element from the heap
#                      while maintaining the heap property.
heap = []
heapq.heappush(heap, 3)
heapq.heappush(heap, 1)
heapq.heappush(heap, 4)
smallest = heapq.heappop(heap)  # Returns 1
print(smallest)

# Accessing the Smallest Element Without Popping
data = [3, 1, 4, 1, 5, 9, 2]
smallest_three = heapq.nsmallest(3, data)  # Returns [1, 1, 2]
print(smallest_three)

# Merging Heaps (Note you need to add a list() before returning value)
# heapq.merge(*iterables): Merges multiple sorted inputs into a single sorted output.
#                          It takes multiple sorted iterables as arguments and
#                          returns an iterator over the sorted values.
heap1 = [1, 3, 5]
heap2 = [2, 4, 6]
merged_heap = list(heapq.merge(heap1, heap2))  # Returns [1, 2, 3, 4, 5, 6]
print(merged_heap)

# Heap Element Replacement
# heapq.heapreplace(heap, element): Pops and returns the smallest element from the heap,
#                                   then pushes the new element onto the heap.
heap = [1, 3, 5]
smallest = heapq.heapreplace(heap, 2)  # Returns 1, and heap becomes [2, 3, 5]
print(smallest)
print(heap)


# [Practice Makes You a Pro!]

# Heapify, O(N) != Heap Operation, O(log N)
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

# Creating a Heap
# heapq.heapify(iterable): Transforms the iterable into a valid heap in-place.
# The time complexity is O(n) where n is the length of the iterable.

# Pushing and Popping Elements
# heapq.heappush(heap, element): Pushes the element onto the heap and maintains the heap property.
# heapq.heappop(heap): Pops and returns the smallest element from the heap
#                      while maintaining the heap property.

# Accessing the Smallest Element Without Popping

# Merging Heaps (Note you need to add a list() before returning value)
# heapq.merge(*iterables): Merges multiple sorted inputs into a single sorted output.
#                          It takes multiple sorted iterables as arguments and
#                          returns an iterator over the sorted values.

# Heap Element Replacement
# heapq.heapreplace(heap, element): Pops and returns the smallest element from the heap,
#                                   then pushes the new element onto the heap.
