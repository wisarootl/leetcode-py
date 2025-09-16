from leetcode_py.cli.utils.problem_finder import _build_problem_tags_cache, get_tags_for_problem


def test_build_problem_tags_cache_with_real_tags():
    result = _build_problem_tags_cache()

    # Test that grind tag includes both grind-75 problems and daily_temperatures
    assert "daily_temperatures" in result
    assert "grind" in result["daily_temperatures"]

    # Test that grind-75 problems also get grind tag
    assert "two_sum" in result
    assert "grind-75" in result["two_sum"]
    assert "grind" in result["two_sum"]


def test_get_tags_for_problem():
    # Test daily_temperatures has grind tag
    tags = get_tags_for_problem("daily_temperatures")
    assert "grind" in tags

    # Test grind-75 problem has both tags
    tags = get_tags_for_problem("two_sum")
    assert "grind-75" in tags
    assert "grind" in tags
