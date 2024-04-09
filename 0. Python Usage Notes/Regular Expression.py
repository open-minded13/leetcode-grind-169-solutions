# Date of Last Practice: Dec 18, 2023 -> Dec 31, 2023 -> Jan 27, 2024 -> Mar 21, 2024

import re

# 1. Matching Digits (\d):
#    - \d matches any single digit (0-9).
pattern = r"\d"

# 2. Matching Word Characters (\w = [a-zA-Z0-9_]):
#    - \w matches any word character, which includes letters, digits, and underscore.
#    - The \w token does not include some characters that are valid in
#      the local part of email addresses, such as the period ., plus +, percent %, and hyphen -.
pattern = r"\w"

# 3. Matching White Space (\s):
#    - \s matches any whitespace character, including spaces, tabs, and newlines.
pattern = r"\s"

# 4. Matching Email Addresses (Basic):
#    - [a-zA-Z0-9._%+-]+ matches the username part of the email address.
#    - @[a-zA-Z0-9.-]+ matches the @ symbol and the domain name.
#    - \.[a-zA-Z]{2,} matches the top-level domain (TLD) with at least two characters.
pattern = r"[a-zA-Z0-9_.%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

# 5. Matching URLs (Basic):
#    - (https?|ftp):// matches either "http", "https", or "ftp".
#    - https?: The s is made optional by the ? quantifier,
#      which means the s can appear zero or one time.
#      This allows the pattern to match both "http" and "https".
#    - [^\s/$.?#]: It matches any character that is not a whitespace, /, $, ., ?, or #.
#                  Take https://www.example.com, it matches the first character of
#                  www.example.com, which is w.
#    - .: It matches any character (except newline).
#    - [^\s]*: Matches zero or more characters that are not whitespaces.
#              The * quantifier matches zero or more occurrences of the preceding character class.
pattern = r"(https?|ftp)://[^\s/$.?#].[^\s]*"

# 6. Matching Dates (MM/DD/YYYY format):
#    - ^ matches the start of the string.
#    - (0[1-9]|1[0-2]) matches the month in MM format (01-12).
#    - / matches the separator between month and day.
#    - (0[1-9]|[12][0-9]|3[01]) matches the day in DD format (01-31).
#    - / matches the separator between day and year.
#    - \d{4} matches the year in YYYY format (e.g., 2023).
#    - $ matches the end of the string.
#    - For example, without ^ and $, the regex would match 12/25/2023 in the string
#      "Christmas is on 12/25/2023 this year", but with them,
#      it would not match because the date is not the entire string.
pattern = r"^(0[1-9]|1[0-2])/(0[1-9]|[12][0-9]|3[01])/\d{4}$"

# 7. Matching Phone Numbers (U.S.):
#    - \d{3}-\d{3}-\d{4} matches the format XXX-XXX-XXXX for U.S. phone numbers.
pattern = r"\d{3}-\d{3}-\d{4}"

# 8. Matching HTML Tags (Basic):
#    - <[^>]+> matches any HTML tag, including its attributes.
#    - The + quantifier means one or more times, whereas the * quantifier means zero or more times.
pattern = r"<[^>]+>"

# 9. Matching IPv4 Addresses:
#    - (\d{1,3}\.){3} matches the first three parts of the IPv4 address (e.g., 192.168.1.).
#    - \d{1,3} matches the last part of the IPv4 address (e.g., 1).
pattern = r"(\d{1,3}\.){3}\d{1,3}"

# 10. Matching Zip Codes (U.S.):
#     - \d{5} matches the five-digit ZIP code.
#     - (-\d{4})? makes the last four digits optional (ZIP+4 format).
pattern = r"\d{5}(-\d{4})?"

# Note: These comments provide an explanation of what each regular expression does.
# You can modify and use them based on your specific text processing needs.


def demo_re_functions():
    test_string = "Example string 123 with different 456 patterns 789."

    # Key functions:

    # re.findall(pattern, string, flags=0)
    # Purpose: Finds all non-overlapping occurrences of the pattern in the string.
    # Input: Pattern (regex), string to search in.
    # Returns: List of strings (all matches).
    findall_result = re.findall(r"\d+", test_string)
    print("re.findall result:", findall_result)

    # re.finditer(pattern, string, flags=0)
    # Purpose: Similar to findall, but returns an iterator yielding match objects.
    # Input: Pattern (regex), string to search in.
    # Returns: Iterator over match objects.
    print("re.finditer results:")
    for match in re.finditer(r"\d+", test_string):
        print(" -", match.group())

    # re.sub(pattern, repl, string, count=0, flags=0)
    # Purpose: Replaces occurrences of the pattern in the string with 'repl'.
    # Input: Pattern (regex), replacement string, string to perform replacement in.
    # Returns: Modified string.
    sub_result = re.sub(r"\d+", "#", test_string)
    print("re.sub result:", sub_result)

    # re.subn(pattern, repl, string, count=0, flags=0)
    # Purpose: Like re.sub, but returns a tuple of the modified string and the number of substitutions made.
    # Input: Pattern (regex), replacement string, string to perform replacement in.
    # Returns: Tuple (modified string, number of substitutions made).
    subn_result = re.subn(r"\d+", "#", test_string)
    print("re.subn result:", subn_result)

    # re.split(pattern, string, maxsplit=0, flags=0)
    # Purpose: Splits the string by occurrences of the pattern.
    # Input: Pattern (regex), string to split.
    # Returns: List of strings resulting from the split.
    split_result = re.split(r"\s+", test_string)
    print("re.split result:", split_result)

    # Other functions:

    # re.search(pattern, string, flags=0)
    # Purpose: Searches for the FIRST occurrence of the pattern in the string.
    # Input: Pattern (regex), string to search in.
    # Returns: Match object if found; None otherwise.
    search_result = re.search(r"\d", test_string)
    print("re.search result:", search_result.group() if search_result else "No match")
    search_result = re.search(r"\d+", test_string)
    print("re.search result:", search_result.group() if search_result else "No match")

    # re.match(pattern, string, flags=0)
    # Purpose: Matches the pattern at the BEGINNING of the string.
    # Input: Pattern (regex), string to match against.
    # Returns: Match object if the beginning of the string matches the pattern; None otherwise.
    match_result = re.match(r"Example", test_string)
    print("re.match result:", match_result.group() if match_result else "No match")

    # re.fullmatch(pattern, string, flags=0)
    # Purpose: Checks if the entire string matches the pattern.
    # Input: Pattern (regex), string to match against.
    # Returns: Match object if the entire string matches; None otherwise.
    fullmatch_result = re.fullmatch(r".*789\.", test_string)
    print(
        "re.fullmatch result:",
        fullmatch_result.group() if fullmatch_result else "No match",
    )

    # Compiling a pattern for efficiency when used multiple times
    # Purpose: Compiles a regex pattern for repeated use.
    # Input: Pattern (regex).
    # Returns: Compiled regex object.
    compiled_pattern = re.compile(r"\d+")
    compiled_findall_result = compiled_pattern.findall(test_string)
    print("Compiled pattern findall result:", compiled_findall_result)


if __name__ == "__main__":
    demo_re_functions()
