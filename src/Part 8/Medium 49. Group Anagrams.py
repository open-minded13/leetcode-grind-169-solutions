"""
Group anagrams from a list of strings.

This module defines a `Solution` class with a method to group anagrams
together. An anagram is a word formed by rearranging the letters of another word,
typically using all the original letters exactly once.
"""

# Date of Last Practice: Aug 24, 2024
#
# Time Complexity: O(N * K * log(K)), where N is the number of strings in the input list
#                  and K is the average length of each string. We iterate over each
#                  string in the input list, which takes O(N) time. For each string, we
#                  create a key by sorting the string, which takes O(K * log(K)) time.
#                  Thus, the overall time complexity is O(N * K * log(K)).
#
# Space Complexity: O(N * K), where N is the number of strings in the input list and K
#                   is the average length of each string. We use a dictionary to store
#                   the anagrams, where the key is the sorted string and the value is a
#                   list of anagrams.

from typing import List, Dict


class Solution:
    """
    Group anagrams from a list of strings.
    """

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Group anagrams from the given list of strings.

        Args:
            strs (List[str]): A list of strings to be grouped.

        Returns:
            List[List[str]]: A list of lists, where each inner list contains
            strings that are anagrams of each other.
        """
        # Step 1 - Initialize a dictionary to hold the anagrams
        word_dict: Dict[str, List[str]] = {}

        # Step 2 - Iterate over each string in the input list
        for string in strs:
            # Sort the string to create a key
            key = "".join(sorted(string))
            # Step 3 - Add the string to the corresponding key in the dictionary
            if key not in word_dict:
                word_dict[key] = []
            word_dict[key].append(string)

        # Step 4 - Return the grouped anagrams as a list of lists
        return [anagram for anagram in word_dict.values()]


def main():
    """
    Demonstrate the usage of the Solution class with test cases.
    """
    # Step 5 - Create an instance of the Solution class
    solution = Solution()

    # Step 6 - Test cases
    assert solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) == [
        ["eat", "tea", "ate"],
        ["tan", "nat"],
        ["bat"],
    ]

    assert solution.groupAnagrams([""]) == [[""]]

    assert solution.groupAnagrams(["a"]) == [["a"]]

    # Additional Test Case
    assert solution.groupAnagrams(["ab", "ba", "abc", "cba", "bca", "cab"]) == [
        ["ab", "ba"],
        ["abc", "cba", "bca", "cab"],
    ]

    print("All test cases passed successfully.")


if __name__ == "__main__":
    main()
