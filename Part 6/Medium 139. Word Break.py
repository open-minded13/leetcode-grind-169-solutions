from typing import List

# Date of Last Practice: Jan 1, 2024 -> Feb 20, 2024
#
# Time Complexity: O(N^2), where N is the length of the string s.
#                  The outer loop runs N times. The inner will also run N times
#                  in the worst case when max_word_length is larger than N.
#                  Therefore, the overall time complexity is O(N^2).
#                  However, with the optimization using max_word_length,
#                  the number of iterations in the inner loop is reduced.
#
# Space Complexity: O(N), where N is the length of the string s.
#                   The space complexity is primarily due to the dp array,
#                   which has a size of O(n).


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[0] = True

        # Adding max_word_length allows you to defeat 70% of users
        # (compared to 5% without this).
        max_word_length = max(map(len, wordDict))

        # Converting wordDict into a set allows you to defeat 97% of users
        # (compared to 70% without this).
        wordDict = set(wordDict)

        for i in range(1, len(s) + 1):
            for j in range(0, i):
                if i - j <= max_word_length:
                    if dp[j] and s[j:i] in wordDict:
                        dp[i] = True
                        break
            # The following is the same but it runs longer in practice.
            # for j in range(i-1, max(i-max_word_length-1, -1), -1):
            #     if dp[j] and s[j:i] in wordDict:
            #         dp[i] = True
            #         break

        if dp[len(s)] == True:
            return True
        return False


# Test cases
solution = Solution()
assert solution.wordBreak("leetcode", ["leet", "code"]) == True
assert solution.wordBreak("applepenapple", ["apple", "pen"]) == True
assert solution.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]) == False

print("All test cases passed.")
