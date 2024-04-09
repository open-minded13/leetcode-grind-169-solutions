# Date of Last Practice: Dec 18, 2023 -> Feb 4, 2024
#
# Time Complexity: O(N), where N is the number of input characters
#                  (i.e., the word string for the insert and search functions and
#                   the prefix string for the startsWith function).
#
# Space Complexity: O(N*M), where N is the number of words and M is the average length of the words.
#                   In the worst case, if all words have unique characters,
#                   the space complexity can be O(N * M).
#                   However, this is a worst-case scenario and often not reached
#                   since common prefixes of different words share nodes.


class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.isEndOfWord = True

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.isEndOfWord

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True


# Instantiate the Trie
trie = Trie()

# Test insert and search
trie.insert("apple")
print(trie.search("apple"))  # Returns True
print(trie.search("app"))  # Returns False

# Test startsWith
print(trie.startsWith("app"))  # Returns True

# Insert more words and test again
trie.insert("app")
print(trie.search("app"))  # Returns True
