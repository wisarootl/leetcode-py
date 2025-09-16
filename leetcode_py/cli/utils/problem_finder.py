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

        problems = []
        tag_items = tags_data.get(tag, [])

        for item in tag_items:
            if isinstance(item, dict) and "tag" in item:
                # Resolve tag reference
                referenced_problems = find_problems_by_tag(item["tag"])
                problems.extend(referenced_problems)
            elif isinstance(item, str):
                problems.append(item)

        return problems
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


def _process_tag_reference(item: dict, tag_name: str, problem_tags_map: dict[str, list[str]]) -> None:
    referenced_problems = find_problems_by_tag(item["tag"])
    for problem_name in referenced_problems:
        _add_problem_to_tag_map(problem_tags_map, problem_name, tag_name)


def _process_tag_item(item: str | dict, tag_name: str, problem_tags_map: dict[str, list[str]]) -> None:
    if isinstance(item, dict) and "tag" in item:
        _process_tag_reference(item, tag_name, problem_tags_map)
    elif isinstance(item, str):
        _add_problem_to_tag_map(problem_tags_map, item, tag_name)


@lru_cache(maxsize=1)
def _build_problem_tags_cache() -> dict[str, list[str]]:
    try:
        with open(get_tags_path()) as f:
            tags_data = json5.load(f)

        problem_tags_map: dict[str, list[str]] = {}

        for tag_name, problems in tags_data.items():
            if isinstance(problems, list):
                for item in problems:
                    _process_tag_item(item, tag_name, problem_tags_map)

        return problem_tags_map
    except (ValueError, OSError, KeyError):
        return {}


def get_tags_for_problem(problem_name: str) -> list[str]:
    cache = _build_problem_tags_cache()
    return cache.get(problem_name, [])
