# Date of Last Practice: Dec 12, 2023 -> Feb 7, 2024
#
# Time Complexity: O(1).
#
# Space Complexity: The space complexity is O(N), where N is the number of elements
#                   pushed onto the stack. This is because, in the worst-case scenario,
#                   the elements in the stack can be in non-decreasing order,
#                   which means each element pushed onto the main stack (stack)
#                   will also be pushed onto the minimum stack (min_stack).


class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        val = self.stack.pop()
        if val == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


# Test Cases
min_stack = MinStack()
min_stack.push(-2)
min_stack.push(0)
min_stack.push(-3)
assert min_stack.getMin() == -3  # Returns -3
min_stack.pop()
assert min_stack.top() == 0  # Returns 0
assert min_stack.getMin() == -2  # Returns -2
print("All test cases passed!")
