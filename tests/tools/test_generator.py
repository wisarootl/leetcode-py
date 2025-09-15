import json
import shutil
import tempfile
from pathlib import Path

import pytest
import typer

from leetcode_py.cli.utils.resources import get_problems_json_path, get_template_path
from leetcode_py.tools.generator import check_problem_exists, generate_problem, load_json_data


class TestGenerator:

    def test_load_json_data_success(self):
        with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=True) as f:
            json.dump({"problem_name": "test"}, f)
            f.flush()
            json_path = Path(f.name)

            data = load_json_data(json_path)
            assert data == {"problem_name": "test"}

    def test_load_json_data_real_file(self):
        real_json_path = get_problems_json_path() / "two_sum.json"

        data = load_json_data(real_json_path)

        assert data["problem_name"] == "two_sum"
        assert data["solution_class_name"] == "Solution"
        assert data["problem_number"] == "1"
        assert data["problem_title"] == "Two Sum"

    def test_load_json_data_file_not_found(self):
        with pytest.raises(typer.Exit):
            load_json_data(Path("/nonexistent/file.json"))

    def test_load_json_data_invalid_json(self):
        with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=True) as f:
            f.write("invalid json")
            f.flush()
            json_path = Path(f.name)

            with pytest.raises(typer.Exit):
                load_json_data(json_path)

    def test_check_problem_exists_force_true(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            output_dir = Path(temp_dir)
            problem_dir = output_dir / "test_problem"
            problem_dir.mkdir()

            # Should not raise with force=True
            check_problem_exists("test_problem", output_dir, force=True)

    def test_check_problem_exists_no_conflict(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            output_dir = Path(temp_dir)

            # Should not raise when problem doesn't exist
            check_problem_exists("nonexistent_problem", output_dir, force=False)

    def test_check_problem_exists_conflict(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            output_dir = Path(temp_dir)
            problem_dir = output_dir / "test_problem"
            problem_dir.mkdir()

            with pytest.raises(typer.Exit):
                check_problem_exists("test_problem", output_dir, force=False)

    def test_generate_problem_real_integration(self):
        # Use real paths from the project
        real_json_path = get_problems_json_path() / "two_sum.json"
        real_template_path = get_template_path()

        with tempfile.TemporaryDirectory() as temp_dir:
            # Copy real JSON to temp location
            temp_json = Path(temp_dir) / "two_sum.json"
            shutil.copy2(real_json_path, temp_json)

            # Copy entire template directory (including cookiecutter.json)
            temp_template = Path(temp_dir) / "template"
            shutil.copytree(real_template_path, temp_template)

            output_dir = Path(temp_dir) / "output"
            output_dir.mkdir()

            # Generate problem
            generate_problem(temp_json, temp_template, output_dir, force=True)

            # Assert files were created
            problem_dir = output_dir / "two_sum"
            assert problem_dir.exists()
            assert (problem_dir / "README.md").exists()
            assert (problem_dir / "solution.py").exists()
            assert (problem_dir / "test_solution.py").exists()
            assert (problem_dir / "helpers.py").exists()
            assert (problem_dir / "__init__.py").exists()

            # Assert content is correct
            solution_content = (problem_dir / "solution.py").read_text()
            assert "class Solution:" in solution_content
            assert "def two_sum(self, nums: list[int], target: int) -> list[int]:" in solution_content

            readme_content = (problem_dir / "README.md").read_text()
            assert "# Two Sum" in readme_content
            assert "Given an array of integers" in readme_content
