import pytest

from leetcode_py import logged_test

from .helpers import assert_top_k_frequent, run_top_k_frequent
from .solution import Solution


class TestTopKFrequentWords:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "words, k, expected",
        [
            (["i", "love", "leetcode", "i", "love", "coding"], 2, ["i", "love"]),
            (
                ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"],
                4,
                ["the", "is", "sunny", "day"],
            ),
            (["a", "aa", "aaa"], 1, ["a"]),
            (["a", "aa", "aaa"], 2, ["a", "aa"]),
            (["a", "aa", "aaa"], 3, ["a", "aa", "aaa"]),
            (["apple", "banana", "apple"], 1, ["apple"]),
            (["apple", "banana", "apple"], 2, ["apple", "banana"]),
            (["word", "word", "word"], 1, ["word"]),
            (["a", "b", "c", "d", "e"], 3, ["a", "b", "c"]),
            (["hello", "world", "hello"], 2, ["hello", "world"]),
            (["cat", "dog", "cat", "dog", "bird"], 2, ["cat", "dog"]),
            (["x", "y", "z", "x", "y", "x"], 2, ["x", "y"]),
            (["test"], 1, ["test"]),
            (["a", "b", "a", "c", "b", "a"], 3, ["a", "b", "c"]),
            (
                ["python", "java", "python", "cpp", "java", "python"],
                3,
                ["python", "java", "cpp"],
            ),
            (["one", "two", "three", "one", "two", "one"], 2, ["one", "two"]),
            (
                ["red", "blue", "green", "red", "blue", "red"],
                3,
                ["red", "blue", "green"],
            ),
            (["same", "same", "same", "same"], 1, ["same"]),
        ],
    )
    def test_top_k_frequent(self, words: list[str], k: int, expected: list[str]):
        result = run_top_k_frequent(Solution, words, k)
        assert_top_k_frequent(result, expected)
