def run_encode_decode(solution_class: type, strs: list[str]):
    implementation = solution_class()
    encoded = implementation.encode(strs)
    decoded = implementation.decode(encoded)
    return decoded


def assert_encode_decode(result: list[str], expected: list[str]) -> bool:
    assert result == expected
    return True
