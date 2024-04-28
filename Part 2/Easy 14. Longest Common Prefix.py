from typing import List

# Date of Last Practice: Apr 28, 2024
#
# Time Complexity: O(N*L), where N is the number of strings, and
#                  L is the length of the first string in the list.
#                  This scenario occurs when the initial prefix is not
#                  significantly shortened until later strings are examined,
#                  leading to a larger number of character comparisons.
#                  For example, strs = ["long string", "long string", ...,"long string","low"]
#
#                  The best case occurs when the initial prefix is same as
#                  the string with the minimum length.
#
# Space Complexity: O(1) because the algorithm modifies the prefix in place and
#                   does not require additional storage that grows with the input size.


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        prefix = strs[0]
        for string in strs[1:]:
            while string[: len(prefix)] != prefix and prefix:
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix


class FirstSolution:
    # Time Complexity: O(NlogN) + O(M*N)
    #
    # Sorting: The solution starts by sorting the array based on the length of the strings,
    #          which takes O(NlogN), where N is the number of strings.
    #
    # Finding the Prefix: For each character in the shortest string,
    #                     it checks this character against all other strings.
    #                     The complexity of this step is (M*N),
    #                     where M is the length of the shortest string.
    #
    # The approach works correctly but might not be the most efficient,
    # particularly when the array contains strings of vastly different lengths,
    # as sorting may not be necessary

    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        strs.sort(key=lambda x: len(x))
        common_prefix = ""
        for index in range(len(strs[0])):
            candidate = strs[0][index]
            for i in range(1, len(strs)):
                if candidate != strs[i][index]:
                    return common_prefix
            common_prefix += candidate

        return common_prefix


# Test cases with assertions
sol = Solution()
assert (
    sol.longestCommonPrefix(["flower", "flow", "flight"]) == "fl"
), "Test case 1 failed"
assert sol.longestCommonPrefix(["dog", "racecar", "car"]) == "", "Test case 2 failed"
assert (
    sol.longestCommonPrefix(["interspecies", "interstellar", "interstate"]) == "inters"
), "Test case 3 failed"
assert sol.longestCommonPrefix(["throne", "throne"]) == "throne", "Test case 4 failed"
assert (
    sol.longestCommonPrefix(["prefix", "pretext", "prequel"]) == "pre"
), "Test case 5 failed"
assert sol.longestCommonPrefix([]) == "", "Test case 6 failed"
assert sol.longestCommonPrefix(["a"]) == "a", "Test case 7 failed"
assert sol.longestCommonPrefix(["", ""]) == "", "Test case 8 failed"

print("All tests passed!")
