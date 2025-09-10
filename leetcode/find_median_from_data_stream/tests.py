import pytest

from leetcode_py.test_utils import logged_test

from .solution import MedianFinder, MedianFinderHybrid


class TestFindMedianFromDataStream:
    @pytest.mark.parametrize(
        "finder_class, operations, inputs, expected",
        [
            (
                MedianFinder,
                ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"],
                [[], [1], [2], [], [3], []],
                [None, None, None, 1.5, None, 2.0],
            ),
            (
                MedianFinderHybrid,
                ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"],
                [[], [1], [2], [], [3], []],
                [None, None, None, 1.5, None, 2.0],
            ),
            (
                MedianFinder,
                ["MedianFinder", "addNum", "findMedian"],
                [[], [5], []],
                [None, None, 5.0],
            ),
            (
                MedianFinderHybrid,
                ["MedianFinder", "addNum", "findMedian"],
                [[], [5], []],
                [None, None, 5.0],
            ),
            (
                MedianFinder,
                ["MedianFinder", "addNum", "addNum", "addNum", "addNum", "findMedian"],
                [[], [1], [3], [2], [4], []],
                [None, None, None, None, None, 2.5],
            ),
            (
                MedianFinderHybrid,
                ["MedianFinder", "addNum", "addNum", "addNum", "addNum", "findMedian"],
                [[], [1], [3], [2], [4], []],
                [None, None, None, None, None, 2.5],
            ),
            (
                MedianFinderHybrid,
                ["MedianFinder", "addNum", "addNum", "addNum", "findMedian"],
                [[], [-1], [50], [101], []],
                [None, None, None, None, 50.0],
            ),
        ],
    )
    @logged_test
    def test_median_finder(
        self, finder_class, operations: list[str], inputs: list[list[int]], expected: list[float | None]
    ):
        mf = None
        results: list[float | None] = []
        for i, op in enumerate(operations):
            if op == "MedianFinder":
                mf = finder_class()
                results.append(None)
            elif op == "addNum" and mf is not None:
                mf.add_num(inputs[i][0])
                results.append(None)
            elif op == "findMedian" and mf is not None:
                results.append(mf.find_median())
        assert results == expected
