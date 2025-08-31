"""Tests for TemplateGenerator file operations."""

import pytest

from leetcode_py.tools.generator import TemplateGenerator


class TestTemplateGeneratorFileOps:
    """Test cases for file operations in TemplateGenerator."""

    def setup_method(self):
        """Set up test fixtures."""
        self.generator = TemplateGenerator()

    def test_generate_problem_file_not_found(self):
        """Test generate_problem when JSON file doesn't exist."""
        with pytest.raises(Exception):  # typer.Exit inherits from click.exceptions.Exit
            self.generator.generate_problem("nonexistent.json", False)

    def test_auto_set_dummy_return_comprehensive(self):
        """Test all branches of auto_set_dummy_return."""
        # Test when dummy_return already exists
        data_with_dummy = {"return_type": "bool", "dummy_return": "existing"}
        result = self.generator.auto_set_dummy_return(data_with_dummy)
        assert result["dummy_return"] == "existing"

        # Test when no return_type exists
        data_no_return_type = {"problem_name": "test"}
        result = self.generator.auto_set_dummy_return(data_no_return_type)
        assert "dummy_return" not in result

        # Test all type mappings
        type_mappings = {"bool": "False", "int": "0", "str": '""', "float": "0.0", "None": "None"}

        for return_type, expected in type_mappings.items():
            data = {"return_type": return_type}
            result = self.generator.auto_set_dummy_return(data)
            assert result["dummy_return"] == expected

        # Test container types
        container_types = [
            ("list[int]", "[]"),
            ("dict[str, int]", "{}"),
            ("set[str]", "set()"),
            ("tuple[int, str]", "()"),
        ]

        for return_type, expected in container_types:
            data = {"return_type": return_type}
            result = self.generator.auto_set_dummy_return(data)
            assert result["dummy_return"] == expected

        # Test unknown type
        data_unknown = {"return_type": "UnknownType"}
        result = self.generator.auto_set_dummy_return(data_unknown)
        assert result["dummy_return"] == "None"
