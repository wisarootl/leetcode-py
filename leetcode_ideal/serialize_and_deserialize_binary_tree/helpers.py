from collections.abc import Sequence

from leetcode_py import TreeNode


def create_tree(root_list: Sequence[int | None]) -> TreeNode[int] | None:
    return TreeNode[int].from_list(list(root_list)) if root_list else None


def run_serialize_deserialize(
    solution_class: type, root_list: Sequence[int | None]
) -> TreeNode[int] | None:
    root = create_tree(root_list)
    codec = solution_class()
    serialized = codec.serialize(root)
    return codec.deserialize(serialized)


def assert_serialize_deserialize(result: TreeNode[int] | None, expected: TreeNode[int] | None) -> bool:
    if result is None and expected is None:
        assert True
    elif result is not None and expected is not None:
        assert result.to_list() == expected.to_list()
    else:
        assert False
    return True
