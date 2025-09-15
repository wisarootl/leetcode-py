import inspect
from pathlib import Path

from leetcode_py.cli.utils.resources import get_problems_json_path, get_tags_path, get_template_path


def test_get_template_path_development():
    result = get_template_path()
    assert isinstance(result, Path)
    assert result.name == "leetcode"
    assert result.exists()
    assert result.is_absolute()


def test_get_template_path_structure():
    template_path = get_template_path()

    # Check expected subdirectories exist
    assert (template_path / "json").exists()
    assert (template_path / "json" / "problems").exists()
    assert (template_path / "json" / "tags.json5").exists()
    assert (template_path / "{{cookiecutter.problem_name}}").exists()


def test_get_problems_json_path():
    result = get_problems_json_path()
    assert isinstance(result, Path)
    assert result.parts[-2:] == ("json", "problems")
    assert result.exists()

    # Check it contains JSON files
    json_files = list(result.glob("*.json"))
    assert len(json_files) > 0
    assert any(f.name == "two_sum.json" for f in json_files)


def test_get_tags_path():
    result = get_tags_path()
    assert isinstance(result, Path)
    assert result.name == "tags.json5"
    assert result.exists()
    assert result.suffix == ".json5"


def test_get_template_path_relative_resolution():
    """Test that template path is resolved relative to __file__."""
    template_path = get_template_path()

    # Should be: leetcode_py/cli/resources/leetcode
    expected_parts = ("leetcode_py", "cli", "resources", "leetcode")
    assert template_path.parts[-4:] == expected_parts


def test_get_template_path_uses_relative_path():
    source = inspect.getsource(get_template_path)
    assert "__file__" in source
    assert "parent.parent" in source
    assert "resources" in source


def test_get_template_path_error_handling():
    source = inspect.getsource(get_template_path)
    assert "FileNotFoundError" in source
    assert "not found" in source.lower()


def test_path_functions_consistency():
    template_path = get_template_path()
    json_path = get_problems_json_path()
    tags_path = get_tags_path()

    # JSON path should be under template path
    assert str(json_path).startswith(str(template_path))

    # Tags path should be under template path
    assert str(tags_path).startswith(str(template_path))

    # Tags should be sibling to problems directory
    assert tags_path.parent == json_path.parent


def test_cookiecutter_template_exists():
    template_path = get_template_path()
    cookiecutter_dir = template_path / "{{cookiecutter.problem_name}}"

    assert cookiecutter_dir.exists()
    assert cookiecutter_dir.is_dir()

    # Check for expected template files
    expected_files = ["solution.py", "test_solution.py", "README.md", "helpers.py"]
    for filename in expected_files:
        assert (cookiecutter_dir / filename).exists(), f"Missing template file: {filename}"
