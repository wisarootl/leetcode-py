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
from helpers import assert_count_substrings, run_count_substrings
from solution import Solution

# %%
# Example test case
s = "abc"
expected = 3

# %%
result = run_count_substrings(Solution, s)
result

# %%
assert_count_substrings(result, expected)
