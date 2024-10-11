# Date of Last Practice: Apr 25, 2024
#
# Time Complexity: O(N), where N is the length of the input string s.
#
# Space Complexity: O(1) as the space used by the dictionary does not
#                   depend on the input size and there are no additional
#                   data structures that scale with the input size.


class Solution:

    def romanToInt(self, s: str) -> int:
        # Dictionary for mapping Roman numerals to their integer values
        symbol_to_value = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        result = 0

        # Iterate over each character in the string except the last one
        for index, _ in enumerate(s):
            # If current value is less than the next value, subtract current value
            if (
                index < len(s) - 1
                and symbol_to_value[s[index]] < symbol_to_value[s[index + 1]]
            ):
                result -= symbol_to_value[s[index]]
            else:
                # Otherwise, add the current value
                result += symbol_to_value[s[index]]

        return result


class FirstSolution:
    def romanToInt(self, s: str) -> int:
        # Step 1: Define a dictionary with Roman numeral values including subtractive combinations
        symbol_to_value = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900,
        }

        # Step 2: Initialize the result variable to store the numerical value of the Roman numeral
        result = 0
        index = 0

        # Step 3: Iterate over each character in the input string
        while index < len(s):
            # Step 3.1: Check for a two-character subtractive combination
            if index + 1 < len(s) and s[index : index + 2] in symbol_to_value:
                result += symbol_to_value[s[index : index + 2]]
                index += 2
            else:
                # Step 3.2: Add value of the current single character
                result += symbol_to_value[s[index]]
                index += 1

        return result


# Test cases to validate the solution
sol = Solution()

assert sol.romanToInt("III") == 3
assert sol.romanToInt("LVIII") == 58
assert sol.romanToInt("MCMXCIV") == 1994
assert sol.romanToInt("IV") == 4
assert sol.romanToInt("IX") == 9
assert sol.romanToInt("XL") == 40
assert sol.romanToInt("XC") == 90
assert sol.romanToInt("CD") == 400
assert sol.romanToInt("CM") == 900
assert sol.romanToInt("MMMCMXCIX") == 3999  # Testing the upper limit

print("All tests passed.")
