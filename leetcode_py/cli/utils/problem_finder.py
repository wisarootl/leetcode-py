import json
from pathlib import Path
from typing import List

import json5

from .resources import get_problems_json_path, get_tags_path


def find_problems_by_tag(tag: str) -> List[str]:
    tags_file = get_tags_path()

    try:
        with open(tags_file) as f:
            tags_data = json5.load(f)
            return tags_data.get(tag, [])
    except (ValueError, OSError, KeyError):
        return []


def get_problem_json_path(problem_name: str) -> Path:
    json_path = get_problems_json_path()
    return json_path / f"{problem_name}.json"


def find_problem_by_number(number: int) -> str | None:
    json_path = get_problems_json_path()

    for json_file in json_path.glob("*.json"):
        try:
            with open(json_file) as f:
                data = json.load(f)
                if data.get("problem_number") == str(number):
                    return data.get("problem_name", json_file.stem)
        except (json.JSONDecodeError, KeyError, OSError):
            continue

    return None
