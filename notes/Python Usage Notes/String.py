# Date of Last Practice: Jul 3, 2023 -> Mar 21, 2024


# Create strings
my_string = "Hello, world!"

# Access characters
print(my_string[0])  # Output: H

# String length
print(len(my_string))  # Output: 13

# String slicing: string[start:end], where start is inclusive, and end is exclusive.
print(my_string[0:5])

# Concatenate strings
string1 = "Hi, "
string2 = "Claire!"
print(string1 + string2)

# String methods:
#    - upper()
#    - lower()
#    - split()
#    - strip()
#    - replace()
#    - find()
#    - startswith()
#    - endswith()
my_string = " Hello, World! "
print(my_string.upper())  # Output: " HELLO, WORLD! "
print(my_string.lower())  # Output: " hello, world! "
string1, string2 = my_string.split(",")
print(string1)  # Output: " Hello"
print(string2)  # Output: " World!"
print(my_string.strip())  # Output: "Hello, World!"
print(my_string.replace("Hello", "Yo"))  # Output: " Yo, World! "
print(my_string.find("World"))  # Output: 8
print(my_string.startswith(" He"))  # Output: True
print(my_string.endswith("! "))  # Output: True

# String formatting
#    - Using % (variable1, variable2)
#    - Using .format(variable1, variable2)
#    - Using f-strings
name = "Kyle"
age = 25
print("His name is %s and he is %d years old." % (name, age))
print("His name is {} and he is {} years old.".format(name, age))
print(f"His name is {name} and he is {age} years old.")

# ^10 centers the name within a width of 10 characters.
print(f"His name is {name:^10} and he is {age} years old.")

# String joining
my_list = ["A", "B", "C"]
separator = ", "
print(separator.join(my_list))

# String iteration
text = "text"
for char in text:
    print(char)

reversed_text = text[::-1]
print(reversed_text)

# String manipulation with regular expressions
# Regular expressions (regex) allow you to perform
# powerful pattern matching and manipulation on strings.
# The re module in Python provides regex functionality.
import re

text = "Hello, my email is alice@example.com. Please contact me!"
pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"
emails = re.findall(pattern, text)
print(emails)  # Output: ['alice@example.com']

# String encoding and decoding
# You can encode and decode strings using different character encodings,
# such as UTF-8 or ASCII.
text = "Hello, world!"
encoded = text.encode("utf-8")
decoded = encoded.decode("utf-8")
print(encoded)  # Output: b'Hello, world!'
print(decoded)  # Output: 'Hello, world!'
