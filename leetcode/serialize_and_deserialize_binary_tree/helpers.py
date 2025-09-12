from leetcode_py import TreeNode


def run_serialize_deserialize(solution_class: type, root_list: list[int | None]):
    root = TreeNode[int].from_list(root_list) if root_list else None
    codec = solution_class()
    serialized = codec.serialize(root)
    deserialized = codec.deserialize(serialized)
    return deserialized


def assert_serialize_deserialize(result: TreeNode[int] | None, expected_list: list[int | None]) -> bool:
    expected = TreeNode[int].from_list(expected_list) if expected_list else None
    if expected is None:
        assert result is None
    else:
        assert result is not None
        assert result.to_list() == expected.to_list()
    return True
