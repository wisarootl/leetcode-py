import pytest

from leetcode_py.cli.utils.problem_finder import (
    _build_problem_tags_cache,
    find_problem_by_number,
    find_problems_by_tag,
    get_all_problems,
    get_tags_for_problem,
)


def test_find_problem_by_number():
    # Test existing problem
    result = find_problem_by_number(1)
    assert result == "two_sum"

    # Test another existing problem
    result = find_problem_by_number(125)
    assert result == "valid_palindrome"


def test_find_problem_by_number_not_found():
    result = find_problem_by_number(99999)
    assert result is None


def test_find_problems_by_tag():
    # Test existing tag
    result = find_problems_by_tag("grind-75")
    assert isinstance(result, list)
    assert len(result) > 0

    # Test grind-75 tag (should have many problems)
    result = find_problems_by_tag("grind-75")
    assert isinstance(result, list)
    assert len(result) > 10  # Should have many problems


def test_find_problems_by_tag_not_found():
    result = find_problems_by_tag("nonexistent")
    assert result == []


def test_get_all_problems():
    result = get_all_problems()
    assert isinstance(result, list)
    assert len(result) > 0

    # Should contain known problems
    assert "two_sum" in result
    assert "valid_palindrome" in result


def test_get_tags_for_problem():
    # Test problem with known tags
    result = get_tags_for_problem("two_sum")
    assert isinstance(result, list)
    assert "grind-75" in result

    # Test problem that might not have tags
    result = get_tags_for_problem("nonexistent_problem")
    assert result == []


@pytest.mark.parametrize(
    "number,expected",
    [
        (1, "two_sum"),
        (125, "valid_palindrome"),
        (99999, None),
    ],
)
def test_find_problem_by_number_parametrized(number, expected):
    result = find_problem_by_number(number)
    assert result == expected


@pytest.mark.parametrize(
    "tag,should_exist",
    [
        ("grind-75", True),
        ("grind-75", True),
        ("nonexistent", False),
    ],
)
def test_find_problems_by_tag_parametrized(tag, should_exist):
    result = find_problems_by_tag(tag)
    if should_exist:
        assert len(result) > 0
    else:
        assert len(result) == 0


def test_problem_finder_consistency():
    """Test that problem finder functions are consistent with each other."""
    all_problems = get_all_problems()

    # Test that problems found by number are in all_problems
    for number in [1, 125]:
        problem = find_problem_by_number(number)
        if problem:
            assert problem in all_problems

    # Test that problems found by tag are in all_problems
    grind_problems = find_problems_by_tag("grind-75")
    for problem in grind_problems:
        assert problem in all_problems


def test_build_problem_tags_cache_with_real_tags():
    result = _build_problem_tags_cache()

    # Test that grind tag includes both grind-75 problems and daily_temperatures
    assert "daily_temperatures" in result
    assert "grind" in result["daily_temperatures"]

    # Test that grind-75 problems also get grind tag
    assert "two_sum" in result
    assert "grind-75" in result["two_sum"]
    assert "grind" in result["two_sum"]


def test_get_tags_for_problem_extended():
    # Test daily_temperatures has grind tag
    tags = get_tags_for_problem("daily_temperatures")
    assert "grind" in tags

    # Test grind-75 problem has both tags
    tags = get_tags_for_problem("two_sum")
    assert "grind-75" in tags
    assert "grind" in tags
