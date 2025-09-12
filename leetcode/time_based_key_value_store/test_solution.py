import pytest

from leetcode_py.test_utils import logged_test

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
            )
        ],
    )
    def test_time_map_operations(self, operations: list[str], inputs: list[list], expected: list):
        result = run_time_map_operations(TimeMap, operations, inputs)
        assert_time_map_operations(result, expected)
