from typing import Any


class WordDictionary:

    # Time: O(1)
    # Space: O(1)
    def __init__(self) -> None:
        self.root: dict[str, Any] = {}

    # Time: O(m) where m = len(word)
    # Space: O(m) for new word
    def add_word(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node:
                node[char] = {}
            node = node[char]
        node["#"] = True

    # Time: O(n * 26^k) where n = len(word), k = number of dots
    # Space: O(n) for recursion stack
    def search(self, word: str) -> bool:
        def dfs(i: int, node: dict[str, Any]) -> bool:
            if i == len(word):
                return "#" in node

            char = word[i]
            if char == ".":
                for key in node:
                    if key != "#" and dfs(i + 1, node[key]):
                        return True
                return False
            else:
                return char in node and dfs(i + 1, node[char])

        return dfs(0, self.root)
