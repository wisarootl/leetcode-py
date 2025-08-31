"""Tests for TemplateGenerator file operations."""

from pathlib import Path
from unittest.mock import Mock

import pytest
import typer

from leetcode_py.tools.generator import FileOperations, TemplateGenerator


class TestTemplateGeneratorFileOps:
    """Test cases for file operations in TemplateGenerator."""

    def setup_method(self):
        """Set up test fixtures."""
        self.generator = TemplateGenerator()

    def test_generate_problem_file_not_found(self):
        """Test generate_problem when JSON file doesn't exist."""
        mock_file_ops = Mock(spec=FileOperations)
        mock_file_ops.exists.return_value = False
        generator = TemplateGenerator(file_ops=mock_file_ops)

        template_dir = Path("/test/template")
        output_dir = Path("/test/output")

        with pytest.raises(typer.Exit):
            generator.generate_problem("nonexistent.json", template_dir, output_dir, False)

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

    def test_default_file_operations_read_json_success(self):
        """Test DefaultFileOperations read_json success."""
        import json
        import tempfile

        from leetcode_py.tools.generator import DefaultFileOperations

        file_ops = DefaultFileOperations()

        with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
            test_data = {"test": "data"}
            json.dump(test_data, f)
            f.flush()

            result = file_ops.read_json(Path(f.name))
            assert result == test_data

        Path(f.name).unlink()  # Clean up

    def test_default_file_operations_read_json_error(self):
        """Test DefaultFileOperations read_json with invalid JSON."""
        import tempfile

        from leetcode_py.tools.generator import DefaultFileOperations

        file_ops = DefaultFileOperations()

        with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
            f.write("invalid json")
            f.flush()

            with pytest.raises(typer.Exit):
                file_ops.read_json(Path(f.name))

        Path(f.name).unlink()  # Clean up

    def test_default_file_operations_write_json_success(self):
        """Test DefaultFileOperations write_json success."""
        import json
        import tempfile

        from leetcode_py.tools.generator import DefaultFileOperations

        file_ops = DefaultFileOperations()

        with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
            test_data = {"test": "data"}
            file_ops.write_json(Path(f.name), test_data)

            # Verify the file was written correctly
            with open(f.name) as read_f:
                result = json.load(read_f)
                assert result == test_data

        Path(f.name).unlink()  # Clean up

    def test_default_file_operations_exists(self):
        """Test DefaultFileOperations exists method."""
        import tempfile

        from leetcode_py.tools.generator import DefaultFileOperations

        file_ops = DefaultFileOperations()

        with tempfile.NamedTemporaryFile(delete=False) as f:
            assert file_ops.exists(Path(f.name)) is True

        Path(f.name).unlink()
        assert file_ops.exists(Path(f.name)) is False
