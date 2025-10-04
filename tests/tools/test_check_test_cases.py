import pytest
from typer.testing import CliRunner

from leetcode_py.tools.check_test_cases import app, count_test_cases_for_problem


class TestCountTestCasesForProblem:
    @pytest.mark.parametrize(
        "json_data, expected",
        [
            (
                {
                    "test_methods": [
                        {"test_cases": {"list": ["(1, 2, 3)", "(4, 5, 6)"]}},
                        {"test_cases": {"list": ["(7, 8)"]}},
                    ]
                },
                3,
            ),
            (
                {
                    "_test_methods": {
                        "list": [
                            {"test_cases": {"list": ["(1, 2)", "(3, 4)", "(5, 6)"]}},
                            {"test_cases": {"list": ["(7, 8, 9)"]}},
                        ]
                    }
                },
                4,
            ),
            (
                {
                    "test_methods": [
                        {"test_cases": {"list": []}},
                        {"test_cases": ""},
                        {"test_cases": "   "},
                    ]
                },
                0,
            ),
            ({}, 0),
            (
                {
                    "test_methods": [
                        {
                            "test_cases": {
                                "list": ["([1, 2], 'hello', True)", "([3, 4], 'world', False)"]
                            }
                        },
                        {"test_cases": {"list": ["([], '', None)"]}},
                    ]
                },
                3,
            ),
        ],
    )
    def test_count_test_cases(self, json_data, expected):
        assert count_test_cases_for_problem(json_data) == expected

    def test_invalid_test_cases_returns_zero(self):
        """Test that invalid test cases are ignored and return 0."""
        json_data = {"test_methods": [{"test_cases": "invalid python literal"}]}
        # Current implementation ignores invalid test cases and returns 0
        assert count_test_cases_for_problem(json_data) == 0

    def test_python_expressions_in_test_cases(self):
        """Test that Python expressions like 'string' * 100 are handled correctly."""
        json_data = {
            "test_methods": [
                {
                    "test_cases": {
                        "list": ["('input', 'expected')", "('100[leetcode]', 'leetcode' * 100)"]
                    }
                }
            ]
        }
        # Should not raise an error and should count 2 test cases
        assert count_test_cases_for_problem(json_data) == 2


class TestCheckTestCases:
    def setup_method(self):
        self.runner = CliRunner()

    def test_real_json_files_can_be_parsed(self):
        """Test that all real JSON files can be parsed without errors."""
        result = self.runner.invoke(app, ["--threshold", "50", "--max", "-1"])

        # Should not crash with parsing errors
        assert "Error reading problem" not in result.stderr
        assert "malformed node or string" not in result.stderr

        # Should produce valid output
        assert "Problems with ≤50 test cases" in result.stdout

    def test_decode_string_specifically(self):
        """Test the specific decode_string.json that was causing parsing errors."""
        import json

        from leetcode_py.cli.utils.resources import get_problems_json_path

        problems_dir = get_problems_json_path()
        decode_string_file = problems_dir / "decode_string.json"

        if decode_string_file.exists():
            with open(decode_string_file) as f:
                data = json.load(f)

            # Should not raise an error when counting test cases
            count = count_test_cases_for_problem(data)
            assert count > 0  # Should have test cases
        else:
            pytest.skip("decode_string.json not found")

    def test_all_json_files_individually(self):
        """Test each JSON file individually to catch parsing issues."""
        import json

        from leetcode_py.cli.utils.resources import get_problems_json_path

        problems_dir = get_problems_json_path()
        failed_files = []

        for json_file in problems_dir.glob("*.json"):
            try:
                with open(json_file) as f:
                    data = json.load(f)
                count_test_cases_for_problem(data)
            except Exception as e:
                failed_files.append((json_file.name, str(e)))

        if failed_files:
            error_msg = "\n".join([f"{name}: {error}" for name, error in failed_files])
            pytest.fail(f"Failed to parse {len(failed_files)} JSON files:\n{error_msg}")
