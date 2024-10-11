"""
A module to implement two different WordDictionary data structures.

This module defines two classes: WordDictionary (Trie-based) and 
WordDictionarySet. Both classes support adding new words and finding if a string 
matches any previously added string. The search function in both classes can handle 
the dot '.' character as a wildcard that matches any letter.

Typical usage example:

    # Using the optimized Trie-based approach (preferred and scalable)
    word_dict = WordDictionary()
    word_dict.addWord("bad")
    word_dict.addWord("dad")
    word_dict.addWord("mad")
    assert word_dict.search("pad") is False
    assert word_dict.search("bad") is True
    assert word_dict.search(".ad") is True
    assert word_dict.search("b..") is True
    
    # Using the set-based approach, which performs better for LeetCode test cases
    word_dict_set = WordDictionarySet()
    word_dict_set.addWord("bad")
    word_dict_set.addWord("dad")
    word_dict_set.addWord("mad")
    assert word_dict_set.search("pad") is False
    assert word_dict_set.search("bad") is True
    assert word_dict_set.search(".ad") is True
    assert word_dict_set.search("b..") is True
"""

# Date of Last Practice: Aug 28, 2024
#
# Time Complexity: O(n) for addWord and O(26^d * n) for search, where n is the length of
#                  the word and d is the number of dots in the word. The search function
#                  calls a helper function search_trie, which recursively checks each
#                  character in the word.
#
#                  Best Case: If the word is fully matched without encountering a "."
#                             character, the time complexity is O(n), where n is the
#                             length of the word.
#
#                  Worst Case: If the word contains "." characters, the search might
#                              need to explore multiple branches at each .. In the worst
#                              case, if the word has d dots and each dot can lead to up
#                              to 26 branches (a-z), the time complexity is O(26^d * n).
#                              However, due to early stopping with any(), this is an
#                              upper bound and often the actual time is much lower.
#
# Space Complexity: O(k * n), where k is the number of words added to the dictionary and
#                   n is the average length of the words. The Trie structure stores the
#                   words in a tree-like structure, which can have up to 26 children for
#                   each node (one for each letter in the alphabet).
#
#                   The set-based approach has a space complexity of O(k * n * n), where
#                   k is the number of words added to the dictionary and n is the
#                   average length of the words. The set stores all possible variants of
#                   each word with a dot, which can be up to n variants for each word.


class TrieNode:
    """Represents a node in the Trie."""

    def __init__(self):
        """Initialize the TrieNode with children and a flag for end of word."""
        self.children = {}
        self.is_end_of_word = False


class WordDictionary:
    """
    A data structure that supports adding new words and searching with wildcards.

    The WordDictionary uses a Trie (prefix tree) for efficient storage
    and search operations. It supports adding words and searching words with
    '.' as a wildcard.
    """

    def __init__(self):
        """Initialize the WordDictionary with a root TrieNode."""
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        """
        Add a word to the WordDictionary.

        This function inserts the word into the Trie, character by character.

        Args:
            word: The word to be added to the dictionary.
        """
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.is_end_of_word = True

    def search(self, word: str) -> bool:
        """
        Search for a word in the WordDictionary.

        The search can include '.' as a wildcard character that matches any letter.

        Args:
            word: The word to search for in the dictionary.

        Returns:
            A boolean indicating whether the word or its wildcard version exists.
        """

        def search_trie(node, word_str):
            if not node:
                return False
            if not word_str:
                return node.is_end_of_word

            char = word_str[0]
            if char == ".":
                return any(
                    search_trie(child, word_str[1:]) for child in node.children.values()
                )

            return char in node.children and search_trie(
                node.children[char], word_str[1:]
            )

        return search_trie(self.root, word)


class WordDictionarySet:
    """
    A data structure that supports adding new words and searching with wildcards.

    The WordDictionarySet stores words in a set and supports searching with
    '.' as a wildcard character.
    """

    def __init__(self):
        """Initialize the WordDictionarySet with an empty set."""
        self.word_set = set()

    def addWord(self, word: str) -> None:
        """
        Add a word to the WordDictionarySet.

        This function adds the word and all possible single-dot variants to the set.

        Args:
            word: The word to be added to the dictionary.
        """
        for index in range(len(word)):
            self.word_set.add(word[:index] + "." + word[index + 1 :])
        self.word_set.add(word)

    def search(self, word: str) -> bool:
        """
        Search for a word in the WordDictionarySet.

        The search can include '.' as a wildcard character that matches any letter.

        Args:
            word: The word to search for in the dictionary.

        Returns:
            A boolean indicating whether the word or its wildcard version exists.
        """
        first_dot_index = word.find(".")

        if first_dot_index == -1:
            return word in self.word_set

        # Generate all possible variants by replacing '.' with each letter
        keys = [
            word[:first_dot_index] + chr(char) + word[first_dot_index + 1 :]
            for char in range(ord("a"), ord("z") + 1)
        ]

        # Check if any of the generated variants exist in the set
        return any(key in self.word_set for key in keys)


def main():
    """Demonstrate the usage of both WordDictionary and WordDictionarySet classes with test cases."""

    # Testing the optimized Trie-based approach (preferred)
    word_dict = WordDictionary()
    word_dict.addWord("bad")
    word_dict.addWord("dad")
    word_dict.addWord("mad")

    # Test cases for WordDictionary
    assert word_dict.search("pad") is False
    assert word_dict.search("bad") is True
    assert word_dict.search(".ad") is True
    assert word_dict.search("b..") is True

    # Testing the set-based approach
    word_dict_set = WordDictionarySet()
    word_dict_set.addWord("bad")
    word_dict_set.addWord("dad")
    word_dict_set.addWord("mad")

    # Test cases for WordDictionarySet
    assert word_dict_set.search("pad") is False
    assert word_dict_set.search("bad") is True
    assert word_dict_set.search(".ad") is True
    assert word_dict_set.search("b..") is True

    print("All test cases passed!")


if __name__ == "__main__":
    main()
