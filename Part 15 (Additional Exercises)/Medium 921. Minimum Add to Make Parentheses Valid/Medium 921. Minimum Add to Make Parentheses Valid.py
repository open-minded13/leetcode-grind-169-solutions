# Date of Last Practice: Mar 17, 2024
#
# Time Complexity: O(N), where N is the length of the string.
#                  This is because the solution iterates through each character of
#                  the string exactly once.
#
# Space Complexity: O(1). The solution uses only a constant amount of extra space
#                   to store the variables left_parenthesis and right_parenthesis,
#                   regardless of the size of the input string.


class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        # Step 1 - Initialize counters for left and right parentheses
        left_parenthesis, right_parenthesis = 0, 0

        # Step 2 - Iterate through each character in the string
        for char in s:
            if char == "(":
                # Increment left_parenthesis for each opening parenthesis
                left_parenthesis += 1
            elif char == ")" and left_parenthesis > 0:
                # If there's an unmatched opening parenthesis, decrement it
                left_parenthesis -= 1
            else:
                # Increment right_parenthesis for each unpaired closing parenthesis
                right_parenthesis += 1

        # Step 3 - Return the sum of left_parenthesis and right_parenthesis
        return left_parenthesis + right_parenthesis


# Test cases
solution = Solution()
# Test case 1: one unmatched closing parenthesis
assert solution.minAddToMakeValid("())") == 1
# Test case 2: three unmatched opening parentheses
assert solution.minAddToMakeValid("(((") == 3
# Test case 3: mixed unmatched parentheses
assert solution.minAddToMakeValid("()))((") == 4
# Test case 4: already valid string
assert solution.minAddToMakeValid("()()") == 0
# Test case 5: empty string
assert solution.minAddToMakeValid("") == 0

print("All test cases passed.")
