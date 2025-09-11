def run_trie_operations(solution_class: type, operations: list[str], inputs: list[list[str]]):
    trie = None
    results: list[bool | None] = []
    for i, op in enumerate(operations):
        if op == "Trie":
            trie = solution_class()
            results.append(None)
        elif op == "insert" and trie is not None:
            trie.insert(inputs[i][0])
            results.append(None)
        elif op == "search" and trie is not None:
            results.append(trie.search(inputs[i][0]))
        elif op == "starts_with" and trie is not None:
            results.append(trie.starts_with(inputs[i][0]))
    return results, trie


def assert_trie_operations(result: list[bool | None], expected: list[bool | None]) -> bool:
    assert result == expected
    return True
