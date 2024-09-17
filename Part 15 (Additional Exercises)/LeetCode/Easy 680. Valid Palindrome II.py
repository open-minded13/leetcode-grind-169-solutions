# Date of Last Practice: Mar 11, 2024
#
# Time Complexity: O(N), where N is the lenght of the string.
#                  It only involves at most two passes through the string.
#
# Space Complexity: O(N+M+1), where N is the number of nodes in the linked list 1,
#                   The space complexity for the comparison steps where
#                   subs[::-1] is used should be considered O(n),
#                   where n is the length of the substring being checked for palindrome properties.
#                   This is because, in the worst-case scenario,
#                   the algorithm could create a substring that is nearly
#                   as long as the entire original string s,
#                   thus requiring additional space proportional to the length of s.


class Solution:
    def validPalindrome(self, s: str) -> bool:

        if s == s[::-1]:
            return True

        # Step 1 - Define a helper function to check if a substring is a palindrome
        def is_palindrome(subs: str) -> bool:
            return subs == subs[::-1]

        # Step 2 - Initialize two pointers at the start and end of the string
        left, right = 0, len(s) - 1

        # Step 3 - Move towards the center of the string
        while left < right:

            # Step 4 - Check if characters at current pointers do not match
            if s[left] != s[right]:

                # Step 5 - Check if removing one character makes it a palindrome
                return is_palindrome(s[left:right]) or is_palindrome(
                    s[left + 1 : right + 1]
                )
            left += 1
            right -= 1
        return True


# Step 6 - Test cases
sol = Solution()
assert sol.validPalindrome("aba") == True, "Test case 1 failed"
assert sol.validPalindrome("abca") == True, "Test case 2 failed"
assert sol.validPalindrome("abc") == False, "Test case 3 failed"
assert sol.validPalindrome("a") == True, "Test case 4 failed"
assert sol.validPalindrome("deeee") == True, "Test case 5 failed"

# If no assertions are raised, all test cases have passed
print("All test cases passed!")
