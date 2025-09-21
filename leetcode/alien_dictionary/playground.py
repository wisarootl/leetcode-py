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
from helpers import assert_alien_order, run_alien_order
from solution import Solution

# %%
# Example test case
words = ["wrt", "wrf", "er", "ett", "rftt"]
expected = "wertf"

# %%
result = run_alien_order(Solution, words)
result

# %%
assert_alien_order(result, expected)
