# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.17.3
#   kernelspec:
#     display_name: leetcode-py-py3.13
#     language: python
#     name: python3
# ---

# %%
from helpers import assert_longest_common_subsequence, run_longest_common_subsequence
from solution import Solution

# %%
# Example test case
text1 = "abcde"
text2 = "ace"
expected = 3

# %%
result = run_longest_common_subsequence(Solution, text1, text2)
result

# %%
assert_longest_common_subsequence(result, expected)
