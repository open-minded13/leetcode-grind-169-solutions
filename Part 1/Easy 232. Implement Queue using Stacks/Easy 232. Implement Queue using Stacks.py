# Date of Last Practice: Oct 15, 2023 -> Jan 29, 2024
#
# Time Complexity: O(N) for push() and O(1) for others.
#                  Overall, the time complexity of push() is O(N) due to its moving operations.
# Space Complexity: O(N) for push() and O(1) for others.
#                   The space complexity of push () is O(N) due to the additional space used for temp_stack.


class MyQueue:
    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        temp_stack = []
        while self.stack:
            temp_stack.append(self.stack.pop())
        temp_stack.append(x)
        while temp_stack:
            self.stack.append(temp_stack.pop())

    def pop(self) -> int:
        item = self.stack[-1]
        del self.stack[-1]
        return item

    def peek(self) -> int:
        return self.stack[-1]

    def empty(self) -> bool:
        if not self.stack:
            return True
        else:
            return False


# Test the MyQueue class
if __name__ == "__main__":
    # Create a MyQueue object
    obj = MyQueue()

    # Test the push operation
    obj.push(1)
    obj.push(2)
    obj.push(3)

    # Test the peek operation
    assert obj.peek() == 1

    # Test the pop operation
    assert obj.pop() == 1

    # Test the empty operation
    assert not obj.empty()

    # Pop the remaining elements
    assert obj.pop() == 2
    assert obj.pop() == 3

    # Check if the queue is empty
    assert obj.empty()

    print("All test cases passed!")
