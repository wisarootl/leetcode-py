def run_coin_change(solution_class: type, coins: list[int], amount: int):
    implementation = solution_class()
    return implementation.coin_change(coins, amount)


def assert_coin_change(result: int, expected: int) -> bool:
    assert result == expected
    return True
