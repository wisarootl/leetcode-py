import json
from functools import lru_cache
from pathlib import Path

import json5

from .resources import get_problems_json_path, get_tags_path


def find_problems_by_tag(tag: str) -> list[str]:
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


def get_all_problems() -> list[str]:
    json_path = get_problems_json_path()
    return [json_file.stem for json_file in json_path.glob("*.json")]


@lru_cache(maxsize=1)
def _build_problem_tags_cache() -> dict[str, list[str]]:
    tags_file = get_tags_path()
    problem_tags_map: dict[str, list[str]] = {}

    try:
        with open(tags_file) as f:
            tags_data = json5.load(f)

        # Build reverse mapping: problem -> list of tags
        for tag_name, problems in tags_data.items():
            if isinstance(problems, list):
                for problem_name in problems:
                    if problem_name not in problem_tags_map:
                        problem_tags_map[problem_name] = []
                    problem_tags_map[problem_name].append(tag_name)

        return problem_tags_map
    except (ValueError, OSError, KeyError):
        return {}


def get_tags_for_problem(problem_name: str) -> list[str]:
    cache = _build_problem_tags_cache()
    return cache.get(problem_name, [])
