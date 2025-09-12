def run_flood_fill(solution_class: type, image: list[list[int]], sr: int, sc: int, color: int):
    implementation = solution_class()
    return implementation.flood_fill(image, sr, sc, color)


def assert_flood_fill(result: list[list[int]], expected: list[list[int]]) -> bool:
    assert result == expected
    return True
