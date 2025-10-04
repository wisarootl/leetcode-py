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
from helpers import assert_character_replacement, run_character_replacement
from solution import Solution

# %%
# Example test case
s = "ABAB"
k = 2
expected = 4

# %%
result = run_character_replacement(Solution, s, k)
result

# %%
assert_character_replacement(result, expected)
