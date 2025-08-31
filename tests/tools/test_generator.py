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
            "examples": [{"input": "test"}],
            "tags": ["grind-75"],
            "other_field": "value",
        }

        result = self.generator.convert_arrays_to_nested(data)

        assert "_examples" in result
        assert result["_examples"] == {"list": [{"input": "test"}]}
        assert "_tags" in result
        assert result["_tags"] == {"list": ["grind-75"]}
        assert "examples" not in result
        assert "tags" not in result
        assert result["other_field"] == "value"

    def test_convert_arrays_to_nested_partial_arrays(self):
        """Test converting only some arrays to nested format."""
        data: dict[str, Any] = {
            "examples": [{"input": "test"}],
            "test_cases": [[1, 2, 3]],
            "other_list": ["not", "converted"],  # Not in array_fields
            "string_field": "value",
        }

        result = self.generator.convert_arrays_to_nested(data)

        assert "_examples" in result
        assert "_test_cases" in result
        assert "other_list" in result  # Should remain unchanged
        assert result["other_list"] == ["not", "converted"]
        assert result["string_field"] == "value"

    def test_convert_arrays_to_nested_non_list_values(self):
        """Test converting arrays when field exists but is not a list."""
        data: dict[str, Any] = {"examples": "not a list", "tags": None, "test_cases": 123}

        result = self.generator.convert_arrays_to_nested(data)

        # Non-list values should remain unchanged
        assert result["examples"] == "not a list"
        assert result["tags"] is None
        assert result["test_cases"] == 123

    def test_check_overwrite_permission_force(self):
        """Test overwrite permission with force flag."""
        template_dir = Path("/fake/template")
        # Should not raise exception with force=True
        self.generator.check_overwrite_permission("test_problem", True, template_dir)

    def test_check_overwrite_permission_nonexistent_problem(self):
        """Test overwrite permission when problem doesn't exist."""
        template_dir = Path("/nonexistent/template")
        # Should not raise exception when problem doesn't exist
        self.generator.check_overwrite_permission("nonexistent_problem", False, template_dir)

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
