class Solution:

    # Time: O(C) where C is total number of characters in all words
    # Space: O(1) since at most 26 characters in alphabet
    def alien_order(self, words: list[str]) -> str:
        # Build adjacency list and in-degree count
        adj: dict[str, set[str]] = {c: set() for word in words for c in word}
        in_degree = dict.fromkeys(adj, 0)

        # Build graph by comparing adjacent words
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            min_len = min(len(w1), len(w2))

            # Check for invalid case: longer word is prefix of shorter word
            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
                return ""

            # Find first different character and add edge
            for j in range(min_len):
                if w1[j] != w2[j]:
                    if w2[j] not in adj[w1[j]]:
                        adj[w1[j]].add(w2[j])
                        in_degree[w2[j]] += 1
                    break

        # Topological sort using Kahn's algorithm
        queue = [c for c in in_degree if in_degree[c] == 0]
        result = []

        while queue:
            c = queue.pop(0)
            result.append(c)

            for neighbor in adj[c]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        # Check for cycle (invalid ordering)
        return "".join(result) if len(result) == len(in_degree) else ""
