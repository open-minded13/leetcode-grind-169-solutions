"""Learn to use Lambda functions in Python by practicing with examples."""

# Date of Last Practice: Mar 20, 2024 -> June 3, 2024 -> Sep 9, 2024

# [Step-by-Step Tutorial]
#
# Lambda Basics
#
# A lambda function is a small anonymous function that can take any number of arguments,
# but can only have one expression.
#
# Syntax: lambda arguments: expression

# Example 1: Simple addition
add = lambda x, y: x + y
print("Example 1: 5 + 3 =", add(5, 3))

# Working with Lists
# Lambda functions are useful for operations like sorting, filtering, and transforming
# elements in lists.

# Example 2: Sorting a list of numbers
numbers = [5, 2, 3, 1, 4]
sorted_numbers = sorted(numbers, key=lambda x: x)
print("Example 2: Sorted numbers:", sorted_numbers)

# Example 3: Sorting a list of strings by their last character
words = ["banana", "apple", "cherry"]
sorted_words = sorted(words, key=lambda s: s[-1])
print("Example 3: Words sorted by last character:", sorted_words)

# Working with Dictionaries
# You can iterate over dictionaries by keys, values, or both (items), and lambda
# functions can be especially useful for these.

# Example 4: Sorting dictionary keys by their corresponding values
ages = {"Alice": 30, "Bob": 25, "Charlie": 35}
sorted_keys = sorted(ages, key=lambda k: ages[k])
print("Example 4: Dictionary keys sorted by values:", sorted_keys)

# Example 5: Finding the dictionary key with the minimum value
min_age_key = min(ages, key=lambda k: ages[k])
print("Example 5: Key with the minimum value:", min_age_key)

# Example 6: Sorting dictionary items by value
sorted_items = sorted(ages.items(), key=lambda item: item[1])
print("Example 6: Dictionary items sorted by value:", sorted_items)

# Example 7: Finding the key-value pair with the maximum value
max_age_item = max(ages.items(), key=lambda item: item[1])
print("Example 7: Key-value pair with the maximum value:", max_age_item)


# Custom Objects Example
# Using lambda functions to sort or compare custom objects.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"{self.name}: {self.age}"


# Example 8: Sorting a list of Person objects by age
people = [Person("Alice", 30), Person("Bob", 25), Person("Charlie", 35)]
sorted_people = sorted(people, key=lambda person: person.age)
print("Example 8: People sorted by age:", sorted_people)


# [Practice Makes You a Pro!]

# Example 1: Simple addition
t, w = 3, 4

# Working with Lists
# Lambda functions are useful for operations like sorting, filtering, and transforming
# elements in lists.

# Example 2: Sorting a list of numbers
nums = [6, 5, 4, 3, 2, 1]

# Example 3: Sorting a list of strings by their last character
string_list = ["zyx", "cba", "fed"]

# Working with Dictionaries
# You can iterate over dictionaries by keys, values, or both (items), and lambda
# functions can be especially useful for these.

# Example 4: Sorting dictionary keys by their corresponding values
ages = {"Alice": 30, "Bob": 25, "Charlie": 35}

# Example 5: Finding the dictionary key with the minimum value
ages = {"Alice": 30, "Bob": 25, "Charlie": 35}

# Example 6: Sorting dictionary items by value
ages = {"Alice": 30, "Bob": 25, "Charlie": 35}

# Example 7: Finding the key-value pair with the maximum value
ages = {"Alice": 30, "Bob": 25, "Charlie": 35}


# Custom Objects Example
# Using lambda functions to sort or compare custom objects.
class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        # Return a string representation of the object
        # __repr__ is called by the repr() built-in function
        # This function is triggered when you print the object
        return f"{self.name}: {self.age}"


# Example 8: Sorting a list of Cat objects by age
cats = [Cat("Alan", 9), Cat("Bob", 6), Cat("Claire", 3)]
