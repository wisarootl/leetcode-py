import pytest

from leetcode_py.test_utils import logged_test

from .helpers import assert_median_finder, run_median_finder
from .solution import MedianFinder, MedianFinderHybrid


class TestFindMedianFromDataStream:

    @logged_test
    @pytest.mark.parametrize("solution_class", [MedianFinder, MedianFinderHybrid])
    @pytest.mark.parametrize(
        "operations, inputs, expected",
        [
            (
                ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"],
                [[], [1], [2], [], [3], []],
                [None, None, None, 1.5, None, 2.0],
            )
        ],
    )
    def test_median_finder(
        self,
        solution_class: type,
        operations: list[str],
        inputs: list[list[int]],
        expected: list[float | None],
    ):
        result, _ = run_median_finder(solution_class, operations, inputs)
        assert_median_finder(result, expected)
