from unittest.mock import patch

import pytest

from leetcode_py.test_utils import logged_test


class TestLoggedTest:
    def test_logged_test_decorator_success(self):
        @logged_test
        def sample_test():
            return "success"

        result = sample_test()
        assert result == "success"

    def test_logged_test_decorator_failure(self):
        @logged_test
        def failing_test():
            raise ValueError("test error")

        with pytest.raises(ValueError, match="test error"):
            failing_test()

    def test_logged_test_preserves_function_metadata(self):
        @logged_test
        def sample_function():
            """Sample docstring"""
            pass

        assert sample_function.__name__ == "sample_function"
        assert sample_function.__doc__ == "Sample docstring"

    @pytest.mark.parametrize(
        "args,kwargs,expected",
        [
            ((1, 2), {"c": 3}, 6),
            ((5, 10), {}, 15),
        ],
    )
    def test_logged_test_with_arguments(self, args, kwargs, expected):
        @logged_test
        def function_with_args(a, b, c=None):
            return a + b + (c or 0)

        result = function_with_args(*args, **kwargs)
        assert result == expected

    @pytest.mark.parametrize(
        "kwargs,expected",
        [
            ({"a": 1, "b": 2, "c": 3}, 6),
            ({"x": 10, "y": 20}, 30),
        ],
    )
    def test_logged_test_with_kwargs(self, kwargs, expected):
        @logged_test
        def function_with_kwargs(**kwargs):
            return sum(kwargs.values())

        result = function_with_kwargs(**kwargs)
        assert result == expected

    @patch("builtins.print")
    def test_logged_test_prints_empty_line(self, mock_print):
        @logged_test
        def sample_test():
            return "success"

        sample_test()
        mock_print.assert_called_once_with("")
