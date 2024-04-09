# Date of Last Practice: Sep 2, 2023 -> Dec 22, 2023 -> Jan 1, 2024 -> Mar 20, 2024

# Create a list
my_list = [1, 2, 3, 4, 5]

# Access elements in a list
print(f"my_list[0] = {my_list[0]}")
print(f"my_list[-1] = {my_list[-1]}")

# Modify elements in a list
my_list[0] = 6
print(f"my_list[0] = {my_list[0]}")

# Add elements to a list
my_list.append(8)
print(f"my_list = {my_list}")

# Remove elements from a list. If an element does not exist,
# return "ValueError: list.remove(x): x not in list"
my_list.remove(8)
print(f"my_list = {my_list}")

# Iterate over a list
for index, item in enumerate(my_list):
    print(f"my_list's item[{index}] = {item}")

# List comprehension
#
# Syntax: new_list = [expression for item in iterable if condition]
# The reason the following code doesn't work as intended is because
# the append() method expects a single element to be added to the list,
# not a generator expression.
#
# odd_numbers = []
# odd_numbers.append(item for item in my_list if item % 2 == 1)
# print(f"odd_numbers = {odd_numbers}")

squared_list = [item**2 for item in my_list]
print(f"squared_list = {squared_list}")

# List comprehension with if condition
even_numbers = [item for item in my_list if item % 2 == 0]
print(f"even_numbers = {even_numbers}")

# Sort a list
my_list.sort()
my_list.sort(reverse=True)

# Check if an element exists in a list
if 3 in my_list:
    print("The value 3 is in the list")

# Search for an element's index in a list.
# This function applies a linear search internally.
# .index(value, start_index, stop_index (not included))
index = my_list.index(3)
print(f"The value 3 is in index {index}")

# Combine two lists
list_1 = [1, 2, 3]
list_2 = ["A", "B", "C"]
combined_list = list_1 + list_2
print(combined_list)

# Initialize a 2-D matrix
matrix_2D = [[i, i + 1, i + 2] for i in range(1, 4)]
print(matrix_2D)

# Initialize another 2-D matrix
matrix_2D = [[i for i in range(2, -1, -1)] for _ in range(3)]
print(matrix_2D)

# Incorrect 2-D matrix initialization
matrix_2D = [[-1] * 3] * 4
print(matrix_2D)
matrix_2D[0][1] = 10
print(f"{matrix_2D} <- You can see that each column has been changed.")

# Create a 2-D matrix
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Access and update a 2-D matrix
print(f"matrix[0][1] = {matrix[0][1]}")
matrix[0][1] = 10
print(f"matrix[0][1] = {matrix[0][1]}")

# Delete elements from a 2-D matrix
del matrix[0][1]
print(f"matrix[0][1] = {matrix[0][1]}")
print(f"matrix = {matrix}")

# Mutable Nature of Lists in Python
# In Python, lists are mutable objects. This means that if you append
# a list directly to another list and then modify the original list,
# the changes will be reflected in the list where it was appended.
# This is because both lists are referring to the same object in memory.
# Therefore, be sure to copy a list or use list().

# Copy a list
not_a_new_list = my_list
not_a_new_list[0] = 20
print(f"not_a_new_list[0] = {not_a_new_list[0]} vs my_list[0] = {my_list[0]}")
# my_list.copy() is equal to list(my_list)
new_list = my_list.copy()
new_list[0] = 30
print(f"new_list[0] = {new_list[0]} vs my_list[0] = {my_list[0]}")

# Example: The trouble caused by not using list()
results = []
combination = [3, 5]

# Append the combination list directly
results.append(combination)
print("Results after first append:", results)  # Output: [[3, 5]]

# Modify the combination
combination.append(7)

# See the effect on results
print("Results after modifying combination:", results)  # Output: [[3, 5, 7]]

# Now, let's try with list()
results = []
combination = [3, 5]

# Append a copy of the combination
results.append(list(combination))
print("Results after first append with list():", results)  # Output: [[3, 5]]

# Modify the combination
combination.append(7)

# See the effect on results
print("Results after modifying combination:", results)  # Output: [[3, 5]]
