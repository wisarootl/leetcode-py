def run_accounts_merge(solution_class: type, accounts: list[list[str]]):
    implementation = solution_class()
    return implementation.accounts_merge(accounts)


def assert_accounts_merge(result: list[list[str]], expected: list[list[str]]) -> bool:
    # Sort both result and expected for comparison since order doesn't matter
    result_sorted = [sorted(account) for account in sorted(result)]
    expected_sorted = [sorted(account) for account in sorted(expected)]
    assert result_sorted == expected_sorted
    return True
