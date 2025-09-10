from collections.abc import Sequence

from leetcode_py import GraphNode


def create_graph(adj_list: Sequence[Sequence[int]]) -> GraphNode | None:
    return GraphNode.from_adjacency_list(list(list(inner) for inner in adj_list))


def run_clone_graph(solution_class: type, adj_list: Sequence[Sequence[int]]) -> GraphNode | None:
    node = create_graph(adj_list)
    return solution_class().clone_graph(node)


def assert_clone_graph(result: GraphNode | None, expected: GraphNode | None) -> bool:
    if result is None and expected is None:
        assert True
    elif result is not None and expected is not None:
        assert result.is_clone(expected)
    else:
        assert False
    return True
