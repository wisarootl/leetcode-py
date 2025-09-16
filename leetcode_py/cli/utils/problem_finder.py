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


@lru_cache(maxsize=1)
def _build_problem_number_cache() -> dict[int, str]:
    json_path = get_problems_json_path()
    number_to_name_map: dict[int, str] = {}

    for json_file in json_path.glob("*.json"):
        try:
            with open(json_file) as f:
                data = json.load(f)
                problem_number = data.get("problem_number")
                if problem_number and problem_number.isdigit():
                    number_to_name_map[int(problem_number)] = data.get("problem_name", json_file.stem)
        except (json.JSONDecodeError, KeyError, OSError):
            continue

    return number_to_name_map


def find_problem_by_number(number: int) -> str | None:
    cache = _build_problem_number_cache()
    return cache.get(number)


def get_all_problems() -> list[str]:
    json_path = get_problems_json_path()
    return [json_file.stem for json_file in json_path.glob("*.json")]


def _add_problem_to_tag_map(
    problem_tags_map: dict[str, list[str]], problem_name: str, tag_name: str
) -> None:
    if problem_name not in problem_tags_map:
        problem_tags_map[problem_name] = []
    problem_tags_map[problem_name].append(tag_name)


@lru_cache(maxsize=1)
def _build_problem_tags_cache() -> dict[str, list[str]]:
    try:
        with open(get_tags_path()) as f:
            tags_data = json5.load(f)

        problem_tags_map: dict[str, list[str]] = {}

        for tag_name, problems in tags_data.items():
            if not isinstance(problems, list):
                continue

            for item in problems:
                if isinstance(item, dict) and "tag" in item:
                    # Include all problems from referenced tag
                    for problem_name in tags_data.get(item["tag"], []):
                        if isinstance(problem_name, str):
                            _add_problem_to_tag_map(problem_tags_map, problem_name, tag_name)
                elif isinstance(item, str):
                    _add_problem_to_tag_map(problem_tags_map, item, tag_name)

        return problem_tags_map
    except (ValueError, OSError, KeyError):
        return {}


def get_tags_for_problem(problem_name: str) -> list[str]:
    cache = _build_problem_tags_cache()
    return cache.get(problem_name, [])
