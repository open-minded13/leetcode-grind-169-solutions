# Date of Last Practice: Dec 26, 2023 -> Dec 31, 2023 -> Mar 21, 2024

# Differences Between sort() and sorted()
# 1. Modification: sort() sorts the list in place and
#                  modifies the original list. sorted(), on the other hand,
#                  creates a new sorted list without altering the original iterable.
# 2. Return Type: sort() does not return anything (it returns None).
#                 sorted() returns a new sorted list.
# 3. Applicability: sort() is only applicable to lists.
#                   sorted() can be used with any iterable,
#                   including lists, tuples, dictionaries (by keys), and strings.

# Example demonstrating the usage of sort() and sorted() in Python.

# List for sort() method examples
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

# Sort the list in ascending order
numbers.sort()
print("Sorted in ascending order:", numbers)

# Sort the list in descending order
numbers.sort(reverse=True)
print("Sorted in descending order:", numbers)

# List of strings for sorting based on length
words = ["apple", "banana", "cherry", "date"]

# Sort words by length (shortest to longest)
words.sort(key=len)
print("Words sorted by length:", words)

# List of tuples for lambda function sorting
people = [("Alice", 25), ("Bob", 30), ("Charlie", 20)]

# Sort by age
people.sort(key=lambda x: x[1])
print("People sorted by age:", people)

# Using sorted() function on a tuple
tuple_numbers = (3, 1, 4, 1, 5)

# Sort the tuple and return a new sorted list
sorted_numbers = sorted(tuple_numbers)
print("Sorted tuple:", sorted_numbers)

# Sort the tuple in descending order
desc_sorted_numbers = sorted(tuple_numbers, reverse=True)
print("Tuple sorted in descending order:", desc_sorted_numbers)

# Using sorted() with lambda function on a dictionary
employees = {"A": 25, "B": 34, "C": 68, "D": 45}
desc_sorted_employees = dict(
    sorted(employees.items(), reverse=True, key=lambda item: item[1])
)
print("Employees sorted by age:", desc_sorted_employees)

# Wrong way (the following will only sort D, C, B, A in reverse order by key):
desc_sorted_employees = sorted(employees, reverse=True)
print("Employees sorted by key:", desc_sorted_employees)

# Using sorted() with lambda function on a list of dictionaries
employees = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 30},
    {"name": "Charlie", "age": 20},
]

# Sort employees by age
sorted_employees = sorted(employees, key=lambda x: x["age"])
print("Employees sorted by age:", sorted_employees)
