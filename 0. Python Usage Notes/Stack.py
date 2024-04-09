# Date of Last Practice: Aug 31 2023 - Mar 21, 2024

# In Python, you can use the built-in list data type as a stack directly,
# without the need to create a separate Stack class.
stack_list = []
stack_list.append(0)
stack_list.append(1)
stack_list.append(2)

last_value = stack_list[-1]
print(last_value)
popped_value = stack_list.pop()
print(popped_value)
popped_value = stack_list.pop()
print(popped_value)


# Using a stack data structure with class in Python.
class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            return None
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.stack[-1]

    def size(self):
        return len(self.stack)


# Example usage:
stack = Stack()
stack.push(5)
stack.push(10)
stack.push(15)
print(stack.peek())  # Output: 15
print(stack.pop())  # Output: 15
print(stack.pop())  # Output: 10
print(stack.is_empty())  # Output: False
print(stack.size())  # Output: 1
