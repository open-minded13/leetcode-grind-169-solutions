"""
Reverse the order of words in a string while preserving original spaces.

The class `Solution` contains methods to reverse the words in a string, both with
and without preserving the original spaces. Each method ensures that only a single
space separates each word in the returned string (without preservation), or that
spaces are kept in their original positions (with preservation).

The `reverseWordsWithSpaces` is inspired by the "Sentence Reverse" exercise on the 
Exponent platform: https://www.tryexponent.com/practice/prepare/sentence-reverse

Typical usage example:
    solution = Solution()
    result1 = solution.reverseWords(" hello world ")
    result2 = solution.reverseWordsWithSpaces("  hello  world  ")
"""

# Date of Last Practice: Sep 24, 2024
#
# Time Complexity: O(N) where N is the length of the input string.
#
#                  For the `reverseWords` method:
#                  - Splitting the String (s.split()): O(N)
#                  - Reversing the List (words[::-1]): O(W), where W is the number of
#                                                      words
#                  - Joining the List (join): O(N)
#
#                  For the `reverseWordsWithSpaces` method:
#                  - Converting the String to List: O(N)
#                  - Reversing the Entire String: O(N)
#                  - Reversing Each Word: O(N)
#
# Space Complexity: O(N) where N is the length of the input string.
#
#                   For the `reverseWords` method:
#                   - Splitting the String (s.split()): O(N)
#                   - Reversing the List (words[::-1]): O(N)
#                   - Joining the List (join): O(N)
#
#                   For the `reverseWordsWithSpaces` method:
#                   - Converting the String to List: O(N)
#                   - Reversing the Entire String: O(1)
#                   - Reversing Each Word: O(1)


class Solution:
    """Class to reverse the words in a given string with two approaches."""

    def reverseWords(self, s: str) -> str:
        """
        Reverses the words in the input string `s`.

        This method ignores extra spaces and returns the reversed words
        concatenated with a single space.

        Args:
            s: A string with words to reverse.

        Returns:
            A new string with words in reverse order, separated by a single space.
        """
        # Step 1 - Split the string into words, ignoring multiple spaces
        words = s.split()

        # Step 2 - Reverse the list of words
        reversed_words = words[::-1]

        # Step 3 - Join the reversed words with a single space
        return " ".join(reversed_words)

    def reverseWordsWithSpaces(self, s: str) -> str:
        """
        Reverses the words in the input string `s` while preserving spaces.

        This method is based on the problem statement from Exponent platform:
        https://www.tryexponent.com/practice/prepare/sentence-reverse.

        Args:
            s: A string with words to reverse, including spaces.

        Returns:
            A new string with words in reverse order, preserving the original spaces.
        """
        # Step 1 - Convert string into a list of characters for mutability
        s = list(s)
        n = len(s)

        # Step 2 - Inner function to reverse a portion of the list in place
        def reverse_string(start, end):
            """Reverses characters in the list `s` from index `start` to `end`."""
            while start < end:
                s[start], s[end] = s[end], s[start]
                start += 1
                end -= 1

        # Step 3 - Reverse the entire string
        reverse_string(0, n - 1)

        # Step 4 - Reverse each word in the reversed list
        start = 0
        while start < n:
            # Skip initial spaces
            while start < n and s[start] == " ":
                start += 1
            end = start
            # Find the end of the word
            while end < n and s[end] != " ":
                end += 1
            # Reverse the current word
            reverse_string(start, end - 1)
            start = end

        # Step 5 - Join the list into a string and return
        return "".join(s)


def test_reverse_words():
    """Validate the `reverseWords` and `reverseWordsWithSpaces` methods."""
    solution = Solution()

    # Test cases for reverseWords (ignores extra spaces)
    assert solution.reverseWords("the sky is blue") == "blue is sky the"
    assert solution.reverseWords("  hello world  ") == "world hello"
    assert solution.reverseWords("a good   example") == "example good a"
    assert solution.reverseWords("   singleword   ") == "singleword"
    assert solution.reverseWords("   ") == ""
    assert solution.reverseWords("word") == "word"

    # Test cases for reverseWordsWithSpaces (preserves original spaces)
    assert solution.reverseWordsWithSpaces("  hello  world  ") == "  world  hello  "
    assert solution.reverseWordsWithSpaces("a good   example ") == " example   good a"
    assert solution.reverseWordsWithSpaces("   singleword   ") == "   singleword   "
    assert solution.reverseWordsWithSpaces("word") == "word"
    assert solution.reverseWordsWithSpaces("   ") == "   "

    print("All test cases passed!")


if __name__ == "__main__":
    # Run tests to validate the solution
    test_reverse_words()
