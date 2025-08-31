from pathlib import Path
from typing import Any

from leetcode_py.tools.generator import TemplateGenerator


class TestTemplateGenerator:
    """Test cases for TemplateGenerator."""

    def setup_method(self):
        """Set up test fixtures."""
        self.generator = TemplateGenerator()

    def test_init(self):
        """Test generator initialization."""
        assert "grind-75" in self.generator.common_tags
        assert "blind-75" in self.generator.common_tags

    def test_auto_set_dummy_return_bool(self):
        """Test auto-setting dummy return for bool type."""
        data: dict[str, Any] = {"return_type": "bool"}
        result = self.generator.auto_set_dummy_return(data)
        assert result["dummy_return"] == "False"

    def test_auto_set_dummy_return_list(self):
        """Test auto-setting dummy return for list type."""
        data: dict[str, Any] = {"return_type": "list[int]"}
        result = self.generator.auto_set_dummy_return(data)
        assert result["dummy_return"] == "[]"

    def test_auto_set_dummy_return_existing(self):
        """Test that existing dummy_return is not overwritten."""
        data: dict[str, Any] = {"return_type": "bool", "dummy_return": "True"}
        result = self.generator.auto_set_dummy_return(data)
        assert result["dummy_return"] == "True"

    def test_auto_set_dummy_return_all_types(self):
        """Test auto_set_dummy_return for all supported types."""
        test_cases = [
            ("int", "0"),
            ("str", '""'),
            ("float", "0.0"),
            ("None", "None"),
            ("dict[str, int]", "{}"),
            ("set[int]", "set()"),
            ("tuple[int, str]", "()"),
            ("CustomType", "None"),  # Unknown type defaults to None
        ]

        for return_type, expected_dummy in test_cases:
            data: dict[str, Any] = {"return_type": return_type}
            result = self.generator.auto_set_dummy_return(data)
            assert result["dummy_return"] == expected_dummy

    def test_auto_set_dummy_return_no_return_type(self):
        """Test auto_set_dummy_return when no return_type is provided."""
        data: dict[str, Any] = {"problem_name": "test"}
        result = self.generator.auto_set_dummy_return(data)
        assert "dummy_return" not in result

    def test_convert_arrays_to_nested(self):
        """Test converting arrays to nested format."""
        data: dict[str, Any] = {
            "readme_examples": [{"content": "test"}],
            "tags": ["grind-75"],
            "other_field": "value",
        }

        result = self.generator.convert_arrays_to_nested(data)

        assert "_readme_examples" in result
        assert result["_readme_examples"] == {"list": [{"content": "test"}]}
        assert "_tags" in result
        assert result["_tags"] == {"list": ["grind-75"]}
        assert "readme_examples" not in result
        assert "tags" not in result
        assert result["other_field"] == "value"

    def test_convert_arrays_to_nested_partial_arrays(self):
        """Test converting only some arrays to nested format."""
        data: dict[str, Any] = {
            "solution_methods": [{"name": "test"}],
            "test_methods": [[1, 2, 3]],
            "other_list": ["not", "converted"],  # Not in array_fields
            "string_field": "value",
        }

        result = self.generator.convert_arrays_to_nested(data)

        assert "_solution_methods" in result
        assert "_test_methods" in result
        assert "other_list" in result  # Should remain unchanged
        assert result["other_list"] == ["not", "converted"]
        assert result["string_field"] == "value"

    def test_convert_arrays_to_nested_non_list_values(self):
        """Test converting arrays when field exists but is not a list."""
        data: dict[str, Any] = {"readme_examples": "not a list", "tags": None, "solution_methods": 123}

        result = self.generator.convert_arrays_to_nested(data)

        # Non-list values should remain unchanged
        assert result["readme_examples"] == "not a list"
        assert result["tags"] is None
        assert result["solution_methods"] == 123

    def test_check_overwrite_permission_force(self):
        """Test overwrite permission with force flag."""
        output_dir = Path("/fake/output")
        # Should not raise exception with force=True
        self.generator.check_overwrite_permission("test_problem", True, output_dir)

    def test_check_overwrite_permission_nonexistent_problem(self):
        """Test overwrite permission when problem doesn't exist."""
        output_dir = Path("/nonexistent/output")
        # Should not raise exception when problem doesn't exist
        self.generator.check_overwrite_permission("nonexistent_problem", False, output_dir)

    def test_check_and_prompt_tags_with_existing_tags(self):
        """Test check_and_prompt_tags when tags already exist."""
        data: dict[str, Any] = {"tags": ["existing-tag"]}
        result = self.generator.check_and_prompt_tags(data)
        assert result["tags"] == ["existing-tag"]  # Should remain unchanged

    def test_check_and_prompt_tags_no_tags_field(self):
        """Test check_and_prompt_tags when no tags field exists."""
        data: dict[str, Any] = {"problem_name": "test"}
        result = self.generator.check_and_prompt_tags(data)
        assert result == data  # Should remain unchanged

    def test_check_and_prompt_tags_non_interactive(self):
        """Test check_and_prompt_tags in non-interactive mode."""
        import io
        import sys

        # Simulate non-interactive terminal
        original_stdin = sys.stdin
        sys.stdin = io.StringIO()  # Empty stdin

        try:
            data: dict[str, Any] = {"tags": []}
            result = self.generator.check_and_prompt_tags(data)
            assert result["tags"] == []  # Should remain empty
        finally:
            sys.stdin = original_stdin

    def test_generate_problem_components(self):
        """Test individual components of problem generation."""
        # Test data processing
        data: dict[str, Any] = {"problem_name": "test", "return_type": "bool", "tags": []}

        # Test auto_set_dummy_return
        processed_data = self.generator.auto_set_dummy_return(data)
        assert processed_data["dummy_return"] == "False"

        # Test convert_arrays_to_nested
        nested_data = self.generator.convert_arrays_to_nested(processed_data)
        assert "_tags" in nested_data
        assert nested_data["_tags"] == {"list": []}

    def test_file_operations_injection(self):
        """Test that file operations can be injected for testing."""
        from unittest.mock import Mock

        from leetcode_py.tools.generator import FileOperations

        mock_file_ops = Mock(spec=FileOperations)
        generator = TemplateGenerator(file_ops=mock_file_ops)
        assert generator.file_ops is mock_file_ops

    def test_check_and_prompt_tags_interactive_valid_choices(self):
        """Test interactive tag selection with valid choices."""
        from unittest.mock import patch

        data: dict[str, Any] = {"tags": []}

        with (
            patch("sys.stdin.isatty", return_value=True),
            patch("typer.prompt", return_value="1,2"),
            patch("typer.echo"),
        ):
            result = self.generator.check_and_prompt_tags(data)
            assert "grind-75" in result["tags"]
            assert "blind-75" in result["tags"]

    def test_check_and_prompt_tags_interactive_skip(self):
        """Test interactive tag selection with skip option."""
        from unittest.mock import patch

        data: dict[str, Any] = {"tags": []}

        with (
            patch("sys.stdin.isatty", return_value=True),
            patch("typer.prompt", return_value="0"),
            patch("typer.echo"),
        ):
            result = self.generator.check_and_prompt_tags(data)
            assert result["tags"] == []

    def test_check_and_prompt_tags_interactive_invalid_input(self):
        """Test interactive tag selection with invalid input."""
        from unittest.mock import patch

        data: dict[str, Any] = {"tags": []}

        with (
            patch("sys.stdin.isatty", return_value=True),
            patch("typer.prompt", return_value="invalid"),
            patch("typer.echo"),
        ):
            result = self.generator.check_and_prompt_tags(data)
            assert result["tags"] == []

    def test_generate_problem_success(self):
        """Test successful problem generation."""
        from unittest.mock import Mock, patch

        from leetcode_py.tools.generator import FileOperations

        mock_file_ops = Mock(spec=FileOperations)
        mock_file_ops.exists.side_effect = lambda path: str(path).endswith("test.json")
        mock_file_ops.read_json.return_value = {
            "problem_name": "test_problem",
            "return_type": "bool",
            "tags": [],
        }

        generator = TemplateGenerator(file_ops=mock_file_ops)

        template_dir = Path("/test/template")
        output_dir = Path("/test/output")

        with patch("leetcode_py.tools.generator.cookiecutter", return_value=None) as mock_cookiecutter:
            generator.generate_problem("test.json", template_dir, output_dir, force=True)

            mock_file_ops.read_json.assert_called_once()
            mock_file_ops.write_json.assert_called_once()
            mock_cookiecutter.assert_called_once()
