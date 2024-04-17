from collections import defaultdict, deque

# Date of Last Practice: Mar 4, 2024
#
# Time Complexity: O(N * L), where N is the total number of words in the word list
#                  and L is the length of the words.
#
#                  The solution involves two main operations:
#                  Preprocessing the word list and executing a breadth-first search (BFS).
#
#                  During preprocessing, for each of the N words in the wordList,
#                  we create L generic forms by replacing each letter with a placeholder,
#                  leading to a complexity of O(N * L).
#
#                  The BFS operation, crucial for finding the shortest transformation sequence,
#                  also operates within O(N * L) complexity. Although we explore the possibilities
#                  by generating all generic forms (O(L)) for each word
#                  and each word is a potential next step for every other word (O(N)),
#                  the early termination of BFS upon finding the first word == endWord ensures that
#                  the overall time complexity is kept to O(N * L).
#
# Space Complexity: O(N * L), where N is the total number of words in the word list
#                   and L is the length of the words.
#
#                   The space complexity is primarily determined by the storage requirements
#                   of the generic_to_words mapping and the BFS queue.
#
#                   The generic_to_words mapping stores generic forms of the words,
#                   with up to L variations for each of the N words,
#                   leading to a space requirement of O(N * L).
#
#                   The BFS queue and the set of visited words collectively
#                   require additional space, proportional to the number of words N,
#                   but this does not exceed O(N) in the worst case.


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list) -> int:
        # Step 1 - Early exit if endWord is not in the wordList
        if endWord not in wordList:
            return 0

        # Step 2 - Preprocess wordList to map generic word forms to actual words
        generic_to_words = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                generic_form = word[:i] + "_" + word[i + 1 :]
                generic_to_words[generic_form].append(word)

        # Step 3 - BFS to find the shortest transformation sequence
        bfs_queue = deque([(beginWord, 1)])
        visited = set(beginWord)

        while bfs_queue:
            current_word, path_length = bfs_queue.popleft()
            if current_word == endWord:
                return path_length

            for i in range(len(current_word)):
                generic_form = current_word[:i] + "_" + current_word[i + 1 :]
                for next_word in generic_to_words[generic_form]:
                    if next_word not in visited:
                        visited.add(next_word)
                        bfs_queue.append((next_word, path_length + 1))

        return 0


# Test cases
sol = Solution()
# Test case 1: Expected shortest transformation sequence length is 5
assert (
    sol.ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]) == 5
), "Test case 1 failed"
# Test case 2: Expected result is 0 since "cog" is not in wordList
assert (
    sol.ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log"]) == 0
), "Test case 2 failed"

print("All test cases passed!")
