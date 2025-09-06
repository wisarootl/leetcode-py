from typing import Any

from leetcode_py.data_structures import DictTree


class Trie(DictTree[str]):
    END_OF_WORD = "#"

    # Time: O(1)
    # Space: O(1)
    def __init__(self) -> None:
        self.root: dict[str, Any] = {}

    # Time: O(m) where m is word length
    # Space: O(m)
    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node:
                node[char] = {}
            node = node[char]
        node[self.END_OF_WORD] = True  # End of word marker

    # Time: O(m) where m is word length
    # Space: O(1)
    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node:
                return False
            node = node[char]
        return self.END_OF_WORD in node

    # Time: O(m) where m is prefix length
    # Space: O(1)
    def starts_with(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node:
                return False
            node = node[char]
        return True
