from pathlib import Path


def get_template_path() -> Path:
    current_file = Path(__file__)
    resources_path = current_file.parent.parent / "resources" / "leetcode"

    if resources_path.exists():
        return resources_path

    raise FileNotFoundError(f"Template resources not found at {resources_path}.")


def get_problems_json_path() -> Path:
    return get_template_path() / "json" / "problems"


def get_tags_path() -> Path:
    return get_template_path() / "json" / "tags.json5"
