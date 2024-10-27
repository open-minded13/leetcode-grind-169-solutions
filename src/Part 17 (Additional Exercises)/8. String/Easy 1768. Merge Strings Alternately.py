"""
Merges two strings alternately and appends extra characters if one string is
longer than the other. Each string is composed of lowercase English letters.
"""

# Date of Last Practice: Oct 27, 2024
#
# Time Complexity: O(N), where N is the length of the longer string. We iterate
#                  through the longer string to merge the two strings.
#
# Space Complexity: O(N), where N is the length of the longer string. We store
#                   the merged string in a variable.


class Solution:
    """Merges strings by alternating characters from each input string."""

    def mergeAlternately(self, word1: str, word2: str) -> str:
        """
        Merges two strings by alternating characters from each input string.

        Alternates characters between word1 and word2. Appends remaining
        characters from the longer string at the end.

        Args:
            word1: First input string.
            word2: Second input string.

        Returns:
            Merged string with alternating characters from word1 and word2.
        """
        merged_str = ""
        ptr1, ptr2 = 0, 0  # Initialize pointers for both strings

        # Step 1 - Alternate characters until reaching the end of one string
        while ptr1 < len(word1) and ptr2 < len(word2):
            merged_str += word1[ptr1] + word2[ptr2]
            ptr1 += 1
            ptr2 += 1

        # Step 2 - Append remaining characters if word1 is longer
        if ptr1 < len(word1):
            merged_str += word1[ptr1:]

        # Step 3 - Append remaining characters if word2 is longer
        if ptr2 < len(word2):
            merged_str += word2[ptr2:]

        return merged_str


# Test cases to validate the solution
def main():
    """
    Tests the Solution class to ensure the mergeAlternately function
    performs as expected.
    """
    sol = Solution()

    # Test case 1
    assert sol.mergeAlternately("abc", "pqr") == "apbqcr", "Test case 1 failed"
    # Test case 2
    assert sol.mergeAlternately("ab", "pqrs") == "apbqrs", "Test case 2 failed"
    # Test case 3
    assert sol.mergeAlternately("abcd", "pq") == "apbqcd", "Test case 3 failed"
    # Test case 4 - Edge case: word1 and word2 are the same length
    assert sol.mergeAlternately("hello", "world") == "hweolrllod", "Test case 4 failed"
    # Test case 5 - Edge case: one character strings
    assert sol.mergeAlternately("a", "b") == "ab", "Test case 5 failed"

    print("All test cases passed.")


if __name__ == "__main__":
    main()
