"""
Word Count Engine.

This module contains a solution to the problem of counting words in a 
document string. The words are case-insensitive and punctuation is 
removed before counting. Words are sorted by frequency, and words with 
the same frequency retain their original order from the document.
"""

import re
from collections import defaultdict
from typing import List

# Date of Last Practice: Sep 22, 2024 -> Ocy 7, 2024
#
# Time Complexity: O(W * log W + N), where W is the number of words and N is the
#                  number of characters in the document.
#
#                  - O(N) to clean the words.
#                  - O(W) to count the words.
#                  - O(W * log W) to sort the words by frequency.
#
# Space Complexity: O(W + N), where W is the number of words and N is the number
#                   of characters in the document.
#
#                   - O(N) to store `words` and `cleaned_words`, which in the worst
#                     case would be the same size as the document.
#                   - O(W) to store the word counts.


class Solution:
    """
    Solution for counting words and returning sorted word frequencies.
    """

    def __init__(self):
        """
        Initializes the Solution class with a dictionary for word counts
        and a dictionary for word order.
        """
        self.word_counter = defaultdict(int)
        self.word_index = {}

    def _clean_word(self, word: str) -> str:
        """
        Cleans the input word by removing non-alphabetic characters.

        Args:
            word (str): The word to clean.

        Returns:
            str: The cleaned, lowercase word.
        """
        return re.sub(r"[^A-Za-z]", "", word).lower()

    def word_count_engine(self, document: str) -> List[List[str]]:
        """
        Processes the document to count word occurrences and sort by
        frequency and order of appearance.

        Args:
            document (str): The input document string.

        Returns:
            List[List[str]]: A list of word and frequency pairs, sorted
                             by frequency.
        """
        words = document.split()
        for index, word in enumerate(words):
            cleaned_word = self._clean_word(word)
            if not cleaned_word:
                continue
            self.word_counter[cleaned_word] += 1
            if cleaned_word not in self.word_index:
                self.word_index[cleaned_word] = index

        sorted_words = sorted(
            self.word_counter,
            key=lambda word: (-self.word_counter[word], self.word_index[word]),
        )
        return [[word, str(self.word_counter[word])] for word in sorted_words]


def test_word_count_engine():
    """
    Tests the word_count_engine function with multiple sample test cases.
    """
    # Test case 1
    document1 = (
        "Practice makes perfect, you'll get perfecT by practice. "
        "just practice! just just just!!"
    )
    expected_output1 = [
        ["just", "4"],
        ["practice", "3"],
        ["perfect", "2"],
        ["makes", "1"],
        ["youll", "1"],
        ["get", "1"],
        ["by", "1"],
    ]
    solution = Solution()
    assert (
        solution.word_count_engine(document1) == expected_output1
    ), "Test case 1 failed!"

    # Test case 2
    document2 = "To be, or not to be, that is the question:"
    expected_output2 = [
        ["to", "2"],
        ["be", "2"],
        ["or", "1"],
        ["not", "1"],
        ["that", "1"],
        ["is", "1"],
        ["the", "1"],
        ["question", "1"],
    ]
    solution = Solution()
    assert (
        solution.word_count_engine(document2) == expected_output2
    ), "Test case 2 failed!"

    # Test case 3
    document3 = (
        "Every book is a quotation; and every house is a quotation out "
        "of all forests, and mines, and stone quarries; and every man is a "
        "quotation from all his ancestors. "
    )
    expected_output3 = [
        ["and", "4"],
        ["every", "3"],
        ["is", "3"],
        ["a", "3"],
        ["quotation", "3"],
        ["all", "2"],
        ["book", "1"],
        ["house", "1"],
        ["out", "1"],
        ["of", "1"],
        ["forests", "1"],
        ["mines", "1"],
        ["stone", "1"],
        ["quarries", "1"],
        ["man", "1"],
        ["from", "1"],
        ["his", "1"],
        ["ancestors", "1"],
    ]
    solution = Solution()
    assert (
        solution.word_count_engine(document3) == expected_output3
    ), "Test case 3 failed!"

    # Test case 4
    document4 = (
        "I have failed over and over and over again in my life and "
        "that is why I succeed."
    )
    expected_output4 = [
        ["over", "3"],
        ["and", "3"],
        ["i", "2"],
        ["have", "1"],
        ["failed", "1"],
        ["again", "1"],
        ["in", "1"],
        ["my", "1"],
        ["life", "1"],
        ["that", "1"],
        ["is", "1"],
        ["why", "1"],
        ["succeed", "1"],
    ]
    solution = Solution()
    assert (
        solution.word_count_engine(document4) == expected_output4
    ), "Test case 4 failed!"

    # Test case 5
    document5 = (
        "Look If you had One shot, Or one opportunity, To seize "
        "everything you ever wanted, In one moment, Would you capture it, "
        "Or just let it slip?"
    )
    expected_output5 = [
        ["you", "3"],
        ["one", "3"],
        ["or", "2"],
        ["it", "2"],
        ["look", "1"],
        ["if", "1"],
        ["had", "1"],
        ["shot", "1"],
        ["opportunity", "1"],
        ["to", "1"],
        ["seize", "1"],
        ["everything", "1"],
        ["ever", "1"],
        ["wanted", "1"],
        ["in", "1"],
        ["moment", "1"],
        ["would", "1"],
        ["capture", "1"],
        ["just", "1"],
        ["let", "1"],
        ["slip", "1"],
    ]
    solution = Solution()
    assert (
        solution.word_count_engine(document5) == expected_output5
    ), "Test case 5 failed!"

    # Test case 6
    document6 = (
        "Cause I'm Slim Shady, yes I'm the real Shady, All you other Slim "
        "Shadys are just imitating So won't the real Slim Shady, please "
        "stand up, Please stand up, Please stand up"
    )
    expected_output6 = [
        ["slim", "3"],
        ["shady", "3"],
        ["please", "3"],
        ["stand", "3"],
        ["up", "3"],
        ["im", "2"],
        ["the", "2"],
        ["real", "2"],
        ["cause", "1"],
        ["yes", "1"],
        ["all", "1"],
        ["you", "1"],
        ["other", "1"],
        ["shadys", "1"],
        ["are", "1"],
        ["just", "1"],
        ["imitating", "1"],
        ["so", "1"],
        ["wont", "1"],
    ]
    solution = Solution()
    assert (
        solution.word_count_engine(document6) == expected_output6
    ), "Test case 6 failed!"

    print("All test cases passed!")


def main():
    """
    Main function to demonstrate word count engine functionality.
    """
    test_word_count_engine()


if __name__ == "__main__":
    main()
