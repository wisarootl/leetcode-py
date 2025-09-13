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
from helpers import assert_find_anagrams, run_find_anagrams
from solution import Solution

# %%
# Example test case
s = "cbaebabacd"
p = "abc"
expected = [0, 6]

# %%
result = run_find_anagrams(Solution, s, p)
result

# %%
assert_find_anagrams(result, expected)
