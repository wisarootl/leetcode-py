import pytest

from leetcode_py import logged_test

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
            ),
            (["MedianFinder", "addNum", "findMedian"], [[], [1], []], [None, None, 1.0]),
            (
                ["MedianFinder", "addNum", "addNum", "addNum", "findMedian"],
                [[], [1], [1], [1], []],
                [None, None, None, None, 1.0],
            ),
            (
                ["MedianFinder", "addNum", "addNum", "addNum", "addNum", "findMedian"],
                [[], [1], [2], [3], [4], []],
                [None, None, None, None, None, 2.5],
            ),
            (
                ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "addNum", "findMedian"],
                [[], [-1], [0], [], [1], [2], []],
                [None, None, None, -0.5, None, None, 0.5],
            ),
            (
                ["MedianFinder", "addNum", "addNum", "addNum", "addNum", "addNum", "findMedian"],
                [[], [5], [1], [3], [2], [4], []],
                [None, None, None, None, None, None, 3.0],
            ),
            (
                ["MedianFinder", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian"],
                [[], [100000], [], [-100000], [], [0], []],
                [None, None, 100000.0, None, 0.0, None, 0.0],
            ),
            (
                [
                    "MedianFinder",
                    "addNum",
                    "addNum",
                    "addNum",
                    "addNum",
                    "addNum",
                    "addNum",
                    "addNum",
                    "findMedian",
                ],
                [[], [10], [5], [15], [3], [7], [12], [18], []],
                [None, None, None, None, None, None, None, None, 10.0],
            ),
            (
                [
                    "MedianFinder",
                    "addNum",
                    "addNum",
                    "addNum",
                    "addNum",
                    "addNum",
                    "addNum",
                    "findMedian",
                ],
                [[], [6], [10], [2], [6], [5], [0], []],
                [None, None, None, None, None, None, None, 5.5],
            ),
            (
                [
                    "MedianFinder",
                    "addNum",
                    "addNum",
                    "addNum",
                    "addNum",
                    "addNum",
                    "addNum",
                    "addNum",
                    "addNum",
                    "findMedian",
                ],
                [[], [1], [2], [3], [4], [5], [6], [7], [8], []],
                [None, None, None, None, None, None, None, None, None, 4.5],
            ),
            (
                [
                    "MedianFinder",
                    "addNum",
                    "addNum",
                    "addNum",
                    "addNum",
                    "addNum",
                    "addNum",
                    "addNum",
                    "addNum",
                    "addNum",
                    "findMedian",
                ],
                [[], [9], [8], [7], [6], [5], [4], [3], [2], [1], []],
                [None, None, None, None, None, None, None, None, None, None, 5.0],
            ),
            (
                ["MedianFinder", "addNum", "addNum", "addNum", "addNum", "addNum", "findMedian"],
                [[], [0], [0], [0], [0], [0], []],
                [None, None, None, None, None, None, 0.0],
            ),
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
