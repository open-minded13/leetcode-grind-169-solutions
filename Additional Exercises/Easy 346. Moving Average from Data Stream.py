from collections import deque

# Date of Last Practice: Mar 16, 2024
#
# Time Complexity: O(1). We only have a constant amount of computation.
#
# Space Complexity: O(N), where N is size and size is the maximum number of elements in the window.
#                   This is because it maintains a deque (double-ended queue)
#                   that contains at most size elements,
#                   where size is the maximum number of elements in the window.


class MovingAverage:
    # Step 1 - Initialize the class with maximum size, window, and sum tracker
    def __init__(self, size: int):
        self.max_size = size
        self.window = deque([])
        self.sum_of_window = 0

    # Step 2 - Add a new value and calculate the moving average
    def next(self, val: int) -> float:
        # If the window is full, remove the oldest value
        if len(self.window) >= self.max_size:
            self.sum_of_window -= self.window.popleft()
        # Add the new value to the window and update the sum
        self.sum_of_window += val
        self.window.append(val)
        # Return the average
        return self.sum_of_window / len(self.window)


# Step 3 - Test cases
if __name__ == "__main__":
    movingAverage = MovingAverage(3)
    # Test the functionality with provided values
    assert movingAverage.next(1) == 1.0, "Test case 1 failed"
    assert movingAverage.next(10) == 5.5, "Test case 2 failed"
    assert movingAverage.next(3) == 4.666666666666667, "Test case 3 failed"
    assert movingAverage.next(5) == 6.0, "Test case 4 failed"
    print("All test cases passed!")
