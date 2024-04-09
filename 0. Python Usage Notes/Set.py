# Date of Last Practice: Oct 23, 2023 -> Feb 2, 2024 -> Mar 21, 2024

# In Python, the set() data structure is a built-in collection type that
# represents an unordered collection of unique elements.
# It is implemented using a hash table, which provides efficient insertion, deletion, and
# membership testing operations. The average time complexity of num in my_set is O(1),
# making it faster compared to iterating over a list or checking for membership in a dictionary.

new_set = set()
new_set.add(4)

# remove() will raise an error if the element is not found, while discard() will not.
new_set.remove(4)
new_set.discard(4)
new_set.clear()
if len(new_set) == 0:
    print("new_set is empty now!")

# Removing duplicates from a list: Sets are often used to eliminate duplicate elements
# from a list by converting the list to a set and then converting it back to a list.
# Since sets only store unique elements, any duplicates are automatically removed. For example:
my_list = [1, 1, 2, 4, 6, 2, 7, 8]
unique_elements = list(set(my_list))
print("Unique elements:", unique_elements)

# Checking for membership: Sets are useful for quickly checking if an element exists
# in a collection without iterating over the entire collection.
# This is particularly efficient for large collections. For example:
my_set = {1, 2, 3, 4, 5}
print("Is 2 in my_set?", 2 in my_set)
print("Is 6 in my_set?", 6 in my_set)


# Set operations: Sets support various set operations such as union, intersection, difference,
# and symmetric difference. These operations can be handy for tasks like finding common elements
# between sets, finding unique elements, or comparing sets. For example:
my_set_1 = {1, 2, 3}
my_set_2 = {3, 4, 5, 6}
print("Union:", my_set_1.union(my_set_2))
print("Intersection:", my_set_1.intersection(my_set_2))
print("Difference:", my_set_1.difference(my_set_2))
print("Symmetric Difference:", my_set_1.symmetric_difference(my_set_2))

# [Practice Makes You a Pro!]

# Removing duplicates from a list: Sets are often used to eliminate duplicate elements
# from a list by converting the list to a set and then converting it back to a list.
# Since sets only store unique elements, any duplicates are automatically removed. For example:
#
# list_1 = [1, 2, 3, 2, 3]
# unique_elements =
# print(unique_elements)

# Checking for membership: Sets are useful for quickly checking if an element exists
# in a collection without iterating over the entire collection.
# This is particularly efficient for large collections. For example:
#
# set_1 = set(list_1)

# Set operations: Sets support various set operations such as union, intersection, difference,
# and symmetric difference. These operations can be handy for tasks like finding common elements
# between sets, finding unique elements, or comparing sets. For example:
#
# set_2 = set([3, 5, 4])
# set_3 = set([3, 5, 8])
# print("Union:",)
# print("Intersection:",)
# print("Difference:",)
# print("Symmetric Difference:",)
