"""
Solves the Word Ladder problem using two approaches: 
1. Generic form mapping + BFS (default approach).
2. Graph building + BFS.

The problem involves transforming a given word to a target word by changing 
one letter at a time, with all intermediate words existing in a given word list.
"""

from collections import defaultdict, deque
from typing import List

# Date of Last Practice: Mar 4, 2024 -> Oct 25, 2024
#
# Time Complexity: O(N * L), where N is the total number of words in the word list
#                  and L is the length of the words.
#
#                  The solution involves two main operations: Preprocessing the word
#                  list and executing a breadth-first search (BFS).
#
#                  During preprocessing, for each of the N words in the wordList, we
#                  create L generic forms by replacing each letter with a placeholder,
#                  leading to a complexity of O(N * L).
#
#                  The BFS operation also operates within O(N * L) complexity. Although
#                  we explore the possibilities by generating all generic forms (O(L))
#                  for each word and each word is a potential next step for every other
#                  word (O(N)), the early termination of BFS upon finding the first
#                  `word == endWord` ensures the overall time complexity is O(N * L).
#
#            NOTE: The graph-based approach also has the same time complexity.
#                  - The BFS algorithm processes each node (V) and its edges (E).
#                  - Here, V is N (total number of words), and E (number of edges) is
#                    bounded by N * L because each word can have up to L * 26 neighbors.
#                  - Thus, the time complexity of the BFS is O(V + E), which becomes
#                    O(N + N * L). Simplifying this gives O(N * L).
#
# Space Complexity: O(N * L), where N is the total number of words in the word list and
#                   L is the length of the words.
#
#                   The space complexity is primarily determined by the storage
#                   requirements of the generic_to_words mapping and the BFS queue.
#
#                   The generic_to_words mapping stores generic forms of the words,
#                   with up to L variations for each of the N words, leading to a
#                   space requirement of O(N * L).
#
#                   The BFS queue and the set of visited words collectively require
#                   additional space, proportional to the number of words N, but this
#                   does not exceed O(N) in the worst case.


class Solution:
    """Solution class for the Word Ladder problem with two approaches."""

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """Finds the length of the shortest transformation sequence.

        Uses a mapping of generic word forms to efficiently find words
        differing by one letter. Applies BFS to find the shortest path.

        Args:
            beginWord: The starting word.
            endWord: The target word.
            wordList: The list of words that can be used in transformations.

        Returns:
            The number of words in the shortest transformation sequence,
            or 0 if no such sequence exists.
        """
        # Step 1 - Early exit if endWord is not in the wordList
        if endWord not in wordList:
            return 0

        # Step 2 - Preprocess wordList to map generic forms to words
        generic_to_words = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                # Create a generic form by replacing each character with "_"
                generic_form = word[:i] + "_" + word[i + 1 :]
                generic_to_words[generic_form].append(word)

        # Step 3 - Perform BFS to find the shortest path from beginWord to endWord
        bfs_queue = deque([(beginWord, 1)])  # (current_word, path_length)
        visited = set([beginWord])  # Start with beginWord as visited

        while bfs_queue:
            current_word, path_length = bfs_queue.popleft()

            # Step 3.1 - If current_word is endWord, return the current path length
            if current_word == endWord:
                return path_length

            # Step 3.2 - Explore all neighbors using generic forms
            for i in range(len(current_word)):
                generic_form = current_word[:i] + "_" + current_word[i + 1 :]
                for next_word in generic_to_words[generic_form]:
                    if next_word not in visited:
                        visited.add(next_word)
                        bfs_queue.append((next_word, path_length + 1))

        # Step 4 - Return 0 if no valid transformation sequence is found
        return 0

    def ladderLengthWithGraph(
        self, beginWord: str, endWord: str, wordList: List[str]
    ) -> int:
        """Finds the length of the shortest transformation sequence using a graph.

        Constructs a graph where edges exist between words that differ by
        exactly one character, and then uses BFS to find the shortest path.

        Args:
            beginWord: The starting word.
            endWord: The target word.
            wordList: The list of words that can be used in transformations.

        Returns:
            The number of words in the shortest transformation sequence,
            or 0 if no such sequence exists.
        """
        # Step 1 - Initialize word set and graph
        word_set = set(wordList)
        if endWord not in word_set:
            return 0

        word_graph = defaultdict(list)

        # Step 2 - Define a function to find neighbors (words differing by one letter)
        def find_neighbors(word):
            """Finds all words in word_set that are one letter different."""
            for i in range(len(word)):
                for ascii_val in range(ord("a"), ord("z") + 1):
                    # Replace the ith character with each letter from 'a' to 'z'
                    new_word = word[:i] + chr(ascii_val) + word[i + 1 :]
                    if new_word != word and new_word in word_set:
                        word_graph[word].append(new_word)

        # Step 3 - Build the graph by finding neighbors for each word
        find_neighbors(beginWord)
        for word in wordList:
            find_neighbors(word)

        # Step 4 - Perform BFS to find the shortest path from beginWord to endWord
        bfs_queue = deque([(beginWord, 1)])  # (current_word, path_length)
        visited = set([beginWord])  # Start with the beginWord as visited

        while bfs_queue:
            current_word, path_length = bfs_queue.popleft()

            # Step 4.1 - If current_word is endWord, return the current path length
            if current_word == endWord:
                return path_length

            # Step 4.2 - Add unvisited neighbors to the BFS queue
            for neighbor in word_graph[current_word]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    bfs_queue.append((neighbor, path_length + 1))

        # Step 5 - Return 0 if no valid transformation sequence is found
        return 0


# Step 5 - Test cases to validate the implementation
def main():
    """
    Runs test cases for the Solution class and validates functionality.
    """
    sol = Solution()

    # Test case 1: Expected shortest transformation sequence length is 5
    assert (
        sol.ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]) == 5
    ), "Test case 1 failed"

    # Test case 2: Expected result is 0 since "cog" is not in wordList
    assert (
        sol.ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log"]) == 0
    ), "Test case 2 failed"

    # Test case 3: Single transformation
    assert (
        sol.ladderLength("hot", "dot", ["hot", "dot", "dog"]) == 2
    ), "Test case 3 failed"

    # Test case 4: Validate the graph-based approach (should have the same results)
    assert (
        sol.ladderLengthWithGraph(
            "hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]
        )
        == 5
    ), "Test case 4 failed"
    assert (
        sol.ladderLengthWithGraph("hit", "cog", ["hot", "dot", "dog", "lot", "log"])
        == 0
    ), "Test case 5 failed"
    assert (
        sol.ladderLengthWithGraph("hot", "dot", ["hot", "dot", "dog"]) == 2
    ), "Test case 6 failed"

    print("All test cases passed.")


if __name__ == "__main__":
    main()
