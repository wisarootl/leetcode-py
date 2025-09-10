import pytest

from leetcode_py.test_utils import logged_test

from .solution import TimeMap


class TestTimeBasedKeyValueStore:
    @pytest.mark.parametrize(
        "operations, inputs, expected",
        [
            (
                ["TimeMap", "set", "get", "get", "set", "get", "get"],
                [
                    [],
                    ["foo", "bar", 1],
                    ["foo", 1],
                    ["foo", 3],
                    ["foo", "bar2", 4],
                    ["foo", 4],
                    ["foo", 5],
                ],
                [None, None, "bar", "bar", None, "bar2", "bar2"],
            )
        ],
    )
    @logged_test
    def test_time_map_operations(self, operations: list[str], inputs: list[list], expected: list):
        time_map: TimeMap | None = None
        result: list[str | None] = []
        for i, op in enumerate(operations):
            if op == "TimeMap":
                time_map = TimeMap()
                result.append(None)
            elif op == "set" and time_map is not None:
                time_map.set(*inputs[i])
                result.append(None)
            elif op == "get" and time_map is not None:
                result.append(time_map.get(*inputs[i]))
        assert result == expected
