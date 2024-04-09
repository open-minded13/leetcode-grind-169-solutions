# Date of Last Practice: Jan 7, 2024 -> Feb 21, 2024
#
# Time Complexity: O(4^N), where N is the length of the input string.
#                  The number of recursive calls depends on the length of the input string.
#                  For a string of length N, each digit can correspond to at most 4 letters
#                  (like digit '7' or '9'). Therefore, in the worst-case scenario,
#                  the worst-case time complexity is O(4^N),
#                  as each level of the tree can have at most 4 branches,
#                  and the tree can be N levels deep.
#
# Space Complexity: O(N), where N is the length of the input string.
#                   The maximum depth of the recursion stack is N
#                   because the recursive function is called for each digit.


class Solution:
    def letterCombinations(self, digits: str) -> [str]:
        if not digits:
            return []

        letter_map = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }

        output = []

        def find_combinations(digit_str, combination):
            if not digit_str:
                output.append("".join(combination))
                return

            current_digit = digit_str[0]
            for letter in letter_map[current_digit]:
                find_combinations(digit_str[1:], combination + [letter])

        find_combinations(digits, [])
        return output


# Test cases
sol = Solution()

# Test case 1
assert set(sol.letterCombinations("23")) == set(
    ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
)

# Test case 2
assert sol.letterCombinations("") == []

# Test case 3
assert set(sol.letterCombinations("2")) == set(["a", "b", "c"])

# Test case with 4 digits
letter_map = {
    "2": ["a", "b", "c"],
    "3": ["d", "e", "f"],
    "4": ["g", "h", "i"],
    "5": ["j", "k", "l"],
    "6": ["m", "n", "o"],
    "7": ["p", "q", "r", "s"],
    "8": ["t", "u", "v"],
    "9": ["w", "x", "y", "z"],
}
test_case_4_digits = sol.letterCombinations("2345")
expected_combinations = [
    a + b + c + d
    for a in letter_map["2"]
    for b in letter_map["3"]
    for c in letter_map["4"]
    for d in letter_map["5"]
]
assert set(test_case_4_digits) == set(expected_combinations)

print("All Tests Passed!")
