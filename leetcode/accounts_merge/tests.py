import pytest

from leetcode_py.test_utils import logged_test

from .solution import Solution


class TestAccountsMerge:
    def setup_method(self):
        self.solution = Solution()

    @pytest.mark.parametrize(
        "accounts, expected",
        [
            (
                [
                    ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
                    ["John", "johnsmith@mail.com", "john00@mail.com"],
                    ["Mary", "mary@mail.com"],
                    ["John", "johnnybravo@mail.com"],
                ],
                [
                    ["John", "john00@mail.com", "john_newyork@mail.com", "johnsmith@mail.com"],
                    ["Mary", "mary@mail.com"],
                    ["John", "johnnybravo@mail.com"],
                ],
            ),
            (
                [
                    ["Gabe", "Gabe0@m.co", "Gabe3@m.co", "Gabe1@m.co"],
                    ["Kevin", "Kevin3@m.co", "Kevin5@m.co", "Kevin0@m.co"],
                    ["Ethan", "Ethan5@m.co", "Ethan4@m.co", "Ethan0@m.co"],
                    ["Hanzo", "Hanzo3@m.co", "Hanzo1@m.co", "Hanzo0@m.co"],
                    ["Fern", "Fern5@m.co", "Fern1@m.co", "Fern0@m.co"],
                ],
                [
                    ["Ethan", "Ethan0@m.co", "Ethan4@m.co", "Ethan5@m.co"],
                    ["Gabe", "Gabe0@m.co", "Gabe1@m.co", "Gabe3@m.co"],
                    ["Hanzo", "Hanzo0@m.co", "Hanzo1@m.co", "Hanzo3@m.co"],
                    ["Kevin", "Kevin0@m.co", "Kevin3@m.co", "Kevin5@m.co"],
                    ["Fern", "Fern0@m.co", "Fern1@m.co", "Fern5@m.co"],
                ],
            ),
            # Single account
            (
                [["Alice", "alice@mail.com"]],
                [["Alice", "alice@mail.com"]],
            ),
            # No merging needed - all separate
            (
                [
                    ["Alice", "alice@mail.com"],
                    ["Bob", "bob@mail.com"],
                    ["Charlie", "charlie@mail.com"],
                ],
                [
                    ["Alice", "alice@mail.com"],
                    ["Bob", "bob@mail.com"],
                    ["Charlie", "charlie@mail.com"],
                ],
            ),
            # Chain merging - A->B->C
            (
                [
                    ["John", "john1@mail.com", "john2@mail.com"],
                    ["John", "john2@mail.com", "john3@mail.com"],
                    ["John", "john3@mail.com", "john4@mail.com"],
                ],
                [["John", "john1@mail.com", "john2@mail.com", "john3@mail.com", "john4@mail.com"]],
            ),
            # Multiple emails per account with complex merging
            (
                [
                    ["David", "david1@mail.com", "david2@mail.com", "david3@mail.com"],
                    ["David", "david3@mail.com", "david4@mail.com"],
                    ["Sarah", "sarah@mail.com"],
                    ["David", "david5@mail.com", "david1@mail.com"],
                ],
                [
                    [
                        "David",
                        "david1@mail.com",
                        "david2@mail.com",
                        "david3@mail.com",
                        "david4@mail.com",
                        "david5@mail.com",
                    ],
                    ["Sarah", "sarah@mail.com"],
                ],
            ),
            # Same name different people
            (
                [
                    ["John", "john1@mail.com"],
                    ["John", "john2@mail.com"],
                    ["John", "john3@mail.com"],
                ],
                [
                    ["John", "john1@mail.com"],
                    ["John", "john2@mail.com"],
                    ["John", "john3@mail.com"],
                ],
            ),
        ],
    )
    @logged_test
    def test_accounts_merge(self, accounts: list[list[str]], expected: list[list[str]]):
        result = self.solution.accounts_merge(accounts)
        # Sort both result and expected for comparison since order doesn't matter
        result_sorted = [sorted(account) for account in sorted(result)]
        expected_sorted = [sorted(account) for account in sorted(expected)]
        assert result_sorted == expected_sorted
