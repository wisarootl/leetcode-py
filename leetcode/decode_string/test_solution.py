import pytest

from leetcode_py import logged_test

from .helpers import assert_decode_string, run_decode_string
from .solution import Solution


class TestDecodeString:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "s, expected",
        [
            ("3[a]2[bc]", "aaabcbc"),
            ("3[a2[c]]", "accaccacc"),
            ("2[abc]3[cd]ef", "abcabccdcdcdef"),
            ("abc", "abc"),
            ("2[a]", "aa"),
            ("10[a]", "aaaaaaaaaa"),
            ("2[b3[a]]", "baaabaaa"),
            ("3[a]2[b2[c]]", "aaabccbcc"),
            ("100[leetcode]", "leetcode" * 100),
            (
                "2[2[y]pq4[2[jk]e1[f]]]ef",
                "yypqjkjkefjkjkefjkjkefjkjkefyypqjkjkefjkjkefjkjkefjkjkefef",
            ),
            ("", ""),
            ("a", "a"),
            ("2[3[a]b]", "aaabaaab"),
            ("3[2[ad]3[pf]]xyz", "adadpfpfpfadadpfpfpfadadpfpfpfxyz"),
            ("sd2[f2[e]g]i", "sdfeegfeegi"),
        ],
    )
    def test_decode_string(self, s: str, expected: str):
        result = run_decode_string(Solution, s)
        assert_decode_string(result, expected)
