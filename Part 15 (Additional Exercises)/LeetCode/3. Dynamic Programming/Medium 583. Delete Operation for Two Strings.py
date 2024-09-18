"""
Find the minimum number of deletion steps to make two strings the same.

This solution uses dynamic programming to calculate the minimum steps.
"""

# Date of Last Practice: Sep 17, 2024
#
# Time Complexity: O(M * N), where M and N are the lengths of the input strings.
#                  To find the minimum number of steps, we need to compare each
#                  character of both strings. This requires a nested loop, which
#                  results in a time complexity of O(M * N). The alogrithm is
#                  known as the Longest Common Subsequence (LCS).
#
# Space Complexity: O(M * N), where M and N are the lengths of the input strings.


class Solution:
    """
    Computes the minimum number of steps required to make two strings the same
    by deleting characters.
    """

    def minDistance(self, word1: str, word2: str) -> int:
        """
        Return the minimum number of steps to make word1 and word2 the same.

        Args:
            word1 (str): The first input string.
            word2 (str): The second input string.

        Returns:
            int: The minimum number of steps (deletions) required.
        """
        word1_len, word2_len = len(word1), len(word2)

        # Step 1 - Initialize DP table with the base case values
        dp = [[i + j for i in range(word1_len + 1)] for j in range(word2_len + 1)]

        # Step 2 - Fill the DP table by comparing characters of both strings
        for row in range(1, word2_len + 1):
            for col in range(1, word1_len + 1):
                if word1[col - 1] == word2[row - 1]:
                    # Step 3 - If characters match, no new deletions are needed
                    dp[row][col] = dp[row - 1][col - 1]
                else:
                    # Step 4 - Otherwise, take the minimum from either side + 1 deletion
                    dp[row][col] = min(dp[row][col - 1], dp[row - 1][col]) + 1

        # Step 5 - Return the bottom-right value of the DP table, which is the result
        return dp[word2_len][word1_len]


def test_solution():
    """
    Test cases to validate the correctness of the minDistance method.
    """
    solution = Solution()

    # Test case 1
    assert solution.minDistance("sea", "eat") == 2, "Test case 1 failed"

    # Test case 2
    assert solution.minDistance("leetcode", "etco") == 4, "Test case 2 failed"

    # Test case 3 - Edge case: identical strings
    assert solution.minDistance("abc", "abc") == 0, "Test case 3 failed"

    # Test case 4 - Edge case: empty strings
    assert solution.minDistance("", "") == 0, "Test case 4 failed"

    # Test case 5 - Edge case: one empty string
    assert solution.minDistance("abc", "") == 3, "Test case 5 failed"

    print("All test cases passed!")


if __name__ == "__main__":
    test_solution()
