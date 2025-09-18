def run_can_complete_circuit(solution_class: type, gas: list[int], cost: list[int]):
    implementation = solution_class()
    return implementation.can_complete_circuit(gas, cost)


def assert_can_complete_circuit(result: int, expected: int) -> bool:
    assert result == expected
    return True
