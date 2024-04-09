# Date of Last Practice: July 1, 2023 -> Mar 20, 2024


# Create an empty dictionary
my_dict = {}

# Initialize a dictionary with keys from 'a' to 'z' and values set to 0 using a dictionary comprehension.
letter_count = {chr(i): 0 for i in range(ord("a"), ord("z") + 1)}

# Add/Update key-value pairs to the dictionary
my_dict["apple"] = 3
my_dict["banana"] = 4
my_dict["orange"] = 5

# Another way to add and update values:
my_dict = {"apple": 8, "banana": 8, "candy": 8}


# Access values using keys
print("apple is:", my_dict["apple"])

# Use the get() method to access a value with a fallback
print("guava is:", my_dict.get("guava", 0))  # If 'guava' key doesn't exist, return 0

# Check if a key exists in the dictionary
if "banana" in my_dict:
    print("banana is in my_dict")
else:
    print("banan is not in my_dict")


# Iterate over the keys and values in the dictionary
# In Python, the my_dict.items() method returns a view object that
# contains the key-value pairs of the dictionary my_dict.
# This view object can be used to iterate over the keys and values of the dictionary.
# NOTE: Though the parentheses are not strictly necessary when unpacking the tuples,
#       they can be added for clarity and readability.
for key, value in my_dict.items():
    print(key, ":", value)

# NOTE: The parentheses are strictly necessary here —— (key, value)
#       The enumerate() function is used to add an index to each iteration.
#       When you use enumerate(my_dict.items()),
#       the enumerate() function generates pairs of indices and tuples,
#       where each tuple contains a key-value pair from my_dict.items().
#       To correctly unpack the pairs of indices and tuples,
#       you need to provide the parentheses (key, value)
#       to specify the structure of the elements in each iteration.
for index, (key, value) in enumerate(my_dict.items()):
    print("Test:", index, key, value)

# Get a list of keys
# my_dict.keys() is acceptable but using my_dict directly is better.
keys = list(my_dict)
print("keys:", keys)
for key in my_dict:
    print(f"{key}")

# Get a list of values
values = list(my_dict.values())
print("values:", values)


# Remove key-value pairs:
del my_dict["banana"]
if "banana" not in my_dict:
    print("banana is not in my_dict")

# Remove a key-value pair using pop()
apple_count = my_dict.pop("apple")  # apple's value pop and store into apple_count.
print("apple_count:", apple_count)
if "apple" not in my_dict:
    print("apple is not in my_dict")


# [Practice Makes You a Pro!]

# Create an empty dictionary

# Add/Update key-value pairs to the dictionary

# Another way to add and update values:

# Access values using keys

# Use the get() method to access a value with a fallback

# Check if a key exists in the dictionary

# Iterate over the keys and values in the dictionary
# In Python, the my_dict.items() method returns a view object that
# contains the key-value pairs of the dictionary my_dict.
# This view object can be used to iterate over the keys and values of the dictionary.
# NOTE: Though the parentheses are not strictly necessary when unpacking the tuples,
#       they can be added for clarity and readability.

# NOTE: The parentheses are strictly necessary here —— (key, value)
#       The enumerate() function is used to add an index to each iteration.
#       When you use enumerate(my_dict.items()),
#       the enumerate() function generates pairs of indices and tuples,
#       where each tuple contains a key-value pair from my_dict.items().
#       To correctly unpack the pairs of indices and tuples,
#       you need to provide the parentheses (key, value)
#       to specify the structure of the elements in each iteration.

# Get a list of keys

# Get a list of values

# Remove key-value pairs:

# Remove a key-value pair using pop()
