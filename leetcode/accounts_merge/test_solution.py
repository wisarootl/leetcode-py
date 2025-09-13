import pytest

from leetcode_py.test_utils import logged_test

from .helpers import assert_accounts_merge, run_accounts_merge
from .solution import Solution


class TestAccountsMerge:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
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
            ([["Alice", "alice@mail.com"]], [["Alice", "alice@mail.com"]]),
            (
                [["Bob", "bob1@mail.com"], ["Bob", "bob2@mail.com"]],
                [["Bob", "bob1@mail.com"], ["Bob", "bob2@mail.com"]],
            ),
            (
                [
                    ["Alice", "alice@mail.com", "alice2@mail.com"],
                    ["Alice", "alice2@mail.com", "alice3@mail.com"],
                ],
                [["Alice", "alice2@mail.com", "alice3@mail.com", "alice@mail.com"]],
            ),
            (
                [
                    ["A", "a@mail.com", "b@mail.com"],
                    ["B", "b@mail.com", "c@mail.com"],
                    ["C", "c@mail.com", "d@mail.com"],
                ],
                [["A", "a@mail.com", "b@mail.com", "c@mail.com", "d@mail.com"]],
            ),
            ([["David", "david@mail.com"], ["David", "david@mail.com"]], [["David", "david@mail.com"]]),
            (
                [["Alex", "alex1@mail.com"], ["Bob", "bob1@mail.com"], ["Charlie", "charlie1@mail.com"]],
                [["Alex", "alex1@mail.com"], ["Bob", "bob1@mail.com"], ["Charlie", "charlie1@mail.com"]],
            ),
            (
                [
                    ["John", "john1@mail.com", "john2@mail.com"],
                    ["John", "john3@mail.com"],
                    ["Jane", "jane1@mail.com"],
                ],
                [
                    ["John", "john1@mail.com", "john2@mail.com"],
                    ["John", "john3@mail.com"],
                    ["Jane", "jane1@mail.com"],
                ],
            ),
            (
                [
                    ["User", "user@mail.com", "user1@mail.com"],
                    ["User", "user2@mail.com", "user@mail.com"],
                    ["User", "user3@mail.com", "user1@mail.com"],
                ],
                [["User", "user1@mail.com", "user2@mail.com", "user3@mail.com", "user@mail.com"]],
            ),
            (
                [
                    ["Test", "test1@mail.com"],
                    ["Test", "test2@mail.com"],
                    ["Test", "test1@mail.com", "test3@mail.com"],
                ],
                [["Test", "test2@mail.com"], ["Test", "test1@mail.com", "test3@mail.com"]],
            ),
            (
                [
                    ["Name", "a@mail.com", "b@mail.com", "c@mail.com"],
                    ["Name", "d@mail.com", "e@mail.com"],
                    ["Name", "c@mail.com", "f@mail.com"],
                ],
                [
                    ["Name", "d@mail.com", "e@mail.com"],
                    ["Name", "a@mail.com", "b@mail.com", "c@mail.com", "f@mail.com"],
                ],
            ),
        ],
    )
    def test_accounts_merge(self, accounts: list[list[str]], expected: list[list[str]]):
        result = run_accounts_merge(Solution, accounts)
        assert_accounts_merge(result, expected)
