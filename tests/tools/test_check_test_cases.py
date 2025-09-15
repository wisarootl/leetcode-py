from unittest.mock import Mock, mock_open, patch

import pytest
from typer.testing import CliRunner

from leetcode_py.tools.check_test_cases import app, count_test_cases_for_problem


class TestCountTestCasesForProblem:
    @pytest.mark.parametrize(
        "json_data, expected",
        [
            (
                {"test_methods": [{"test_cases": "[(1, 2, 3), (4, 5, 6)]"}, {"test_cases": "[(7, 8)]"}]},
                3,
            ),
            (
                {
                    "_test_methods": {
                        "list": [
                            {"test_cases": "[(1, 2), (3, 4), (5, 6)]"},
                            {"test_cases": "[(7, 8, 9)]"},
                        ]
                    }
                },
                4,
            ),
            ({"test_methods": [{"test_cases": "[]"}, {"test_cases": ""}, {"test_cases": "   "}]}, 0),
            ({}, 0),
            (
                {
                    "test_methods": [
                        {"test_cases": "[([1, 2], 'hello', True), ([3, 4], 'world', False)]"},
                        {"test_cases": "[([], '', None)]"},
                    ]
                },
                3,
            ),
        ],
    )
    def test_count_test_cases(self, json_data, expected):
        assert count_test_cases_for_problem(json_data) == expected

    def test_invalid_test_cases_raises_error(self):
        json_data = {"test_methods": [{"test_cases": "invalid python literal"}]}
        with pytest.raises((ValueError, SyntaxError)):
            count_test_cases_for_problem(json_data)


class TestCheckTestCases:
    def setup_method(self):
        self.runner = CliRunner()

    @patch("leetcode_py.tools.check_test_cases.get_problems_json_path")
    def test_check_with_no_problems_found(self, mock_get_path):
        mock_path = Mock()
        mock_path.glob.return_value = []
        mock_get_path.return_value = mock_path

        result = self.runner.invoke(app, ["--threshold", "10"])

        assert result.exit_code == 0
        assert "Problems with ≤10 test cases (0 total):" in result.stdout

    @pytest.mark.parametrize(
        "filename, json_data, expected_exit_code, expected_output",
        [
            (
                "test_problem.json",
                {
                    "test_methods": [
                        {"test_cases": "[(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]"},
                        {"test_cases": "[(11, 12), (13, 14), (15, 16), (17, 18), (19, 20)]"},
                        {"test_cases": "[(21, 22), (23, 24), (25, 26), (27, 28), (29, 30)]"},
                    ]
                },
                0,
                "Problems with ≤10 test cases (0 total):",
            ),
            (
                "small_problem.json",
                {"test_methods": [{"test_cases": "[(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]"}]},
                1,
                "Problems with ≤10 test cases (1 total):",
            ),
        ],
    )
    @patch("leetcode_py.tools.check_test_cases.get_problems_json_path")
    @patch("builtins.open", new_callable=mock_open)
    def test_check_with_threshold(
        self, mock_file, mock_get_path, filename, json_data, expected_exit_code, expected_output
    ):
        mock_problem_file = Mock()
        mock_problem_file.name = filename
        mock_path = Mock()
        mock_path.glob.return_value = [mock_problem_file]
        mock_get_path.return_value = mock_path
        mock_file.return_value.read.return_value = ""

        with patch("json.load", return_value=json_data):
            result = self.runner.invoke(app, ["--threshold", "10"])

        assert result.exit_code == expected_exit_code
        assert expected_output in result.stdout

    @patch("leetcode_py.tools.check_test_cases.get_problems_json_path")
    @patch("builtins.open", new_callable=mock_open)
    def test_check_with_max_results_limit(self, mock_file, mock_get_path):
        mock_files = [Mock(name=f"problem_{i}.json") for i in range(5)]
        mock_path = Mock()
        mock_path.glob.return_value = mock_files
        mock_get_path.return_value = mock_path
        json_data = {"test_methods": [{"test_cases": "[(1, 2), (3, 4)]"}]}
        mock_file.return_value.read.return_value = ""

        with patch("json.load", return_value=json_data):
            result = self.runner.invoke(app, ["--threshold", "10", "--max", "2"])

        assert result.exit_code == 1
        assert "Problems with ≤10 test cases (2 total):" in result.stdout

    @pytest.mark.parametrize(
        "args, expected_exit_code, expected_output, output_stream",
        [
            (["--max", "invalid"], 1, "Invalid max_results value: invalid", "stderr"),
        ],
    )
    def test_invalid_inputs(self, args, expected_exit_code, expected_output, output_stream):
        result = self.runner.invoke(app, args)
        assert result.exit_code == expected_exit_code
        output = getattr(result, output_stream)
        assert expected_output in output

    def test_real_json_integration(self):
        """Integration test with real JSON files - should fail if any problems have ≤threshold test cases."""
        threshold = 10
        result = self.runner.invoke(app, ["--threshold", str(threshold), "--max", "-1"])

        # Extract count from output like "Problems with ≤10 test cases (X total):"
        import re

        match = re.search(rf"Problems with ≤{threshold} test cases \((\d+) total\):", result.stdout)
        assert match, f"Could not parse output: {result.stdout}"

        count = int(match.group(1))
        if count > 0:
            pytest.fail(
                f"Found {count} problems with ≤{threshold} test cases. All problems should have >{threshold} test cases."
            )
