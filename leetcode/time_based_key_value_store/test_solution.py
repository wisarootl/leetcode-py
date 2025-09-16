import pytest

from leetcode_py import logged_test

from .helpers import assert_time_map_operations, run_time_map_operations
from .solution import TimeMap


class TestTimeBasedKeyValueStore:

    @logged_test
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
            ),
            (["TimeMap", "get"], [[], ["key", 1]], [None, ""]),
            (["TimeMap", "set", "get"], [[], ["a", "val", 1], ["a", 1]], [None, None, "val"]),
            (
                ["TimeMap", "set", "get", "get"],
                [[], ["key", "value", 5], ["key", 3], ["key", 7]],
                [None, None, "", "value"],
            ),
            (
                ["TimeMap", "set", "set", "get", "get", "get"],
                [[], ["x", "v1", 1], ["x", "v2", 2], ["x", 1], ["x", 2], ["x", 3]],
                [None, None, None, "v1", "v2", "v2"],
            ),
            (
                ["TimeMap", "set", "set", "set", "get", "get", "get"],
                [[], ["k", "a", 10], ["k", "b", 20], ["k", "c", 30], ["k", 15], ["k", 25], ["k", 35]],
                [None, None, None, None, "a", "b", "c"],
            ),
            (
                ["TimeMap", "set", "set", "get", "get"],
                [[], ["key1", "val1", 1], ["key2", "val2", 2], ["key1", 1], ["key2", 2]],
                [None, None, None, "val1", "val2"],
            ),
            (
                ["TimeMap", "set", "set", "set", "get", "get", "get"],
                [[], ["a", "x", 1], ["b", "y", 2], ["c", "z", 3], ["a", 1], ["b", 2], ["c", 3]],
                [None, None, None, None, "x", "y", "z"],
            ),
            (
                ["TimeMap", "set", "get", "set", "get", "set", "get"],
                [
                    [],
                    ["test", "first", 1],
                    ["test", 1],
                    ["test", "second", 100],
                    ["test", 50],
                    ["test", "third", 1000],
                    ["test", 500],
                ],
                [None, None, "first", None, "first", None, "second"],
            ),
            (
                ["TimeMap", "set", "set", "set", "set", "get"],
                [
                    [],
                    ["data", "v1", 1],
                    ["data", "v2", 10],
                    ["data", "v3", 100],
                    ["data", "v4", 1000],
                    ["data", 555],
                ],
                [None, None, None, None, None, "v3"],
            ),
            (
                ["TimeMap", "set", "get", "get", "get"],
                [[], ["single", "value", 42], ["single", 1], ["single", 42], ["single", 100]],
                [None, None, "", "value", "value"],
            ),
            (
                ["TimeMap", "set", "set", "get", "get", "get", "get"],
                [
                    [],
                    ["boundary", "min", 1],
                    ["boundary", "max", 10000000],
                    ["boundary", 0],
                    ["boundary", 1],
                    ["boundary", 5000000],
                    ["boundary", 10000000],
                ],
                [None, None, None, "", "min", "min", "max"],
            ),
        ],
    )
    def test_time_map_operations(self, operations: list[str], inputs: list[list], expected: list):
        result = run_time_map_operations(TimeMap, operations, inputs)
        assert_time_map_operations(result, expected)
