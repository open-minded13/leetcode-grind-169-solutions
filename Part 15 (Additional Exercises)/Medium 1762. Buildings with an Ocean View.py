import sys

# Date of Last Practice: Mar 10, 2024
#
# Time Complexity: O(N), where N is the length of the given heights.
#                  Although there might seem to be a nested loop because
#                  we might pop multiple buildings from the stack for each building we process,
#                  each building is only ever added to and removed from the stack once.
#
# Space Complexity: O(N), where N is the length of the given heights.
#                   This would happen when all buildings can see the ocean,
#                   meaning no buildings are ever popped from the stack.
#
#                   A monotonic stack is a stack whose elements are
#                   monotonically increasing or decreasing.


class SolutionMonotonicStack:
    # This solution is for the additional limitation that
    # we can only traverse from left to right (which Meta interviews will encounter).
    def findBuildings(self, heights):
        ocean_view_buildings = []
        for index, height in enumerate(heights):
            while ocean_view_buildings and heights[ocean_view_buildings[-1]] <= height:
                ocean_view_buildings.pop()
            ocean_view_buildings.append(index)
        return ocean_view_buildings


class Solution:
    def findBuildings(self, heights):
        # Step 1: Initialize the list to store indices of ocean view buildings and the current max height
        ocean_view_buildings = []
        cur_max_height = -sys.maxsize - 1

        # Step 2: Traverse the list in reverse to identify buildings with ocean view
        index = len(heights) - 1
        for height in reversed(heights):
            if height > cur_max_height:
                # If the building has an ocean view, add its index to the list
                ocean_view_buildings.append(index)
                cur_max_height = height
            index -= 1

        # Step 3: Reverse the list to get the indices in ascending order without sorting
        return ocean_view_buildings[::-1]


# Step 4: Test cases
solution = Solution()
assert solution.findBuildings([4, 2, 3, 1]) == [0, 2, 3], "Test case 1 failed"
assert solution.findBuildings([4, 3, 2, 1]) == [0, 1, 2, 3], "Test case 2 failed"
assert solution.findBuildings([1, 3, 2, 4]) == [3], "Test case 3 failed"

print("All test cases passed successfully.")

# Initializing the solution with the monotonic stack approach
solution_monotonic_stack = SolutionMonotonicStack()
test_cases_monotonic_stack = [
    ([4, 2, 3, 1], [0, 2, 3]),
    ([4, 3, 2, 1], [0, 1, 2, 3]),
    ([1, 3, 2, 4], [3]),
]

# Running the test cases
all_passed_monotonic_stack = True
for heights, expected in test_cases_monotonic_stack:
    result_monotonic_stack = solution_monotonic_stack.findBuildings(heights)
    if result_monotonic_stack != expected:
        print(
            f"Monotonic Stack Test with heights {heights} failed. Expected {expected}, got {result_monotonic_stack}."
        )
        all_passed_monotonic_stack = False

if all_passed_monotonic_stack:
    print("Monotonic Stack: All test cases passed successfully.")
else:
    print("Monotonic Stack: Some test cases failed.")
